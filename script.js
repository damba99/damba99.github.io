//Carrusel about

let indiceDiapositivaActual = 0; // Inicializar el índice en 0
mostrarDiapositiva(indiceDiapositivaActual);

function botonCarrusel(n) {
  mostrarDiapositiva(indiceDiapositivaActual += n);
}

function mostrarDiapositiva(n) {
  let diapo = about.getElementsByClassName("image_x");
  if (n >= diapo.length) {
    indiceDiapositivaActual = 0; // Vuelve a la primer diapositiva si n es mayor al largo de la lista que contiene a las imágenes
  }
  if (n < 0) {
    indiceDiapositivaActual = diapo.length - 1; // Va a la última diapositiva si n es menor 0(primer diapositiva)
  }
  for (let i = 0; i < diapo.length; i++) {
    diapo[i].style.display = "none";
  }
  diapo[indiceDiapositivaActual].style.display = "block";
}

//formulario

document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('contactForm');

  form.addEventListener('submit', function(event) {
      event.preventDefault(); // Evita el envío del formulario
      alert('El envío del formulario ha sido prevenido.');
  });
});