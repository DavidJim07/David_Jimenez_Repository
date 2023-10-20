let listaSeries = [];

function getDato(campo) {
  return document.getElementById(campo).value;
}
function getElement(campo) {
  return document.getElementById(campo);
}

class Serie {
    _titulo;
    _categorias;
    _temporadas;
    _estreno;
    _sinopsis;
    _imagen;
    _capitulos;
  
    constructor(
      titulo,
      categorias,
      temporadas,
      estreno,
      sinopsis,
      imagen,
      capitulos
    ) {
      this._titulo = titulo;
      this._categorias = categorias;
      this._temporadas = temporadas;
      this._estreno = estreno;
      this._sinopsis = sinopsis;
      this._imagen = imagen;
      this._capitulos = capitulos;
    }
  
    get titulo() {
      return this._titulo;
    }
  
    set titulo(titulo) {
      this._titulo = titulo;
    }
    
    get categorias() {
        return this._categorias;
    }

    set categorias(categorias) {
        this._categorias = categorias;
    }

    get temporadas() {
      return this._temporadas;
    }
  
    set temporadas(temporadas) {
      this._temporadas = temporadas;
    }
  
    get estreno() {
      return this._estreno;
    }
  
    set estreno(estreno) {
      this._estreno = estreno;
    }
  
    get sinopsis() {
      return this._sinopsis;
    }
  
    set sinopsis(sinopsis) {
      this._v = sinopsis;
    }
  
    get imagen() {
      return this._imagen;
    }
  
    set imagen(imagen) {
      this._imagen = imagen;
    }
  
    get capitulos() {
      return this._capitulos;
    }
  
    set capitulos(capitulos) {
      this._capitulos = capitulos;
    }
  
    agregarCapitulo(temporada, numeroCapitulo, titulo, duracion,  estreno, sinopsis,  imagen,  capitulo) {
      this._capitulos.push(temporada, numeroCapitulo, titulo, duracion,  estreno, sinopsis,  imagen,  capitulo);
    }
}
  
