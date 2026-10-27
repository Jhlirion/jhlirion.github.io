# Preparación para GitHub Pages

Evaluación previa a la publicación: 27 de octubre de 2026. Este documento registra las comprobaciones previas al commit; el build y la publicación deben verificarse después del push.

## Configuración remota consultada, sin cambios

Repositorio público: `Jhlirion/jhlirion.github.io`. Rama predeterminada: `main`.

Respuesta de `gh api repos/Jhlirion/jhlirion.github.io/pages`:

```json
{"build_type":"legacy","html_url":"https://jhlirion.github.io/","https_enforced":true,"source":{"branch":"main","path":"/"},"status":"built"}
```

El estado `built` corresponde a la versión previamente publicada, no a este rediseño. No se modificaron ajustes del repositorio.

## Compatibilidad y cambios preparados

| Área | Resultado |
| --- | --- |
| Entrada | `index.html` en raíz, compatible con la fuente actual |
| Ejecución | HTML/CSS/JS estáticos; sin backend, claves, instalación npm ni servicios de ejecución externos |
| Recursos | SVG, iconos y Pacifico servidos desde el mismo sitio; referencias locales verificadas, incluidas mayúsculas |
| HTTPS | Activado en configuración remota; enlaces externos del sitio usan HTTPS |
| Jekyll | `_config.yml` define URL y exclusiones; no se utiliza `.nojekyll` |
| Exclusiones | `docs`, `scripts`, `README.md`, `_site` |
| Metadatos | Título, descripción, idioma, canonical, Open Graph básico y favicon |
| Indexación | `robots.txt` y `sitemap.xml` para la URL confirmada |
| Direcciones inexistentes | `404.html` con enlaces absolutos para volver al inicio |
| Contacto | Enlace único a WhatsApp; no se enviaron mensajes ni se comprobó la titularidad del número |
| Marca | `jhlirion` sin punto; Pacifico con licencia local |
| Logos | Claude, OpenAI y n8n, SVG de Simple Icons 15.15.0; licencia incluida |
| Gráficos | SVG propios, conceptuales; no representan métricas de clientes ni resultados reales |
| Alcance editorial | Perfil y servicios; sin revelar productos reservados |

Las exclusiones evitan publicar esos archivos en el sitio generado. No los vuelven privados dentro de un repositorio público. No se han colocado secretos en ellos.

## Comprobaciones

- `python3 scripts/check_site.py`: estructura HTML, un H1 por página, IDs únicos, anclas, recursos locales y mayúsculas, fuentes CSS, XML/SVG, exclusiones y patrones evidentes de credenciales.
- `node --check assets/site.js`: sintaxis correcta.
- `git diff --check`: sin errores de espacios.
- Navegación real y carga de gráficos/iconos en Chrome; tarjeta accesible mediante Enter.
- Revisión visual en escritorio y móvil (390 y 320 px), sin desbordamiento horizontal medido. Los detalles nativos ofrecen una base sin JavaScript; el comportamiento de apertura exclusiva se comprobó con Enter.
- `404.html` abierto en navegador y regreso al inicio comprobado.
- Sin advertencias o errores en los registros de navegador consultados.
- Recursos activos de aproximadamente 352 KB, incluida la fuente. Este tamaño no equivale a una medición de Core Web Vitals.

## Límites de la verificación

- Jekyll no está instalado en el entorno; no se ejecutó un build Jekyll local. La aplicación de exclusiones y el artefacto final deben comprobarse en el primer build de Pages.
- No se ejecutó Lighthouse ni se certifica conformidad completa WCAG. La órbita continúa sin control de pausa por solicitud del usuario; se respeta la preferencia del sistema de movimiento reducido.
- Imagen social personalizada opcional pendiente. No es un requisito para publicar.
- La limpieza solicitada retira toda la plantilla `virtual-folio/`, incluida la foto que ya faltaba, y los recursos descartados de `assets/images/`. No hay dependencias activas de esos archivos.

## Secuencia de publicación

1. Revisar el diff final y el contenido de los archivos nuevos.
2. Ejecutar los controles locales anteriores.
3. Crear el commit y hacer push a `main` (autorizados por el usuario el 27 de octubre de 2026). El push activa la publicación actual.
4. Revisar el resultado del build de Pages y abrir la URL publicada.
5. Comprobar CSS, JS, fuentes, SVG, 404, navegación móvil y contacto.
6. Verificar que `/docs/ROADMAP.md` y las rutas antiguas excluidas no son servidas. Tras la publicación, deben responder 404; si no ocurre, corregir exclusiones antes de darla por cerrada.

## Referencias oficiales

- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll
