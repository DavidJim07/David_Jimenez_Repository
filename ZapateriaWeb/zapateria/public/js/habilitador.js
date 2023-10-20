var checkbox = document.getElementById("flexCheckDefault");

if (checkbox.checked) {
  var cajaDeTexto = document.getElementById("tarjeta");
  cajaDeTexto.disabled = false;
  var cajaDeTexto2 = document.getElementById("numeroTarjeta");
  cajaDeTexto2.disabled = false;
  var cajaDeTexto3 = document.getElementById("vencimiento");
  cajaDeTexto3.disabled = false;
  var cajaDeTexto2 = document.getElementById("ccv");
  cajaDeTexto2.disabled = false;
  var boton1 = document.getElementById("guardar");
  boton1.disabled = false;
  var boton2 = document.getElementById("limpiar");
  boton2.disabled = false;
} else {
  var cajaDeTexto = document.getElementById("tarjeta");
  cajaDeTexto.disabled = true;
  var cajaDeTexto2 = document.getElementById("numeroTarjeta");
  cajaDeTexto2.disabled = true;
  var cajaDeTexto3 = document.getElementById("vencimiento");
  cajaDeTexto3.disabled = true;
  var cajaDeTexto2 = document.getElementById("ccv");
  cajaDeTexto2.disabled = true;
  var boton1 = document.getElementById("guardar");
  boton1.disabled = true;
  var boton2 = document.getElementById("limpiar");
  boton2.disabled = true;
}



function verificarCheckbox() {
    // Obtener el elemento checkbox
    var checkbox = document.getElementById("flexCheckDefault");
  
    // Verificar si el checkbox está marcado o no
    if (checkbox.checked) {
      var cajaDeTexto = document.getElementById("tarjeta");
      cajaDeTexto.disabled = false;
      var cajaDeTexto2 = document.getElementById("numeroTarjeta");
      cajaDeTexto2.disabled = false;
      var cajaDeTexto3 = document.getElementById("vencimiento");
      cajaDeTexto3.disabled = false;
      var cajaDeTexto2 = document.getElementById("ccv");
      cajaDeTexto2.disabled = false;
      var boton1 = document.getElementById("guardar");
      boton1.disabled = false;
      var boton2 = document.getElementById("limpiar");
      boton2.disabled = false;
    } else {
      var cajaDeTexto = document.getElementById("tarjeta");
      cajaDeTexto.disabled = true;
      var cajaDeTexto2 = document.getElementById("numeroTarjeta");
      cajaDeTexto2.disabled = true;
      var cajaDeTexto3 = document.getElementById("vencimiento");
      cajaDeTexto3.disabled = true;
      var cajaDeTexto2 = document.getElementById("ccv");
      cajaDeTexto2.disabled = true;
      var boton1 = document.getElementById("guardar");
      boton1.disabled = true;
      var boton2 = document.getElementById("limpiar");
      boton2.disabled = true;
    }
  }