function iniciar(){
    let salida = `<br>
    <div class="container-fluid">
        <div class="card">
            <div class="card-header" >
                Registro de series
            </div>
            <div class="card-body">
                <div class="row">
                <div class="col-md-4">
                    <div class="mb-3">
                        <label class="form-label" >Titulo de la serie</label>
                        <input type="text" class="form-control" id="titulo" name="titulo">
                    </div>
                    <div class="mb-3">
                        <label  class="form-label">Categorias de la pelicula</label><br>
                        <input id="ciencia" type="checkbox" onclick="validarSelectores('ciencia')"/>Ciencia Ficción<br>
                        <input id="accion" type="checkbox" onclick="validarSelectores('accion')"/>Acción<br>
                        <input id="comedia" type="checkbox" onclick="validarSelectores('comedia')"/>Comedia <br>
                        <input id="fantasia" type="checkbox" onclick="validarSelectores('fantasia')"/>Fantasía <br>
                        <input id="drama" type="checkbox" onclick="validarSelectores('drama')"/>Drama/Melodrama <br>
                        <input id="musical" type="checkbox" onclick="validarSelectores('musical')"/>Musical <br>
                        <input id="romantico" type="checkbox" onclick="validarSelectores('romantico')"/>Romántico <br>
                        <input id="terror" type="checkbox" onclick="validarSelectores('terror')"/>Suspenso/Terror <br>
                    </div>
                    <div class="mb-3">
                        <label  class="form-label">Temporadas</label>
                        <input type="number" class="form-control" id="temporadas" name="temporadas" value="1" readonly>
                        <button type="submit" id="mas" name="mas" class="btn btn-primary btn-sm" onclick="incrementarSerie()">Mas</button> 
                        <button type="submit" id="menos" name="menos" class="btn btn-primary btn-sm" onclick="decrementarSerie()" disabled="true">Menos</button> 
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="mb-3">
                        <label  class="form-label">Fecha de estreno</label>
                        <input type="date" class="form-control" id="estreno" name="estreno">
                    </div>
                    <div class="mb-3">
                        <label  class="form-label">Sinopsis</label>
                        <textarea class="form-control" id="sinopsis" name="sinopsis" rows="2"></textarea>
                    </div>
                    <div class="mb-3">
                        <label  class="form-label">Imagen</label>
                        <input type="text" class="form-control" placeholder="URL de la imagen de la serie" id="imagen" name="imagen">
                    </div>
                </div>
                <div class="mb-3">
                    <button type="button" id="modificar" name="modificar" style="display:none" onclick="updateSerie()" class="btn btn-success">Modificar</button>
                    <button type="button" id="cancelar" name="cancelar" style="display:none" onclick="cancelarSerie()" class="btn btn-warning">Cancelar</button>
                    <button type="submit" id="guardar" name="guardar" class="btn btn-success" onclick="agregarSerie()">Guardar serie</button>  
                    <button type="reset" id="limpiar" name="limpiar" class="btn btn-warning" onclick="limpiarSeries()">Limpiar cajas</button>
                    <a id="listar" name="listar" class="btn btn-danger" onclick="mostrarSeries()">Listar</a>
                    <input type="text" id="pos" name="pos" value="" hidden>
                </div>
            </div>
        </div>
    </div>`;
    getElement("panelPrincipal").innerHTML = salida;

    let salida2 = `<div id="tituloSerie" name="tituloSerie"></div>
    <div class="container-fluid">
    <div class="card">
        <div class="card-header" >
            Registro de capitulos
        </div>
        <div class="card-body">
            <div class="row">
            <div class="col-md-4">
                <div class="mb-3">
                    <label class="form-label" >Temporada</label>
                    <div id="selectorTemporada" name="selectorTemporada"></div>
                </div>
                <br>
                <div class="mb-3">
                    <label  class="form-label">Número de capitulo</label>
                    <input type="number" class="form-control" id="numeroCapitulo" name="numeroCapitulo">
                </div>
                <div class="mb-3">
                    <label class="form-label" >Titulo del capitulo</label>
                    <input type="text" class="form-control" id="tituloCapitulo" name="tituloCapitulo">
                </div>
                <div class="mb-3">
                    <label  class="form-label">Duración del capitulo</label>
                    <input type="text" class="form-control" id="duracionCapitulo" name="duracionCapitulo">
                </div>
            </div>
            <div class="col-md-4">
                <div class="mb-3">
                    <label  class="form-label">Fecha de estreno</label>
                    <input type="date" class="form-control" id="estrenoCapitulo" name="estrenoCapitulo">
                </div>
                <div class="mb-3">
                    <label  class="form-label">Sinopsis</label>
                    <textarea class="form-control" id="sinopsisCapitulo" name="sinopsisCapitulo" rows="2"></textarea>
                </div>
                <div class="mb-3">
                    <label  class="form-label">Imagen</label>
                    <input type="text" class="form-control" placeholder="URL de la imagen del capitulo" id="imagenCapitulo" name="imagenCapitulo">
                </div>
                <div class="mb-3">
                    <label  class="form-label">Capitulo</label>
                    <input type="text" class="form-control" placeholder="URL del video del capitulo" id="capituloCapitulo" name="capituloCapitulo">
                </div>
            </div>
            <div class="mb-3">
                <button type="button" id="modificarCapitulos" name="modificarCapitulos" style="display:none" onclick="updateCapitulo()" class="btn btn-success">Modificar</button>
                <button type="button" id="cancelarCapitulos" name="cancelarCapitulos" style="display:none" onclick="cancelarCapitulo()" class="btn btn-warning">Cancelar</button>
                <button type='reset' id="regresarCapitulos" name="regresarCapitulos" class="btn btn-danger" onclick="regresar()">Regresar</button>
                <button type='submit' id="guardarCapitulos" name="guardarCapitulos" class="btn btn-success" onclick="addCapitulo()">Guardar capitulo</button>  
                <button type='reset' id="limpiarCapitulos" name="limpiarCapitulos" class="btn btn-warning" onclick="limpiarCapitulo()">Limpiar cajas</button>
                <a id='listarCapitulos' name="listarCapitulos" class="btn btn-primary" onclick="mostrarCapitulos()">Listar</a>
                <input type="text" id="temp" name="temp" value="" hidden>
                <input type="text" id="cap" name="cap" value="" hidden>
            </div>
        </div>
    </div>
    </div>`;
    getElement("panelCapitulos").innerHTML = salida2;

    getElement("panelCapitulos").style.display = 'none';
    getElement("vista").style.display = 'none';

    mostrarSeries();
}

