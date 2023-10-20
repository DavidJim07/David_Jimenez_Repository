
var iteraciones = document.getElementById("iteraciones").value;
for(let i=1; i<=iteraciones; i++){
    opcionAlterada(i,0);
}

function opcionAlterada(selectId,tipo) {
    if (tipo==0) {
        var selector = document.getElementById(selectId);
        var opciones = selector.options[selector.selectedIndex];
      
        var selector2 = opciones.value;
        var cantidad = opciones.textContent;
        var precio = document.getElementById("total"+selectId);
        
        var opcionDefecto = document.getElementById("opcionDefecto"+selectId).value;
        selector.selectedIndex = opcionDefecto-1;

        precio.innerHTML="$"+(opcionDefecto*selector2);
        renderizar();
    }else if (tipo==1){
        console.log(selectId,tipo);
        var selector = document.getElementById(selectId);
        var opciones = selector.options[selector.selectedIndex];
      
        var selector2 = opciones.value;
        var cantidad = opciones.textContent;
        var precio = document.getElementById("total"+selectId);

        precio.innerHTML="$"+(selector2*cantidad);
        renderizar();
    }
}

function quitar(selectId) {
    var elemento = document.getElementById("contenedor"+selectId);
    elemento.remove();
    renderizar();
}

function renderizar() {
    total=0;
    subtotal3=0;
    var iteraciones = document.getElementById("iteraciones").value;
    for(let i=1; i<=iteraciones; i++){
        var elemento = document.getElementById("contenedor"+i);

        if (elemento != null) {
        // El elemento existe
            total++;
            var selector = document.getElementById(i);
            var opciones = selector.options[selector.selectedIndex];
            subtotal3+= parseInt(opciones.value)*parseInt(opciones.textContent);
        }
    }
    var subtotal = document.getElementById("subtotal");
    var subtotal2 = document.getElementById("subtotal2");

    subtotal.innerHTML="Subtotal: ("+total+") $"+subtotal3.toLocaleString();
    subtotal2.innerHTML="Subtotal: ("+total+") $"+subtotal3.toLocaleString();
    if(total==0){
        window.localStorage.removeItem('carrito');
        document.getElementById("formularioBorrar").submit();
    }
}

function pagar(){
    let zapatos=[];
    for(let i=1; i<=iteraciones; i++){
        var elemento = document.getElementById("contenedor"+i);

        if (elemento != null) {
            var selector = document.getElementById(i);
            var opciones = selector.options[selector.selectedIndex];

            var zapato = {
                idZapato: document.getElementById("idZapato"+i).value,
                idTalla: document.getElementById("idTalla"+i).value,
                cantidad: opciones.textContent
            };
            zapatos.push(zapato);
        }
    }
    var myInput = document.getElementById("myInput");
    myInput.value= JSON.stringify(zapatos);

    var label = document.getElementById('regalo');

    // Obtener el id del elemento de formulario vinculado al <label>
    var forAttribute = label.getAttribute('for');

    // Verificar si el elemento de formulario correspondiente está activo
    var inputElement = document.getElementById(forAttribute);
    var isActive = inputElement && inputElement.checked;

    if (isActive) {
        var input = document.getElementById('esRegalo');
        input.value=1;
    } else {
        var input = document.getElementById('esRegalo');
        input.value=0;
    }
}

function vaciarCarrito(event) {
    event.preventDefault();
    window.localStorage.removeItem('carrito');
    document.getElementById("formularioBorrar").submit();
}