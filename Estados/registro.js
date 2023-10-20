let arrayestados = [];
let lista = [];
let arraypueblos=[];
let clasemodificar="";
let frame = getElement("panel");
let caracteres = "abcd";

class Estado {
  _clave;
  _nombre;
  _capital;
  _habitantes;
  _imagen;
  _pueblitos = [];
  _respuesta;

  constructor(clave, nombre, capital, habitantes, imagen, pueblitos,respuesta) {
    this._clave = clave;
    this._nombre = nombre;
    this._capital = capital;
    this._habitantes = habitantes;
    this._imagen = imagen;
    this._pueblitos = pueblitos;
    this._respuesta=respuesta;
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
    this._pueblitos.push({"nombre":nombre,"fecha":fecha});
  }
 
  get respuesta(){
    return this._respuesta;
  }
}

function inicio(){
    
}

function agregar() {
  let id = localStorage.length;
  let clave = getDato("clave");
  let nombre = getDato("nombre");
  let capital = getDato("capital");
  let habitantes = getDato("habitantes");
  let imagen = getDato("imagen");
  let pueblitos = [];
  let respuesta = caracteres[Math.floor(Math.random() * caracteres.length)];
  let d1 = new Estado(clave, nombre, capital, habitantes, imagen, pueblitos, respuesta);
  let objetos=objeto(d1);
  id++;
  localStorage.setItem(id, JSON.stringify(objetos));
  listar();
  limpiar();
}

function listar() {
  arrayestados=[];
  getElement("tablacuerpo").innerHTML ="";
  for (let id = 1; id <= localStorage.length; id++) {
    arrayestados.push(JSON.parse(localStorage.getItem(id)));
  }
  let salida = "";
  let nitem = 1; 
  for (let estado of arrayestados) {
    if(estado!=null){
      salida +="<tr><td>"+estado.clave+"</td><td>"+estado.nombre+"</td><td>"+estado.capital+"</td><td>"+estado.habitantes+"</td><td><img src="+estado.imagen+" width=100 height=100></td>"+
        "<td><button type='submit' id='vistap' onclick='previsualizar("+nitem+")'>Previsualizar</button> <button type='submit' id='eliminar' onclick='eliminar("+nitem+")'>Eliminar</button></td></tr>";
      nitem++;
    }
  }
  getElement("tablacuerpo").innerHTML = salida;
}

function modificar(id) {
  clasemodificar.clave = getDato("lbclave");
  clasemodificar.nombre = getDato("lbnombre");
  clasemodificar.capital = getDato("lbcapital");
  clasemodificar.habitantes = getDato("lbhabitantes");
  clasemodificar.imagen = getDato("lburl");
  clasemodificar.pueblitos =arraypueblos;
  let objetos=objeto(clasemodificar);
  localStorage.setItem(id, JSON.stringify(objetos));
  previsualizar(id);
}

function eliminar(item){
  let tabla = getElement("tablacuerpo");
  tabla.innerHTML = "";
  localStorage.removeItem(item);
  listar();
}

function previsualizar(item) {
  arrayestados = [];
  clasemodificar="";
  arraypueblos=[];
  arrayestados.push(JSON.parse(localStorage.getItem(item)));
  formulariovista(item);
  for (let estado of arrayestados) {
    getElement("lbclave").value = estado.clave;
    getElement("lbnombre").value = estado.nombre;
    getElement("lbcapital").value = estado.capital;
    getElement("lbhabitantes").value = estado.habitantes;
    getElement("lburl").value = estado.imagen;
    getElement("lbimagen").innerHTML ="<img src=" + estado.imagen + " width=100 height=100></td>";
    arraypueblos= estado.pueblitos;
    clasemodificar=new Estado(estado.clave, estado.nombre, estado.capital, estado.habitantes, estado.imagen, estado.pueblitos, estado.respuesta);
    listarpueblos(item);
  }
}

function registrarpueblito(item){
  clasemodificar.agregarpueblo(getDato('pueblo'),getDato('fecha'));
  let objetos=objeto(clasemodificar);
  localStorage.setItem(item, JSON.stringify(objetos));
  listarpueblos();
}

function listarpueblos(item){
  let salida="";
  let nitem=0;
  for (let p of arraypueblos) {
    salida +="<tr><td>"+p.nombre+"</td>"+
    "<td>"+p.fecha+"</td>"+
    "<td><button type='submit' onclick='eliminarpueblito("+nitem+","+item+")'>Eliminar</button></td></tr>";
    nitem++;
  }
  getElement("tablapueblitoscuerpo").innerHTML=salida;
}

function eliminarpueblito(pos,item){
  arraypueblos.splice(pos, 1);
  clasemodificar.pueblitos = arraypueblos;
  let objetos=objeto(clasemodificar);
  localStorage.setItem(item, JSON.stringify(objetos));
  previsualizar(item);
}

function limpiarr(){
  getElement("pueblo").value="";
  getElement("fecha").value="";
}
function limpiar(){
  getElement("clave").value="";
  getElement("nombre").value="";
  getElement("capital").value="";
  getElement("habitantes").value="";
  getElement("imagen").value="";
}