function incrementarSerie(){
    temp=parseInt(getDato("temporadas"));
    temp++;
    getElement("temporadas").value=temp;
    getElement("menos").disabled=false;
}
function decrementarSerie(){
    temp=parseInt(getDato("temporadas"));
    temp--;
    getElement("temporadas").value=temp;
    if (temp==1) {
        getElement("menos").disabled=true;
    }
}

function objetoSerie(o) {
    let serie = new Object();
    serie["titulo"] = o.titulo;
    serie["categorias"] = o.categorias;
    serie["temporadas"] = o.temporadas;
    serie["estreno"] = o.estreno;
    serie["sinopsis"] = o.sinopsis;
    serie["imagen"] = o.imagen;
    //console.log(o.capitulos);
    for(i=1; i<=o.temporadas; i++){
        o.capitulos.push([]);
    }
    serie["capitulos"] = o.capitulos;
    return serie;
}

function agregarSerie() {
if (localStorage.getItem("series") == null) {
    let titulo = getDato("titulo");
    let categorias = getSelectores();
    let temporadas = getDato("temporadas");
    let estreno = getDato("estreno");
    let sinopsis = getDato("sinopsis");
    let imagen = getDato("imagen");

    let s = new Serie(titulo, categorias, temporadas, estreno, sinopsis,  imagen,  []);
    listaSeries.push(objetoSerie(s));
    localStorage.setItem("series", JSON.stringify(listaSeries));
    alert("Serie agregada correctamente");
    limpiarSeries();
    mostrarSeries();
} else {
    listaSeries = [];
    let nuevo = JSON.parse(localStorage.getItem("series"));
    for (const key in nuevo) {
    listaSeries[key] = nuevo[key];
    }
    let titulo = getDato("titulo");
    let categorias = getSelectores();
    let temporadas = getDato("temporadas");
    let estreno = getDato("estreno");
    let sinopsis = getDato("sinopsis");
    let imagen = getDato("imagen");

    let s = new Serie(titulo, categorias, temporadas, estreno, sinopsis,  imagen,  []);
    listaSeries.push(objetoSerie(s));
    localStorage.setItem("series", JSON.stringify(listaSeries));
    alert("Serie agregada correctamente");
    limpiarSeries();
    mostrarSeries();
}
}

function contarCapitulos(capitulos){
    let total=0
    for(i=0; i<capitulos.length; i++){
        total+=capitulos[i].length;
    }
    return total;
}

function mostrarSeries() {
    let salida = "<table class='table'> <thead><tr><th scope='col'>#</th><th scope='col'>Titulo</th> <th scope='col'>Temporadas</th> <th scope='col'>Categorias</th> <th scope='col'>Estreno</th> <th scope='col'>Sinopsis</th> <th scope='col'>Imagen</th> <th scope='col'>Capitulos</th> <th scope='col'>Acciones</th> </tr></thead><tbody>";
    let pos = 0;
    let nuevo = JSON.parse(localStorage.getItem("series"));
    if (nuevo) {
        for (const n of nuevo) {
        salida += `<tr>
        <td>${pos+1}</td>
        <td>${n.titulo}</td>
        <td>${n.temporadas}</td>
        <td>${mostrarCategorias(n.categorias)}</td>
        <td>${n.estreno}</td>
        <td>${n.sinopsis}</td>
        <td>${n.imagen}</td>
        <td>${contarCapitulos(n.capitulos)}</td>
        <td> <button class="btn btn-danger" onclick='eliminarSerie(${pos})'>Eliminar</button>
            <button class="btn btn-warning" onclick='modificarSerie(${pos})'>Modificar</button> 
            <button class="btn btn-danger" onclick='agregarSerieCapitulo(${pos})'>Agregar Capitulo</button>
        </td>
        </tr>`;
        pos++;
        }
        salida+="</tbody></table>"
        getElement("tablaSeries").innerHTML = salida;
    } 
}

function limpiarSeries() {
    getElement("titulo").value = "";
    getElement("temporadas").value = "1";
    getElement("menos").disabled=true;
    getElement("estreno").value = "";
    getElement("sinopsis").value = "";
    getElement("imagen").value = "";
    resetSelectores();
}

function eliminarSerie(pos) {
    //console.log(pos);
    listaSeries = [];
    let nuevo = JSON.parse(localStorage.getItem("series"));
    for (const key in nuevo) {
    listaSeries[key] = nuevo[key];
    }
    listaSeries.splice(pos, 1);
    localStorage.setItem("series", JSON.stringify(listaSeries));
    alert("Serie eliminada carrectamente");
    mostrarSeries();
}

