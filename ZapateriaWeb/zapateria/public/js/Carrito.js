//Carrito
let carrito = [];
const miLocalStorage = window.localStorage;

//Iterar sobre las tallas para setear precio y cantidad al cargar la pagina
var iteraciones = document.getElementById("iteraciones").value;
for(i=1; i<=iteraciones; i++){
    opcionAlterada(i)
}

cargarCarritoDeLocalStorage();
crearElementos(null,null);
calcularTotal();
var myInput = document.getElementById("myInput");
myInput.value= JSON.stringify(carrito);

function agregarAlCarrito(selectorId,idzapato) {
    cargarCarritoDeLocalStorage();
    var modeloZapato = document.getElementById("modelo"+idzapato).value;
    var etiquetaCantidad = document.getElementById("cantidad"+selectorId);
    var selector = document.getElementById(selectorId);
    var opciones = selector.options[selector.selectedIndex];
  
    var valor = opciones.value;
    var texto = opciones.textContent;

    var partes = valor.split("*");
    var cantidad = etiquetaCantidad.innerHTML.split(" ");

    var nuevoZapato = {
        idZapato: idzapato,
        idTalla: partes[2],
        talla: parseInt(texto),
        modelo: modeloZapato,
        precio: parseInt(partes[1]),
        selector: selectorId,
        cantidad: 1
    };

    indice=existe(nuevoZapato);
    if(indice==-1){
        carrito.push(nuevoZapato);
        calcularTotal();
    }else{
        carrito[indice].cantidad++;
        calcularTotal();
        if(cantidad[1]==carrito[indice].cantidad){
            var botonAgregar = document.getElementById("agregar"+selectorId);
            botonAgregar.disabled = true;
        }
    }
    var myInput = document.getElementById("myInput");
    myInput.value= JSON.stringify(carrito);
    guardarCarritoEnLocalStorage();
    crearElementos(selectorId);
}

function existe(nuevoZapato) {
    cargarCarritoDeLocalStorage();
    for(i=0; i<carrito.length; i++){
        if (carrito[i].idZapato == nuevoZapato.idZapato && carrito[i].talla == nuevoZapato.talla) {
            return i;
        }
    }
    return -1;
}

function crearElementos(selectId){
    cargarCarritoDeLocalStorage();
    var base = document.getElementById('carrito');
    base.innerHTML="";

    for(var i=0; i<carrito.length; i++){
        (function(index) {
            var elemento = document.createElement("li");
            elemento.id = carrito[index].idZapato+"**"+carrito[index].idTalla;
            elemento.className = 'list-group-item';
            var div1 = document.createElement("div");
            div1.id = "div1";
            div1.className = 'row';
            var div2 = document.createElement("div");
            div2.id = "div2";
            div2.className = 'col';
            div2.textContent = carrito[index].modelo;
            var div3 = document.createElement("div");
            div3.id = "div3";
            div3.className = 'col';
            div3.textContent = carrito[index].cantidad;
            var div4 = document.createElement("div");
            div4.id = "div4";
            div4.className = 'col';
            div4.textContent = "$"+(carrito[index].cantidad*carrito[index].precio);
            var div5 = document.createElement("div");
            div5.id = "div4";
            div5.className = 'col';
            div5.textContent = carrito[index].talla;
            var div6 = document.createElement("div");
            div6.id = "div6";
            div6.className = 'col';
            var miBoton = document.createElement("button");
            miBoton.className='btn btn-danger';
            miBoton.textContent = 'X';
            miBoton.onclick = function() {
                //console.log("Index: ",index," || SelectId: ",carrito[index].selector)
                borrarItemCarrito(index,carrito[index].selector);
            };

            elemento.appendChild(div1);
            div1.appendChild(div2);
            div1.appendChild(div3);
            div1.appendChild(div4);
            div1.appendChild(div5);
            div6.appendChild(miBoton);
            div1.appendChild(div6);
            base.appendChild(elemento);
        })(i);
    }
}

function borrarItemCarrito(indice,selectId) {
    cargarCarritoDeLocalStorage();
    if(carrito[indice].cantidad==1){
        carrito.splice(indice, 1);
        guardarCarritoEnLocalStorage();
        calcularTotal();
        verificarEstadoBoton(null,selectId);
    }else{
        carrito[indice].cantidad--; 
        guardarCarritoEnLocalStorage();
        calcularTotal();
        verificarEstadoBoton(indice,selectId);
    }
    var myInput = document.getElementById("myInput");
    myInput.value= JSON.stringify(carrito);
    crearElementos(selectId);
}

