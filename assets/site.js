// La navegación permanece visible y funcional si JavaScript no está disponible.
const toggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#main-nav');
if (toggle && navigation) {
  document.documentElement.classList.add('js');
  toggle.hidden = false;
  const mobile = window.matchMedia('(max-width: 700px)');
  const closeMenu = () => {
    navigation.removeAttribute('data-open');
    toggle.setAttribute('aria-expanded', 'false');
  };
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    navigation.toggleAttribute('data-open', open);
  });
  navigation.addEventListener('click', (event) => {
    const link = event.target.closest('a[href^="#"]');
    if (!link) return;
    closeMenu();
    document.querySelector(link.getAttribute('href'))?.focus({ preventScroll: true });
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      closeMenu();
      toggle.focus();
    }
  });
  document.addEventListener('click', (event) => {
    if (!event.target.closest('.header-inner')) closeMenu();
  });
  navigation.addEventListener('focusout', (event) => {
    if (!navigation.contains(event.relatedTarget) && event.relatedTarget !== toggle) closeMenu();
  });
  mobile.addEventListener('change', closeMenu);
}
const year = document.querySelector('#year');
if (year) year.textContent = new Intl.DateTimeFormat('en', { year: 'numeric', timeZone: 'America/Lima' }).format(new Date());
