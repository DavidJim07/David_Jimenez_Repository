
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
        //console.log(opcionDefecto, cantidad, selector2);

        precio.innerHTML="$"+(opcionDefecto*selector2);
        renderizar();
    }else if (tipo==1){
        //console.log(selectId,tipo);
        var selector = document.getElementById(selectId);
        var opciones = selector.options[selector.selectedIndex];
      
        var selector2 = opciones.value;
        var cantidad = opciones.textContent;
        var precio = document.getElementById("total"+selectId);
        //console.log(cantidad, selector2,"**");

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
    var totalProductos = document.getElementById("totalProductos");
    var titulo = document.getElementById("titulo");

    subtotal.innerHTML="Subtotal: ("+total+") $"+subtotal3.toLocaleString();
    subtotal2.innerHTML="Subtotal: ("+total+") $"+subtotal3.toLocaleString();
    totalProductos.innerHTML=subtotal3.toLocaleString();
    titulo.innerHTML="Proceder a Pago ("+total+")";
    if(total==0){
        window.localStorage.removeItem('carrito');
        document.getElementById("formularioBorrar").submit();
    }
}

function pagar(){
    let zapatos=[];
    subtotal3=0;
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
            subtotal3+= parseInt(opciones.value)*parseInt(opciones.textContent);
            zapatos.push(zapato);
        }
    }
    var myInput = document.getElementById("myInput3");
    myInput.value= JSON.stringify(zapatos);
    var mytotal = document.getElementById("subtotal3");
    mytotal.value=subtotal3;
    window.localStorage.removeItem('carrito');
    //console.log("Termine");
    return true;
}

function registrarTarjeta(tipo){
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
    if(tipo==0){
        var myInput = document.getElementById("myInputTarjeta");
        myInput.value= JSON.stringify(zapatos);
    }else if(tipo==1){
        var myInput = document.getElementById("myInputTarjeta2");
        myInput.value= JSON.stringify(zapatos);
    }
}

function vaciarCarrito(event) {
    event.preventDefault();
    window.localStorage.removeItem('carrito');
    document.getElementById("formularioBorrar").submit();
}