function verificarEstadoBoton(indice,selectId){
    if(selectId!=null && indice!=null){
        cargarCarritoDeLocalStorage();
        var selector = document.getElementById(carrito[indice].selector);
        var opciones = selector.options[selector.selectedIndex];
      
        var valor = opciones.value;
        var texto = opciones.textContent;
    
        var partes = valor.split("*");
        //console.log(partes,texto,indice,selectId,"|||||",carrito[indice]);
        //console.log("Holaaa ",carrito[indice])
        
        if(carrito[indice].idZapato==partes[3] && parseInt(carrito[indice].talla)==parseInt(texto)){
            if(carrito[indice].cantidad<partes[0]){
                //console.log("Entro con "+carrito[indice].cantidad)
                var botonAgregar = document.getElementById("agregar"+carrito[indice].selector);
                botonAgregar.disabled = false;
            }else if(carrito[indice].cantidad>=partes[0]){
                var botonAgregar = document.getElementById("agregar"+carrito[indice].selector);
                botonAgregar.disabled = true;
            }
        }
    }else if(selectId!=null && indice==null){
        cargarCarritoDeLocalStorage();
        modificado=false;
        indice2=0;

        for(var i=0; i<carrito.length; i++){
            var selector = document.getElementById(carrito[i].selector);
            var opciones = selector.options[selector.selectedIndex];
            //console.log(opciones.textContent);
        
            var valor = opciones.value;
            var texto = opciones.textContent;
        
            var partes = valor.split("*");
            if(carrito[i].idZapato==partes[3] && parseInt(carrito[i].talla)==parseInt(texto)){
                //console.log("Index: ",i," || SelectId: ",carrito[i].selector,"****")
                if(carrito[i].cantidad<partes[0]){
                    var botonAgregar = document.getElementById("agregar"+carrito[i].selector);
                    botonAgregar.disabled = false;
                }else if(carrito[i].cantidad>=partes[0]){
                    var botonAgregar = document.getElementById("agregar"+carrito[i].selector);
                    botonAgregar.disabled = true;
                }
            }else if(carrito[i].selector==selectId && carrito[i].idZapato==partes[3]){
                modificado=true;
            }
        }

        if(modificado){
            var botonAgregar = document.getElementById("agregar"+carrito[indice2].selector);
            botonAgregar.disabled = false;
        }


    }
}

function guardarCarritoEnLocalStorage() {
    miLocalStorage.setItem('carrito', JSON.stringify(carrito));
}

function calcularTotal() {
    var total=0;
    for(var i=0; i<carrito.length; i++){
        total+=carrito[i].precio*carrito[i].cantidad;
    }
    var base = document.getElementById('total');
    base.innerHTML=total.toLocaleString();
    
}

function cargarCarritoDeLocalStorage() {
    if (miLocalStorage.getItem('carrito') !== null) {
        carrito = JSON.parse(miLocalStorage.getItem('carrito'));
    }else{
        carrito = [];
    }
}

function vaciarCarrito() {
    carrito = [];
    renderizarCarrito();
    localStorage.clear();
}

//Metodos que ayudan a gestionar los elementos
function opcionAlterada(selectId) {
    var selector = document.getElementById(selectId);
    var opciones = selector.options[selector.selectedIndex];
  
    var valor = opciones.value;
    var texto = opciones.textContent;

    var cantidad = document.getElementById("cantidad"+selectId);
    var precio = document.getElementById("precio"+selectId);

    var partes = valor.split("*");

    cantidad.innerHTML="Cantidad: "+partes[0];
    precio.innerHTML="$"+partes[1];
  
    // Puedes realizar otras acciones con los valores y texto seleccionados
    verificarEstadoBoton(null,selectId)
}

function extraerDatos(event) {
    var boton = event.target; // Botón que disparó el evento
    var etiquetaPadre = boton.parentNode; // Elemento padre del botón
    var datos = etiquetaPadre.textContent.trim(); // Contenido de la etiqueta padre
  
    console.log("Datos extraídos:", datos);
    // Puedes realizar otras acciones con los datos extraídos
}

