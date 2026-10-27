# jhlirion — sitio personal

Web estática de Helton Lirion: datos, IA y automatización para empresas.

## Vista previa local

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Abrir http://127.0.0.1:4173/ . Este servidor sirve archivos directamente; no aplica las exclusiones de Jekyll.

## Validación

```sh
python3 scripts/check_site.py
node --check assets/site.js
```

## GitHub Pages

Configuración remota comprobada el 27 de octubre de 2026: `main`, `/ (root)`, HTTPS activo. `index.html` es la entrada. `_config.yml` excluye documentación y scripts del sitio generado. No añadir `.nojekyll`, porque se perderían esas exclusiones.

Un push a `main` activa la publicación con la configuración actual. Revisar los cambios y las validaciones antes de publicar.

Ver [auditoría de preparación](docs/PAGES_READINESS.md), [roadmap](docs/ROADMAP.md) y [créditos visuales](docs/VISUAL_ASSETS.md).
