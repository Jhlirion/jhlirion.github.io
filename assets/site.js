// Los detalles funcionan sin JavaScript. Esta mejora mantiene una tarjeta
// abierta a la vez cuando la persona explora las especialidades.
const services = [...document.querySelectorAll('.service')];
for (const service of services) {
  service.addEventListener('toggle', () => {
    const label = service.querySelector('.expand-text');
    label.textContent = service.open ? 'Cerrar detalle' : 'Ver enfoque';
    if (service.open) {
      for (const other of services) {
        if (other !== service) other.open = false;
      }
    }
  });
  service.querySelector('.expand-text').textContent = service.open ? 'Cerrar detalle' : 'Ver enfoque';
}
