# Validación del rediseño

Fecha: 28 de octubre de 2026. Estado: LOCAL ONLY. La web pública mantiene la versión anterior.

## GitHub Pages

Consulta de solo lectura del 28 de octubre:

- Repositorio: `Jhlirion/jhlirion.github.io`.
- URL: https://jhlirion.github.io/ .
- Dominio personalizado: ninguno (`cname: null`).
- Publicación: `main`, `/ (root)`; HTTPS activo.
- El estado remoto `built` pertenece a la publicación anterior, no a estos cambios.

La configuración existente se conserva. HTML/CSS/JS estáticos, sin backend, secretos ni build de Node. `_config.yml` mantiene la exclusión de `docs`, `scripts`, `README.md` y `_site`; no añadir `.nojekyll`, pues desactivaría esas exclusiones. La documentación del repositorio público no es privada, aunque no se sirva en Pages.

## Cambios

Hero aprobado con Helton Lirion; jhlirion como logo; cinco secciones y dos páginas de soluciones de referencia. About y cuatro especialidades actualizados con contenido proporcionado por el usuario. Se conservan canonical, sitemap y robots de producción. No hay imagen social inventada ni datos estructurados con perfiles/cargos inferidos.

Contact conserva canales previamente autorizados. No se enviaron mensajes ni se verificó la titularidad del WhatsApp durante esta revisión.

## Evidencia local

- `python3 scripts/check_site.py`: HTML, títulos, anclas, recursos, mayúsculas, XML/SVG, exclusiones y contenido aprobado.
- `node --check assets/site.js`: sintaxis.
- `git diff --check`: formato.
- Chrome: sin desbordamiento medido en 320, 375, 768, 1024 y 1440 px.
- Inspección visual de móvil 320, tableta 768 y escritorio 1440, además de Projects y Contact.
- Teclado: apertura de menú con Enter, Tab entre opciones, Escape con devolución de foco y activación de Contact con cierre de menú y foco en la sección.
- CTA Ver proyectos navega a las dos tarjetas de referencia. Cada Explore Solution abre su detalle estático, con navegación de regreso y contacto.
- Las páginas nuevas se incluyen en sitemap y usan rutas .html sin requerir backend.
- Diagrama y texto distinguen diseño conceptual de implementación real.
- Texto principal medido mediante estilos computados: contraste mínimo 9.25:1 en los elementos evaluados. Es una comprobación parcial, no certificación WCAG completa.
- Enlaces y botones con altura mínima CSS de 44 px. Detalles decorativos no son controles.
- CSS contiene la regla `prefers-reduced-motion`; esta versión no tiene animaciones de contenido. No se cambió la preferencia del sistema para emularla.
- Registros consultados de Chrome: sin errores ni advertencias del sitio.

## Límites pendientes

- No se ejecutó Lighthouse: no hay puntuaciones de Performance, Accessibility o SEO para esta versión.
- No se completó una verificación de zoom nativo al 200 %; los atajos del navegador no alteraron el zoom en la superficie automatizada. La revisión por anchuras no se presenta como sustituto de esa prueba.
- No se ejecutó un build Jekyll local (no está instalado). El último despliegue anterior utilizó este mismo mecanismo, pero esta versión aún debe pasar su build remoto.
- No se ha publicado ni inspeccionado esta versión en producción.

## Después de una autorización de publicación

1. Revisar el diff y ejecutar los controles locales.
2. Crear commit y subir a `main`; el push activa Pages.
3. Confirmar que el workflow de esa revisión termina con éxito en build y deploy.
4. Abrir la URL pública en navegador y comprobar fuente, estilos, menú móvil, CTAs y 404.
5. Comprobar que los documentos/scripts excluidos responden 404 y que los recursos servidos no incluyen referencias reservadas.
6. Informar hash, estado de sincronización y evidencia pública por separado.

## Revisión de soluciones de referencia

- About incorpora identidad, enfoque y los tres principios proporcionados por el usuario.
- Expertise contiene cuatro categorías, sin certificaciones ni tecnologías dominadas inferidas.
- Dos tarjetas y páginas `.html` nuevas, con problema, arquitectura propuesta, componentes, funcionamiento previsto y límites. No hay ejecución de agentes ni procesamiento de datos real.
- Diagramas SVG cargados en navegador y navegación real a ambos detalles, regreso a soluciones y contacto mediante menú móvil comprobados.
- Página principal y ambos detalles medidos en 320, 375, 768, 1024 y 1440 px, sin desbordamiento horizontal.
- About inspeccionado en escritorio, Expertise y detalle de IA en móvil. Consola consultada sin errores ni advertencias.
- Sitemap y validador incluyen las páginas nuevas. Se conserva el mecanismo de Pages; no se ejecutó commit, push ni despliegue.

## Avatar y Medallion

- Avatar SVG provisional añadido a About, preparado para sustituirse por una foto.
- Tarjeta, diagrama y detalle de Data Architecture Optimization actualizados a Medallion, con finalidad analítica y Data Science.
- Página principal y detalle verificados nuevamente en 320, 375, 768, 1024 y 1440 px, sin desbordamiento; consola consultada sin errores.
- CSS y diagrama modificados usan una versión derivada de su contenido para evitar recursos antiguos en caché.
- El validador recorre todos los recursos de `assets/`, incluido el nuevo avatar.
- Cambios locales; no se ha realizado commit, push ni publicación.

## Ajuste de encabezado y redes sociales

- Robot SVG a la derecha del nombre en Home, sin pie ni texto de provisionalidad.
- About solo contiene presentación textual; valores integrados en la descripción.
- Etiqueta GitHub simplificada e Instagram `https://www.instagram.com/jhlirion/` añadido por instrucción explícita del usuario. Se comprobó su href, sin iniciar sesión ni interactuar en la red social.
- Encabezado inspeccionado en escritorio y móvil; sin desbordamiento medido en las cinco anchuras. Avatar cargado y enlaces locales válidos.
- Sin commit, push ni publicación.