function activar(item) {
  getElement("lbclave").readOnly = false;
    getElement("lbnombre").readOnly = false;
    getElement("lbcapital").readOnly = false;
    getElement("lbhabitantes").readOnly = false;
    getElement("lburl").readOnly = false;
  let elementos="";
  elementos+="<button type='submit' id='nuevo' onclick='modificar("+item+")'>Modificar</button>";
  getElement("mod").style.display='none';
  getElement("divmodificar").innerHTML=elementos;
  
}

function objeto(l1){
  let estado = new Object();
  estado["clave"] = l1.clave;
  estado["nombre"] = l1.nombre;
  estado["capital"] = l1.capital;
  estado["habitantes"] = l1.habitantes;
  estado["imagen"] = l1.imagen;
  estado["pueblitos"] = l1.pueblitos;
  estado["respuesta"]=l1.respuesta;
  return estado;
}

function getDato(campo) {
  return document.getElementById(campo).value;
}

function getElement(campo) {
  return document.getElementById(campo);
}

function formularioestados() {
  let salida = "";
  salida = "<center>";
  salida += "<h1>Resgitrar estado</h1>";
  salida +='<input type="text" name="clave" id="clave" placeholder="Ingresa la clave del estado"><br/><br/>';
  salida +='<input type="text" name="nombre" id="nombre" placeholder="Ingresa el nombre del estado"><br/><br/>';
  salida +='<input type="text" name="capital" id="capital" placeholder="Ingresa la capital del estado"><br/><br/>';
  salida +='<input type="number" name="habitantes" id="habitantes" placeholder="Ingresa el numero de habitantes"><br/><br/>';
  salida +='<input type="text" name="imagen" id="imagen" placeholder="Ingresa la url de la imagen"><br/><br/>';
  salida +="<pre>";
  salida +='<button type="submit" name="btcancelar" id="btcancelar" onclick="limpiar()">Cancelar</button> <button type="submit" name="btregistrar" id="btregistrar" onclick="agregar()">Registrar</button>';
  salida +="</pre>";
  salida +="</center>";
  salida +="<br>";
  salida +="<center><h1>Estados</h1></center>";
  salida +='<table id="tablaestado" class="tablaestado" border=1>';
  salida +="<thead>";
  salida +="<tr>";
  salida +="<th>Clave</th>";
  salida +="<th>Nombre del estado</th>";
  salida +="<th>Capital</th>";
  salida +="<th>Numero de Habitantes</th>";
  salida +='<th id="imagen">imagen</th>';
  salida +="<th>Previsualizar</th>";
  salida +="</tr>";
  salida +="</thead>";
  salida +='<tbody id="tablacuerpo">';
  salida +="</tbody>";
  salida +="</table>";
  frame.innerHTML = "";
  frame.innerHTML = salida;
  listar();
}

function formulariovista(item){
  let salida="";
  frame.innerHTML="";
  salida+='<div id="consulta">';
  salida+='<center>';
  salida+='<h1>DATOS DEL ESTADO</h1><br> ';
  salida+='CLAVE:<input type="text" id="lbclave" readonly><br/>';
  salida+='NOMBRE DEL ESTADO: <input type="text" id="lbnombre" readonly><br/>';
  salida+='CAPITAL: <input type="text" id="lbcapital" readonly ><br/>';
  salida+='NUMERO DE HABITANTES: <input type="text" id="lbhabitantes" readonly><br/>';
  salida+='URL IMAGEN<input type="text" id="lburl" readonly><br/>';
  salida+='IMAGEN DEL ESTADO:';
  salida+='<br><br><label id="lbimagen"></label><br/><br/>';
  salida+='<button type="submit" id="mod" onclick="activar('+item+')" >Modificar Estado</button>';
  salida+='</center>';
  salida+='<center><div id="divmodificar"></div></center>';
  salida+='</div>';
  salida+='<div id="contenidopueblos">';
  salida+='<div id="tablapueblos">';
  salida+='<center>';
  salida+='<h1>PUEBLITOS DEL ESTADO</h1>';
  salida+='<table id="tablapueblitos" class="tablapueblitos" border=1>';
  salida+='<thead>';
  salida+='<tr>';
  salida+='<th>Pueblo magico</th>';
  salida+='<th>Dia festivo</th>';
  salida+='<th>Acciones</th>';
  salida+='</tr>';
  salida+='</thead>';
  salida+='<tbody id="tablapueblitoscuerpo">';
  salida+='</tbody>';
  salida+='</table>';
  salida+='</center>';
  salida+='</div>';
  salida+='<div id="registrarpueblos">';
  salida+='<center>';
  salida+='<h1>REGISTRAR PUEBLITO</h1><br>';
  salida+='<input type="text" name="pueblo" id="pueblo" placeholder="Nombre del pueblo magico"><br/><br/>';
  salida+='<input type="text" name="fecha" id="fecha" placeholder="Dia festivo"><br/>';
  salida +="<pre>";
  salida+='<button type="submit" id="cancelar" onclick="limpiarr()" >Cancelar</button>';
  salida+='   <button type="submit" id="registrarpueblo" onclick="registrarpueblito('+item+')">Registrar</button>';
  salida +="</pre>";
  salida+='</center>';
  salida+='</div>';
  salida+='</div>';
  frame.innerHTML = salida;
}

