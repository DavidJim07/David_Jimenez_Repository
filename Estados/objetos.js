let arrayestados = [];
let lista=[];
let frame = getElemen("panel");

class Estado {
  _clave;
  _nombre;
  _capital;
  _habitantes;
  _imagen;
  _respuesta;
  _pueblitos = [];

  constructor(clave, nombre, capital, habitantes, imagen, pueblitos, respuesta) {
    this._clave = clave;
    this._nombre = nombre;
    this._capital = capital;
    this._habitantes = habitantes;
    this._imagen = imagen;
    this._respuesta = respuesta
    this._pueblitos = pueblitos;
  }

  get clave() {
    return this._clave;
  }
  set clave(clave) {
    this._clave = clave;
  }

  get nombre() {
    return this._nombre;
  }
  set nombre(nombre) {
    this._nombre = nombre;
  }

  get capital() {
    return this._capital;
  }
  set capital(capital) {
    this._capital = capital;
  }
  get habitantes(){
    return this._habitantes;
  }
  set habitantes(habitantes){
    this._habitantes=habitantes;
  }
  get respuesta(){
    return this._respuesta;
  }
  get imagen() {
    return this._imagen;
  }
  set imagen(imagen) {
    this._imagen = imagen;
  }
  get pueblitos(){
    return this._pueblitos;
  }
  set pueblitos(pueblo){
    this._pueblitos = pueblo;
  }
  agregarpueblo(nombre, fecha) {
    this._pueblitos.push(nombre, fecha);
  }
  get pueblo() {
    return this._pueblitos;
  }
}
function registrarestado() {
  //let salida = '<iframe src="estados.html"></iframe>';
  let salida="";
  salida='<form id="formestado">';
  salida+='<h1>Resgitrar estado</h1>';
  salida+='<input type="text" name="clave" id="clave" placeholder="Ingresa la clave del estado"><br/><br/>';
  salida+='<input type="text" name="nombre" id="nombre" placeholder="Ingresa el nombre del estado"><br/><br/>';
  salida+='<input type="text" name="capital" id="capital" placeholder="Ingresa la capital del estado"><br/><br/>';
  salida+='<input type="number" name="habitantes" id="habitantes" placeholder="Ingresa el numero de habitantes"><br/><br/>';
  salida+='<input type="text" name="imagen" id="imagen" placeholder="Ingresa la url de la imagen"><br/><br/>';
  salida+='<pre>';
  salida+='<button type="reset" name="btcancelar" id="btcancelar">Cancelar</button> <button type="submit" name="btregistrar" id="btregistrar" onclick="agregar()">Registrar</button>';
  salida+='</pre>';
  salida+='</form>';
  salida+='<button type="submit"  onclick="listar()">Cancelar</button>';
  salida+='<br>';
  salida+='<center><h1>Estados</h1></center>';
  salida+='<table id="tablaestado" class="tablaestado">';
  salida+='<thead>';
  salida+='<tr>';
  salida+='<th>Clave</th>';
  salida+='<th>Nombre del estado</th>';
  salida+='<th>Capital</th>';
  salida+='<th>Numero de Habitantes</th>';
  salida+='<th id="imagen">imagen</th>';
  salida+='<th>Previsualizar</th>';
  salida+='</tr>';
  salida+='</thead>';
  salida+='<tbody id="tablacuerpo">';
  salida+='</tbody>';
  salida+='</table>';
  frame.innerHTML="";
  frame.innerHTML=salida;

  
}

function inicio(){
  arrayestados=[];
  arrayestados.push(JSON.parse(localStorage.getItem(2)));
  let clave = getDato("clave");
  let nombre = getDato("nombre");
  let capital = getDato("capital");
  let habitantes = getDato("habitantes");
  let imagen = getDato("imagen");


  for (let estado of arrayestados) {
    clave.innerHTML=estado.clave;
    nombre.innerHTML=estado.nombre;
    capital.innerHTML
    salida+= "<tr><td>"+estado.clave + "</td><td>" + estado.nombre + "</td><td>" + estado.capital + "</td><td>" + estado.habitantes + "</td><td>" + estado.imagen + "</td></tr>";       
  }
  let tabla=getElemen("tablacuerpo");
  tabla.innerHTML=salida;
}

function getDato(campo) {
  return document.getElementById(campo).value;
}
function getElemen(campo){
  return document.getElementById(campo);
}

function agregar() {
  let id=localStorage.length;
  let clave = getDato("clave");
  let nombre = getDato("nombre");
  let capital = getDato("capital");
  let habitantes = getDato("habitantes");
  const alphabet = "abcd"
  const randomCharacter = alphabet[Math.floor(Math.random() * alphabet.length)];
  let imagen = getDato("imagen");
  let pueblitos=[];
  let d1=new Estado(clave,nombre,capital,habitantes,imagen, pueblitos);
  let estado = new Object();
  estado["clave"] = clave;
  estado["nombre"] = nombre;
  estado["capital"] = capital;
  estado["habitantes"] = habitantes;
  estado["respuesta"] = randomCharacter;
  estado["imagen"] = imagen;
  estado["pueblitos"]=pueblitos;
  id=id+1;
  localStorage.setItem(id, JSON.stringify(estado));
}


function listar() {
  arrayestados=[];
   //Asignamos los datos del localstoreg a un vector en forma de cadena
   for (let id = 1; id <= localStorage.length; id++) {
    arrayestados.push(JSON.parse(localStorage.getItem(id)));
  }
  let salida = "";
  let CveEst = 1;
  for (let estado of arrayestados) {
          salida+= "<tr><td>"+estado.clave + "</td><td>" + estado.nombre + "</td><td>" + estado.capital + "</td><td>" + estado.habitantes + "</td><td>" + estado.imagen + "</td></tr>";
          CveEst++;
  }
  let tabla=getElemen("tablacuerpo");
  tabla.innerHTML=salida;
  
}
