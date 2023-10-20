var checkbox = document.getElementById("flexCheckDefault");

if (checkbox.checked) {
  var cajaDeTexto = document.getElementById("pais");
  cajaDeTexto.disabled = false;
  var cajaDeTexto2 = document.getElementById("estado");
  cajaDeTexto2.disabled = false;
  var cajaDeTexto3 = document.getElementById("ciudad");
  cajaDeTexto3.disabled = false;
  var cajaDeTexto2 = document.getElementById("colonia");
  cajaDeTexto2.disabled = false;
  var cajaDeTexto = document.getElementById("codigoPostal");
  cajaDeTexto.disabled = false;
  var cajaDeTexto2 = document.getElementById("calle");
  cajaDeTexto2.disabled = false;
  var cajaDeTexto3 = document.getElementById("numero");
  cajaDeTexto3.disabled = false;
  var cajaDeTexto2 = document.getElementById("entreCalles");
  cajaDeTexto2.disabled = false;
  var boton1 = document.getElementById("guardar");
  boton1.disabled = false;
  var boton2 = document.getElementById("limpiar");
  boton2.disabled = false;
} else {
  var cajaDeTexto = document.getElementById("pais");
  cajaDeTexto.disabled = true;
  var cajaDeTexto2 = document.getElementById("estado");
  cajaDeTexto2.disabled = true;
  var cajaDeTexto3 = document.getElementById("ciudad");
  cajaDeTexto3.disabled = true;
  var cajaDeTexto2 = document.getElementById("colonia");
  cajaDeTexto2.disabled = true;
  var cajaDeTexto = document.getElementById("codigoPostal");
  cajaDeTexto.disabled = true;
  var cajaDeTexto2 = document.getElementById("calle");
  cajaDeTexto2.disabled = true;
  var cajaDeTexto3 = document.getElementById("numero");
  cajaDeTexto3.disabled = true;
  var cajaDeTexto2 = document.getElementById("entreCalles");
  cajaDeTexto2.disabled = true;
  var boton1 = document.getElementById("guardar");
  boton1.disabled = true;
  var boton2 = document.getElementById("limpiar");
  boton2.disabled = true;
}



function verificarCheckbox() {
    // Obtener el elemento checkbox
    var checkbox = document.getElementById("flexCheckDefault");
  
    if (checkbox.checked) {
      var cajaDeTexto = document.getElementById("pais");
      cajaDeTexto.disabled = false;
      var cajaDeTexto2 = document.getElementById("estado");
      cajaDeTexto2.disabled = false;
      var cajaDeTexto3 = document.getElementById("ciudad");
      cajaDeTexto3.disabled = false;
      var cajaDeTexto2 = document.getElementById("colonia");
      cajaDeTexto2.disabled = false;
      var cajaDeTexto = document.getElementById("codigoPostal");
      cajaDeTexto.disabled = false;
      var cajaDeTexto2 = document.getElementById("calle");
      cajaDeTexto2.disabled = false;
      var cajaDeTexto3 = document.getElementById("numero");
      cajaDeTexto3.disabled = false;
      var cajaDeTexto2 = document.getElementById("entreCalles");
      cajaDeTexto2.disabled = false;
      var boton1 = document.getElementById("guardar");
      boton1.disabled = false;
      var boton2 = document.getElementById("limpiar");
      boton2.disabled = false;
    } else {
      var cajaDeTexto = document.getElementById("pais");
      cajaDeTexto.disabled = true;
      var cajaDeTexto2 = document.getElementById("estado");
      cajaDeTexto2.disabled = true;
      var cajaDeTexto3 = document.getElementById("ciudad");
      cajaDeTexto3.disabled = true;
      var cajaDeTexto2 = document.getElementById("colonia");
      cajaDeTexto2.disabled = true;
      var cajaDeTexto = document.getElementById("codigoPostal");
      cajaDeTexto.disabled = true;
      var cajaDeTexto2 = document.getElementById("calle");
      cajaDeTexto2.disabled = true;
      var cajaDeTexto3 = document.getElementById("numero");
      cajaDeTexto3.disabled = true;
      var cajaDeTexto2 = document.getElementById("entreCalles");
      cajaDeTexto2.disabled = true;
      var boton1 = document.getElementById("guardar");
      boton1.disabled = true;
      var boton2 = document.getElementById("limpiar");
      boton2.disabled = true;
    }
  }