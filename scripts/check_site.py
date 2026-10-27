#!/usr/bin/env python3
"""Valida referencias, SVG y límites de publicación de este sitio estático."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.refs = []
        self.h1_count = 0
        self.stack = []
        self.lang = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        self.h1_count += tag == 'h1'
        for key in ('src', 'href'):
            if attrs.get(key):
                self.refs.append(attrs[key])
        if tag not in {'meta', 'link', 'img', 'br', 'hr', 'input', 'source',
                       'area', 'base', 'col', 'embed', 'param', 'track', 'wbr'}:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, f'Cierre HTML inválido: {tag}'
        self.stack.pop()


def local_ref(origin, ref):
    url = urlsplit(ref)
    if url.scheme or url.netloc:
        assert url.scheme in {'https', 'mailto', 'tel'}, f'URL insegura: {ref}'
        return None, ''
    path = unquote(url.path)
    target = ((ROOT / path.lstrip('/')) if path.startswith('/')
              else origin.parent / path) if path else origin
    if target.is_dir():
        target /= 'index.html'
    target = target.resolve()
    assert target.is_relative_to(ROOT), f'Referencia fuera del sitio: {ref}'
    assert target.is_file(), f'Recurso ausente: {origin.name}: {ref}'
    # Detecta diferencias de mayúsculas incluso en un filesystem no sensible.
    part = ROOT
    for segment in target.relative_to(ROOT).parts:
        assert segment in {p.name for p in part.iterdir()}, f'Mayúsculas incorrectas: {ref}'
        part /= segment
    assert not set(target.relative_to(ROOT).parts) & {'docs', 'scripts', 'virtual-folio', 'images'}, f'Recurso excluido: {ref}'
    return target, unquote(url.fragment)


pages = {}
for name in ('index.html', '404.html'):
    path = ROOT / name
    page = Page()
    page.feed(path.read_text())
    assert page.lang == 'es' and page.h1_count == 1 and not page.stack, name
    assert len(page.ids) == len(set(page.ids)), f'IDs duplicados: {name}'
    pages[path] = page
for origin, page in pages.items():
    for ref in page.refs:
        target, fragment = local_ref(origin, ref)
        if fragment:
            assert target in pages and fragment in pages[target].ids, f'Ancla ausente: {ref}'
for css in (ROOT / 'assets').rglob('*.css'):
    for ref in re.findall(r'url\([\s\'"]*([^\)\'"\s]+)', css.read_text()):
        local_ref(css, ref)
for svg in [*(ROOT / 'assets').rglob('*.svg'), ROOT / 'sitemap.xml']:
    ET.parse(svg)
source = (ROOT / 'index.html').read_text()
assert 'https://wa.me/51991814543' in source
assert 'orbit-toggle' not in source and 'brand-dot' not in source
assert not any(word in source.lower() for word in ('asisai', 'florec', 'localhost', '127.0.0.1'))
config = (ROOT / '_config.yml').read_text()
assert not (ROOT / '.nojekyll').exists(), 'No omitir Jekyll: se perderían las exclusiones.'
for excluded in ('docs', 'scripts'):
    assert f'  - {excluded}' in config
active = [*(ROOT / 'assets').glob('*.css'), *(ROOT / 'assets').glob('*.js'),
          *(ROOT / 'assets').glob('*.svg'), *(ROOT / 'assets' / 'graphics').glob('*.svg'),
          *(ROOT / 'assets' / 'icons').glob('*.svg'), *(ROOT / 'assets' / 'fonts').glob('*')]
for path in [*pages, *active]:
    if path.suffix in {'.html', '.js', '.css', '.svg'}:
        content = path.read_text()
        assert not re.search(r'AIza[\w-]{30,}|sk-(?:proj-)?[A-Za-z0-9_-]{20,}|BEGIN (?:RSA |EC )?PRIVATE KEY', content), f'Posible credencial: {path}'
assert all(p.stat().st_size < 100 * 1024 * 1024 for p in active)
print('OK: HTML, anclas, recursos, mayúsculas, SVG/XML y exclusiones de publicación.')
print('OK: contacto de WhatsApp y ausencia de proyectos reservados o credenciales detectables.')
print(f'Recursos activos: {sum(p.stat().st_size for p in active) / 1024:.0f} KB; sin backend ni build de Node.')