function modificarSerie(pos) {
    //console.log(pos);
    listaSeries = [];
    let nuevo = JSON.parse(localStorage.getItem("series"));
    for (const key in nuevo) {
    listaSeries[key] = nuevo[key];
    }
    //console.log(listaSeries[pos]);
    getElement("titulo").value = listaSeries[pos].titulo;
    marcarSeleccionados(listaSeries[pos].categorias);
    getElement("temporadas").value = listaSeries[pos].temporadas;
    getElement("estreno").value = listaSeries[pos].estreno;
    getElement("sinopsis").value = listaSeries[pos].sinopsis;
    getElement("imagen").value = listaSeries[pos].imagen;

    if(listaSeries[pos].temporadas>=2){
        getElement("menos").disabled=false;
    }

    getElement("guardar").style.display = 'none';
    getElement("limpiar").style.display = 'none';
    getElement("listar").style.display = 'none';
    
    getElement("modificar").style.display = 'inline';
    getElement("cancelar").style.display = 'inline';

    getElement("pos").value=pos;

    getElement("tablaSeries").innerHTML = "";
}

function updateSerie(){
    pos = getElement("pos").value;
    //console.log(pos);
    listaSeries = [];
    let nuevo = JSON.parse(localStorage.getItem("series"));
    for (const key in nuevo) {
    listaSeries[key] = nuevo[key];
    }
    //listaSeries[pos].temporadas = getDato("temporadas");
    if(listaSeries[pos].temporadas!=getDato("temporadas")){
        if (listaSeries[pos].temporadas<getDato("temporadas")) {
            //console.log("Mensaje de que se van a agregar temporadas lo que implica agregar arrays");
            temp=getDato("temporadas")-listaSeries[pos].temporadas;
            for(i=1; i<=temp; i++){
                listaSeries[pos].capitulos.push([]);
            }
        } else {
            if (listaSeries[pos].temporadas>getDato("temporadas")) {
                //console.log("Mensaje de que se van a reducir temporadas lo que implica borrar capitulos");
                temp=listaSeries[pos].temporadas-getDato("temporadas");
                //console.log(listaSeries[pos].capitulos);
                listaSeries[pos].capitulos.splice(getDato("temporadas"), temp);
                //console.log(listaSeries[pos].capitulos);
            }
        }
        listaSeries[pos].temporadas = getDato("temporadas");
    }
    listaSeries[pos].titulo=getDato("titulo");
    listaSeries[pos].categorias = getSelectores();
    listaSeries[pos].estreno = getDato("estreno");
    listaSeries[pos].sinopsis = getDato("sinopsis");
    listaSeries[pos].imagen = getDato("imagen");
    localStorage.setItem("series", JSON.stringify(listaSeries));
    alert("Serie modificada carrectamente");
    cancelarSerie();
}

function cancelarSerie(){
    limpiarSeries();
    getElement("guardar").style.display = 'inline';
    getElement("limpiar").style.display = 'inline';
    getElement("listar").style.display = 'inline';
    
    getElement("modificar").style.display = 'none';
    getElement("cancelar").style.display = 'none';

    getElement("pos").value="";

    mostrarSeries();
}

function validarSelectores(seleccionado){
    let cont=0;
    if(getElement("ciencia").checked) {
        cont++;
    }
    if(getElement("accion").checked) {
        cont++;
    }
    if(getElement("comedia").checked) {
        cont++;
    }
    if(getElement("fantasia").checked) {
        cont++;
    }
    if(getElement("drama").checked) {
        cont++;
    }
    if(getElement("musical").checked) {
        cont++;
    }
    if(getElement("romantico").checked) {
        cont++;
    }
    if(getElement("terror").checked) {
        cont++;
    }
    if(cont>=4){
        getElement(seleccionado).checked=false;
    }
}

function getSelectores(){
    let categorias=[];
    if(getElement("ciencia").checked) {
        categorias.push("ciencia");
    }
    if(getElement("accion").checked) {
        categorias.push("accion");
    }
    if(getElement("comedia").checked) {
        categorias.push("comedia");
    }
    if(getElement("fantasia").checked) {
        categorias.push("fantasia");
    }
    if(getElement("drama").checked) {
        categorias.push("drama");
    }
    if(getElement("musical").checked) {
        categorias.push("musical");
    }
    if(getElement("romantico").checked) {
        categorias.push("romantico");
    }
    if(getElement("terror").checked) {
        categorias.push("terror");
    }
    return categorias;
}

