let listaPeliculas = [];

function getDato(campo) {
  return document.getElementById(campo).value;
}
function getElement(campo) {
  return document.getElementById(campo);
}

class Pelicula {
  _titulo;
  _duracion;
  _categorias;
  _estreno;
  _sinopsis;
  _imagen;
  _pelicula;

  constructor(
    titulo,
    duracion,
    categorias,
    estreno,
    sinopsis,
    imagen,
    pelicula
  ) {
    this._titulo = titulo;
    this._duracion = duracion;
    this._categorias = categorias;
    this._estreno = estreno;
    this._sinopsis = sinopsis;
    this._imagen = imagen;
    this._pelicula = pelicula;
  }

  get titulo() {
    return this._titulo;
  }

  set titulo(titulo) {
    this._titulo = titulo;
  }

  get duracion() {
    return this._duracion;
  }

  set duracion(duracion) {
    this._duracion = duracion;
  }

  set categorias(categorias) {
    this._categorias = categorias;
  }

  get categorias() {
    return this._categorias;
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

  get pelicula() {
    return this._pelicula;
  }

  set pelicula(pelicula) {
    this._pelicula = pelicula;
  }
}

function objetoPelicula(o) {
  let pelicula = new Object();
  pelicula["titulo"] = o.titulo;
  pelicula["duracion"] = o.duracion;
  pelicula["categorias"] = o.categorias;
  pelicula["estreno"] = o.estreno;
  pelicula["sinopsis"] = o.sinopsis;
  pelicula["imagen"] = o.imagen;
  pelicula["pelicula"] = o.pelicula;
  return pelicula;
}

function agregarPelicula() {
  if (localStorage.getItem("peliculas") == null) {
    let titulo = getDato("titulo");
    let duracion = getDato("duracion");
    let categorias = getSelectores();
    let estreno = getDato("estreno");
    let sinopsis = getDato("sinopsis");
    let imagen = getDato("imagen");
    let pelicula = getDato("pelicula");

    let p = new Pelicula(titulo, duracion, categorias, estreno, sinopsis,  imagen,  pelicula);
    listaPeliculas.push(objetoPelicula(p));
    localStorage.setItem("peliculas", JSON.stringify(listaPeliculas));
    alert("Pelicula agregada correctamente");
    limpiarPeliculas();
    mostrarPeliculas();
  } else {
    listaPeliculas = [];
    let nuevo = JSON.parse(localStorage.getItem("peliculas"));
    for (const key in nuevo) {
      listaPeliculas[key] = nuevo[key];
    }
    let titulo = getDato("titulo");
    let duracion = getDato("duracion");
    let categorias = getSelectores();
    let estreno = getDato("estreno");
    let sinopsis = getDato("sinopsis");
    let imagen = getDato("imagen");
    let pelicula = getDato("pelicula");

    let p = new Pelicula(titulo, duracion, categorias, estreno, sinopsis,  imagen,  pelicula);
    listaPeliculas.push(objetoPelicula(p));
    localStorage.setItem("peliculas", JSON.stringify(listaPeliculas));
    alert("Pelicula agregada correctamente");
    limpiarPeliculas();
    mostrarPeliculas();
  }
}

function mostrarPeliculas() {
  let salida = "<table class='table table-hover'> <thead><tr class='table-secondary'><th scope='col'>#</th><th scope='col'>Titulo</th> <th scope='col'>Duración</th> <th scope='col'>Categorias</th> <th scope='col'>Estreno</th> <th scope='col'>Sinopsis</th> <th scope='col'>Imagen</th> <th scope='col'>Pelicula</th> <th scope='col'>Acciones</th> </tr></thead><tbody>";
  let pos = 0;
  let nuevo = JSON.parse(localStorage.getItem("peliculas"));
  if (nuevo) {
    for (const n of nuevo) {
      salida += `<tr class="table-light">
      <td>${pos+1}</td>
      <td>${n.titulo}</td>
      <td>${n.duracion}</td>
      <td>${mostrarCategorias(n.categorias)}</td>
      <td>${n.estreno}</td>
      <td>${n.sinopsis}</td>
      <td>${n.imagen}</td>
      <td>${n.pelicula}</td>
      <td> <button class="btn btn-danger" onclick='eliminarPelicula(${pos})'>Eliminar</button>
          <button class="btn btn-warning" onclick='modificarPelicula(${pos})'>Modificar</button> </td>
      </tr>`;
      pos++;
    }
    salida+="</tbody></table>"
    getElement("tablaPeliculas").innerHTML = salida;
  } 
}

function limpiarPeliculas() {
  getElement("titulo").value = "";
  getElement("duracion").value = "";
  getElement("estreno").value = "";
  getElement("sinopsis").value = "";
  getElement("imagen").value = "";
  getElement("pelicula").value = "";
  resetSelectores();
}

function eliminarPelicula(pos) {
    console.log(pos);
    listaPeliculas = [];
    let nuevo = JSON.parse(localStorage.getItem("peliculas"));
    for (const key in nuevo) {
      listaPeliculas[key] = nuevo[key];
    }
    listaPeliculas.splice(pos, 1);
    localStorage.setItem("peliculas", JSON.stringify(listaPeliculas));
    alert("Pelicula eliminada carrectamente");
    mostrarPeliculas();
}

function modificarPelicula(pos) {
    //console.log(pos);
    listaPeliculas = [];
    let nuevo = JSON.parse(localStorage.getItem("peliculas"));
    for (const key in nuevo) {
      listaPeliculas[key] = nuevo[key];
    }
    //console.log(listaPeliculas[pos]);
    getElement("titulo").value = listaPeliculas[pos].titulo;
    getElement("duracion").value = listaPeliculas[pos].duracion;
    marcarSeleccionados(listaPeliculas[pos].categorias);
    getElement("estreno").value = listaPeliculas[pos].estreno;
    getElement("sinopsis").value = listaPeliculas[pos].sinopsis;
    getElement("imagen").value = listaPeliculas[pos].imagen;
    getElement("pelicula").value = listaPeliculas[pos].pelicula;

    getElement("guardar").style.display = 'none';
    getElement("limpiar").style.display = 'none';
    getElement("listar").style.display = 'none';
    
    getElement("modificar").style.display = 'inline';
    getElement("cancelar").style.display = 'inline';

    getElement("pos").value=pos;

    getElement("tablaPeliculas").innerHTML = "";
}

function updatePelicula(){
    pos = getElement("pos").value;
    //console.log(pos);
    listaPeliculas = [];
    let nuevo = JSON.parse(localStorage.getItem("peliculas"));
    for (const key in nuevo) {
      listaPeliculas[key] = nuevo[key];
    }
    listaPeliculas[pos].titulo=getDato("titulo");
    listaPeliculas[pos].duracion = getDato("duracion");
    listaPeliculas[pos].categorias = getSelectores();
    listaPeliculas[pos].estreno = getDato("estreno");
    listaPeliculas[pos].sinopsis = getDato("sinopsis");
    listaPeliculas[pos].imagen = getDato("imagen");
    listaPeliculas[pos].pelicula = getDato("pelicula");
    localStorage.setItem("peliculas", JSON.stringify(listaPeliculas));
    alert("Pelicula modificada carrectamente");
    cancelarPelicula();
}

function cancelarPelicula(){
    limpiarPeliculas();
    getElement("guardar").style.display = 'inline';
    getElement("limpiar").style.display = 'inline';
    getElement("listar").style.display = 'inline';
    
    getElement("modificar").style.display = 'none';
    getElement("cancelar").style.display = 'none';

    getElement("pos").value="";

    mostrarPeliculas();
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
//-------------------------------------



