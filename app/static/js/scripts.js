function validarFormulario() {
  var nombre = document.getElementById("id_nombre").value;
  var correo = document.getElementById("id_correo").value;

  if (nombre.trim() === "" || nombre.length < 3 || nombre.length > 20) {
    alert("Por favor, ingresa un nombre válido (entre 3 y 20 caracteres).");
    return false; // Evita que se envíe el formulario
  }

  if (correo.length < 5 || correo.indexOf("@") === -1) {
    alert(
      "Por favor, ingresa un correo válido (debe tener al menos 5 caracteres y contener '@')."
    );
    return false; // Evita que se envíe el formulario
  }

  return true; // Si todas las validaciones pasan, se enviará el formulario
}

$(document).ready(function () {
  $("#id_correo").on("blur", function () {
    var correo = $(this).val();
    if (correo.length < 5) {
      $(this).addClass("is-invalid");
    } else {
      $(this).removeClass("is-invalid");
    }
  });
});

document.addEventListener("DOMContentLoaded", function () {
  var vaciarCarritoBtn = document.getElementById("vaciar-carrito");
  if (vaciarCarritoBtn) {
    vaciarCarritoBtn.addEventListener("click", function () {
      // Realiza la lógica para vaciar el carrito aquí
      alert("Carrito vaciado");
    });
  }
});