function resetSelectores(){
    let categorias=[];
    if(getElement("ciencia").checked) {
        getElement("ciencia").checked=false
    }
    if(getElement("accion").checked) {
        getElement("accion").checked=false
    }
    if(getElement("comedia").checked) {
        getElement("comedia").checked=false
    }
    if(getElement("fantasia").checked) {
        getElement("fantasia").checked=false
    }
    if(getElement("drama").checked) {
        getElement("drama").checked=false
    }
    if(getElement("musical").checked) {
        getElement("musical").checked=false
    }
    if(getElement("romantico").checked) {
        getElement("romantico").checked=false
    }
    if(getElement("terror").checked) {
        getElement("terror").checked=false
    }
    return categorias;
}

function marcarSeleccionados(arreglo){
    for(let i=0; i<arreglo.length; i++){
        getElement(arreglo[i]).checked=true;
    }
}

function mostrarCategorias(arreglo){
    let salida="";
    for(let i=0; i<arreglo.length; i++){
    if(i==arreglo.length-1){
        salida+=arreglo[i];
    }else{
        salida+=arreglo[i]+", ";
    }
    }
    return salida;
}




//------------------------------------------------
function agregarSerieCapitulo(pos){
    //console.log(pos); 
    //getElement("panelPrincipal").style.display = (getElement("panelPrincipal").style.display == 'none') ? 'inline' : 'none'; 
    getElement("panelPrincipal").style.display = 'none';
    getElement("tablaSeries").innerHTML = "";

    getElement("panelCapitulos").style.display = 'inline';

    getElement("pos").value=pos;

    listaSeries = [];
    let nuevo = JSON.parse(localStorage.getItem("series"));
    for (const key in nuevo) {
        listaSeries[key] = nuevo[key];
    }
    //console.log(listaSeries[pos].temporadas+"***");
    let salida='<select class="form-select" aria-label="Default select example" id="temporadaCapitulo" name="temporadaCapitulo"';
    for(i=0; i<=listaSeries[pos].temporadas; i++){
        salida+="<option value='"+i+"'>"+i+"</option>";
    }
    salida += "</select>";

    getElement("selectorTemporada").innerHTML = salida;

    let salida2 = "<h1>"+listaSeries[pos].titulo+"</h1>";
    getElement("tituloSerie").innerHTML = salida2;

    mostrarCapitulos();
}

function regresar(){
    getElement("panelPrincipal").style.display = 'inline';
    getElement("panelCapitulos").style.display = 'none';
    
    getElement("tablaCapitulos").innerHTML = "";

    mostrarSeries();
}

function addCapitulo() {
    pos = getElement("pos").value;
    listaSeries = [];
    let nuevo = JSON.parse(localStorage.getItem("series"));
    for (const key in nuevo) {
        listaSeries[key] = nuevo[key];
    }
    
    let capitulo = new Object();
    capitulo["temporada"] = getDato("temporadaCapitulo");
    capitulo["numeroCapitulo"] = getDato("numeroCapitulo");
    capitulo["titulo"] = getDato("tituloCapitulo");
    capitulo["duracion"] = getDato("duracionCapitulo");
    capitulo["estreno"] = getDato("estrenoCapitulo");
    capitulo["sinopsis"] = getDato("sinopsisCapitulo");
    capitulo["imagen"] = getDato("imagenCapitulo");
    capitulo["capitulo"] = getDato("capituloCapitulo");

    capitulos=listaSeries[pos].capitulos;
    capitulos[getDato("temporadaCapitulo")-1].push(capitulo);
    listaSeries[pos].capitulos=capitulos;
    localStorage.setItem("series", JSON.stringify(listaSeries));
    alert("Capitulo agregado correctamente");
    limpiarCapitulo();
    mostrarCapitulos();
}

