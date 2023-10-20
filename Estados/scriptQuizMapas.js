var prueba = listar();
var quiz = document.querySelector(".quizHeader");
var answers = document.querySelectorAll(".answer");
var questions = document.getElementById("question");
var imag = document.getElementById("imagen");
var a_text = document.querySelector("#a_pregunta");
var b_text = document.querySelector("#b_pregunta");
var c_text = document.querySelector("#c_pregunta");
var d_text = document.querySelector("#d_pregunta");
var botonAceptar = document.getElementById("submit");
console.log(prueba.length);
let preguntaActual = 0;
let puntuacion = 0;
var preguntasIncorrectas=[];
var respuestaSeleccionada=[];
var respuestaTemporal=[];
cargarPreguntas();
function cargarPreguntas() {
    const res = getRanArr(prueba.length);
    if (preguntaActual < prueba.length) {
        questions.innerHTML = "<img src="+prueba[preguntaActual].imagen+" width=400 height=300> \n¿Cuál es el nombre del estado de la anterior imagen?";
        respuestaTemporal.push("¿Cuál es el nombre del estado de la anterior imagen?");
        switch (prueba[preguntaActual].respuesta) {
            case "a":
                for (let index = 0; index < prueba.length; index++) {
                    if (res[index] == preguntaActual) {
                        res.splice(index, 1);
                    }
                }
                a_text.innerText = prueba[preguntaActual].nombre;
                b_text.innerText = prueba[res[0]].nombre;
                c_text.innerText = prueba[res[1]].nombre;
                d_text.innerText = prueba[res[2]].nombre;
                respuestaTemporal.push(prueba[preguntaActual].nombre,prueba[res[0]].nombre,prueba[res[1]].nombre,prueba[res[2]].nombre);
                respuestaTemporal.push(prueba[preguntaActual].imagen);
            break;
            case "b":
                for (let index = 0; index < prueba.length; index++) {
                    if (res[index] == preguntaActual) {
                        res.splice(index, 1);
                    }
                }
                a_text.innerText = prueba[res[0]].nombre;
                b_text.innerText = prueba[preguntaActual].nombre;
                c_text.innerText = prueba[res[1]].nombre;
                d_text.innerText = prueba[res[2]].nombre;
                respuestaTemporal.push(prueba[preguntaActual].nombre,prueba[res[0]].nombre,prueba[res[1]].nombre,prueba[res[2]].nombre);
                respuestaTemporal.push(prueba[preguntaActual].imagen);
            break;
            case "c":
                for (let index = 0; index < prueba.length; index++) {
                    if (res[index] == preguntaActual) {
                        res.splice(index, 1);
                    }
                }
                a_text.innerText = prueba[res[0]].nombre;
                b_text.innerText = prueba[res[1]].nombre;
                c_text.innerText = prueba[preguntaActual].nombre;
                d_text.innerText = prueba[res[2]].nombre;
                respuestaTemporal.push(prueba[preguntaActual].nombre,prueba[res[0]].nombre,prueba[res[1]].nombre,prueba[res[2]].nombre);
                respuestaTemporal.push(prueba[preguntaActual].imagen);
            break;
            case "d":
                for (let index = 0; index < prueba.length; index++) {
                    if (res[index] == preguntaActual) {
                        res.splice(index, 1);
                    }
                }
                a_text.innerText = prueba[res[0]].nombre;
                b_text.innerText = prueba[res[1]].nombre;
                c_text.innerText = prueba[res[2]].nombre;
                d_text.innerText = prueba[preguntaActual].nombre;
                respuestaTemporal.push(prueba[preguntaActual].nombre,prueba[res[0]].nombre,prueba[res[1]].nombre,prueba[res[2]].nombre);
                respuestaTemporal.push(prueba[preguntaActual].imagen);
            break;
            default:
            break;
        } 
    } else {
        let salida = "Cantidad de aciertos:"+puntuacion+" de "+prueba.length;
        for(let index = 0; index < preguntasIncorrectas.length; index++){
            salida+="\n*Error en la pregunta:\n <img src="+respuestaSeleccionada[index][2]+" width=400 height=300>"+"\n"+respuestaSeleccionada[index][0];
            salida+=", la respuesta era: "+preguntasIncorrectas[index]+", usted selecccionó: "+respuestaSeleccionada[index][1]+"\n";
        }
        quiz.innerText=salida;
        botonAceptar.innerText = "Iniciar de nuevo";
    }
}

function desmarcarRespuesta() {
    answers.forEach((e) => {
        e.checked = false;
    });
    cargarPreguntas();
}

function getSelected() {
    answers.forEach((e) => {
        if (e.checked) {
            if (e.id == prueba[preguntaActual].respuesta) {
                puntuacion++;
            }else{
                let temporal=[];
                console.log(respuestaTemporal[5]);
                switch (e.id) {
                    case "a":
                        temporal.push(respuestaTemporal[0],respuestaTemporal[1],respuestaTemporal[5]);
                    break;
                    case "b":
                        temporal.push(respuestaTemporal[0],respuestaTemporal[2],respuestaTemporal[5]);
                    break;
                    case "c":
                        temporal.push(respuestaTemporal[0],respuestaTemporal[3],respuestaTemporal[5]);
                    break;
                    case "d":
                        temporal.push(respuestaTemporal[0],respuestaTemporal[4],respuestaTemporal[5]);
                    break;
                }
                respuestaTemporal=[];
                preguntasIncorrectas.push(prueba[preguntaActual].nombre);
                respuestaSeleccionada.push(temporal);
            }
        }
    });
    preguntaActual++;
    desmarcarRespuesta();
}

botonAceptar.addEventListener("click", () => {
    if (preguntaActual < prueba.length) {
        getSelected();
    }else {
        location.reload();
    }
});

function listar() {
    arrayestados=[];
    for (let id = 1; id <= localStorage.length; id++) {
        arrayestados.push(JSON.parse(localStorage.getItem(id)));
    }
    return arrayestados;
}
  
function getRanArr(lngth) {
    let arr = [];
    do {
        let ran = Math.floor(Math.random() * lngth); 
        arr = arr.indexOf(ran) > -1 ? arr : arr.concat(ran);
     }while (arr.length < lngth)
     
     return arr;
  }
  