function mostrarCapitulos() {
    let salida = "";
    listaSeries = [];
    let nuevo = JSON.parse(localStorage.getItem("series"));
    for (const key in nuevo) {
        listaSeries[key] = nuevo[key];
    }

    let pos = getElement("pos").value;
    //let nuevo = JSON.parse(localStorage.getItem("peliculas"));
    //console.log(listaSeries[pos]);
    for(i=0; i<listaSeries[pos].capitulos.length; i++){
        //console.log(n.capitulos[i].length);
        if(listaSeries[pos].capitulos[i].length<=0){
            salida+="<br><h2>Temporada "+(i+1)+": sin capitulos aún.</h2>";
        }else{
            //console.log(listaSeries[pos].capitulos[i]);
            salida +="<br><table class='table'> <thead><tr><th scope='col'>#</th> <th scope='col'>Temporada</th> <th scope='col'>Número</th> <th scope='col'>Titulo</th> <th scope='col'>Duración</th> <th scope='col'>Estreno</th> <th scope='col'>Sinopsis</th> <th scope='col'>Imagen</th> <th scope='col'>Capitulos</th> <th scope='col'>Acciones</th> </tr></thead><tbody>";
            for(j=0; j<listaSeries[pos].capitulos[i].length; j++){
                salida += `<tr>
                <td>${pos+1}</td>
                <td>${listaSeries[pos].capitulos[i][j].temporada}</td>
                <td>${listaSeries[pos].capitulos[i][j].numeroCapitulo}</td>
                <td>${listaSeries[pos].capitulos[i][j].titulo}</td>
                <td>${listaSeries[pos].capitulos[i][j].duracion}</td>
                <td>${listaSeries[pos].capitulos[i][j].estreno}</td>
                <td>${listaSeries[pos].capitulos[i][j].sinopsis}</td>
                <td>${listaSeries[pos].capitulos[i][j].imagen}</td>
                <td>${listaSeries[pos].capitulos[i][j].capitulo}</td>
                <td> <button class="btn btn-danger" onclick='eliminarCapitulo(${pos},${i},${j})'>Eliminar</button>
                    <button class="btn btn-warning" onclick='modificarCapitulo(${pos},${i},${j})'>Modificar</button> </td>
                </tr>`;
            }
            salida+="</tbody></table>"
        }
    }
    getElement("tablaCapitulos").innerHTML = salida; 
}

function limpiarCapitulo() {
    let pos = getElement("pos").value;

    listaSeries = [];
    let nuevo = JSON.parse(localStorage.getItem("series"));
    for (const key in nuevo) {
        listaSeries[key] = nuevo[key];
    }

    let salida='<select class="form-select" aria-label="Default select example" id="temporadaCapitulo" name="temporadaCapitulo"';
    for(i=0; i<=listaSeries[pos].temporadas; i++){
        salida+="<option value='"+i+"'>"+i+"</option>";
    }
    salida += "</select>";

    getElement("selectorTemporada").innerHTML = salida;

    getElement("tituloCapitulo").value = "";
    getElement("numeroCapitulo").value = "";
    getElement("duracionCapitulo").value = "";
    getElement("estrenoCapitulo").value = "";
    getElement("sinopsisCapitulo").value = "";
    getElement("imagenCapitulo").value = "";
    getElement("capituloCapitulo").value = "";
}

function eliminarCapitulo(pos,temporada,posCap) {
    //  console.log(pos);
    listaSeries = [];
    let nuevo = JSON.parse(localStorage.getItem("series"));
    for (const key in nuevo) {
        listaSeries[key] = nuevo[key];
    }
    listaSeries[pos].capitulos[temporada].splice(posCap, 1);
    localStorage.setItem("series", JSON.stringify(listaSeries));
    alert("Capitulo eliminada carrectamente");
    mostrarCapitulos();
}

function modificarCapitulo(pos,temporada,posCap) {
    //console.log(pos);
    listaSeries = [];
    let nuevo = JSON.parse(localStorage.getItem("series"));
    for (const key in nuevo) {
        listaSeries[key] = nuevo[key];
    }
    //console.log(listaSeries[pos].capitulos[temporada][posCap].temporada);
    let salida='<select class="form-select" aria-label="Default select example" id="temporadaCapitulo" name="temporadaCapitulo"> <option value="'+listaSeries[pos].capitulos[temporada][posCap].temporada+'">'+listaSeries[pos].capitulos[temporada][posCap].temporada+'</option>';
    for(i=1; i<=listaSeries[pos].temporadas; i++){
        if(i!=listaSeries[pos].capitulos[temporada][posCap].temporada){
            salida+="<option value='"+i+"'>"+i+"</option>";
        }
    }
    salida += "</select>";

    getElement("selectorTemporada").innerHTML = salida;

    getElement("tituloCapitulo").value = listaSeries[pos].capitulos[temporada][posCap].titulo;
    getElement("numeroCapitulo").value = listaSeries[pos].capitulos[temporada][posCap].numeroCapitulo;
    getElement("duracionCapitulo").value = listaSeries[pos].capitulos[temporada][posCap].duracion;
    getElement("estrenoCapitulo").value = listaSeries[pos].capitulos[temporada][posCap].estreno;
    getElement("sinopsisCapitulo").value = listaSeries[pos].capitulos[temporada][posCap].sinopsis;
    getElement("imagenCapitulo").value = listaSeries[pos].capitulos[temporada][posCap].imagen;
    getElement("capituloCapitulo").value = listaSeries[pos].capitulos[temporada][posCap].capitulo;

    getElement("guardarCapitulos").style.display = 'none';
    getElement("limpiarCapitulos").style.display = 'none';
    getElement("listarCapitulos").style.display = 'none';
    getElement("regresarCapitulos").style.display = 'none';
    
    getElement("modificarCapitulos").style.display = 'inline';
    getElement("cancelarCapitulos").style.display = 'inline';

    getElement("pos").value=pos;
    getElement("temp").value=temporada;
    getElement("cap").value=posCap;

    getElement("tablaCapitulos").innerHTML = "";
}

function updateCapitulo(){
    pos = getElement("pos").value;
    temp = getElement("temp").value;
    cap = getElement("cap").value;
    //console.log(pos);
    listaSeries = [];
    let nuevo = JSON.parse(localStorage.getItem("series"));
    for (const key in nuevo) {
        listaSeries[key] = nuevo[key];
    }

    if (listaSeries[pos].capitulos[temp][cap].temporada!=getDato("temporadaCapitulo")) {
        listaSeries[pos].capitulos[temp][cap].temporada = getDato("temporadaCapitulo");
        listaSeries[pos].capitulos[temp][cap].numeroCapitulo = getDato("numeroCapitulo");
        listaSeries[pos].capitulos[temp][cap].titulo = getDato("tituloCapitulo");
        listaSeries[pos].capitulos[temp][cap].duracion = getDato("duracionCapitulo");
        listaSeries[pos].capitulos[temp][cap].estreno = getDato("estrenoCapitulo");
        listaSeries[pos].capitulos[temp][cap].sinopsis = getDato("sinopsisCapitulo");
        listaSeries[pos].capitulos[temp][cap].imagen = getDato("imagenCapitulo");
        listaSeries[pos].capitulos[temp][cap].capitulo = getDato("capituloCapitulo");
        capitulo=listaSeries[pos].capitulos[temp][cap];
        listaSeries[pos].capitulos[getDato("temporadaCapitulo")-1].push(capitulo);
        listaSeries[pos].capitulos[temp].splice(cap,1);
    }else{
        listaSeries[pos].capitulos[temp][cap].numeroCapitulo = getDato("numeroCapitulo");
        listaSeries[pos].capitulos[temp][cap].titulo = getDato("tituloCapitulo");
        listaSeries[pos].capitulos[temp][cap].duracion = getDato("duracionCapitulo");
        listaSeries[pos].capitulos[temp][cap].estreno = getDato("estrenoCapitulo");
        listaSeries[pos].capitulos[temp][cap].sinopsis = getDato("sinopsisCapitulo");
        listaSeries[pos].capitulos[temp][cap].imagen = getDato("imagenCapitulo");
        listaSeries[pos].capitulos[temp][cap].capitulo = getDato("capituloCapitulo");
    }
    localStorage.setItem("series", JSON.stringify(listaSeries));
    alert("Capitulo modificado correctamente");
    cancelarCapitulo();
}

function cancelarCapitulo(){
    limpiarCapitulo();
    getElement("guardarCapitulos").style.display = 'inline';
    getElement("limpiarCapitulos").style.display = 'inline';
    getElement("listarCapitulos").style.display = 'inline';
    getElement("regresarCapitulos").style.display = 'inline';
    
    getElement("modificarCapitulos").style.display = 'none';
    getElement("cancelarCapitulos").style.display = 'none';

    getElement("temp").value="";
    getElement("cap").value="";

    mostrarCapitulos();
}