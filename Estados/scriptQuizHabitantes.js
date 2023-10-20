var prueba = listar();
var quiz = document.querySelector(".quizHeader");
var answers = document.querySelectorAll(".answer");
var questions = document.getElementById("question");
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
    if (preguntaActual < prueba.length) {
        const res = getRanArr(prueba.length);
        let pregunta= "¿Cuántos habitantes tiene "+prueba[preguntaActual].nombre+"?";
        questions.innerText = pregunta;
        console.log(pregunta);
        respuestaTemporal.push("¿Cuántos habitantes tiene "+prueba[preguntaActual].nombre+"?");
        switch (prueba[preguntaActual].respuesta) {
            case "a":
                for (let index = 0; index < prueba.length; index++) {
                    if (res[index] == preguntaActual) {
                        res.splice(index, 1);
                    }
                }
                a_text.innerText = prueba[preguntaActual].habitantes;
                b_text.innerText = prueba[res[0]].habitantes;
                c_text.innerText = prueba[res[1]].habitantes;
                d_text.innerText = prueba[res[2]].habitantes;
                respuestaTemporal.push(prueba[preguntaActual].habitantes,prueba[res[0]].habitantes,prueba[res[1]].habitantes,prueba[res[2]].habitantes);
            break;
            case "b":
                for (let index = 0; index < prueba.length; index++) {
                    if (res[index] == preguntaActual) {
                        res.splice(index, 1);
                    }
                }
                a_text.innerText = prueba[res[0]].habitantes;
                b_text.innerText = prueba[preguntaActual].habitantes;
                c_text.innerText = prueba[res[1]].habitantes;
                d_text.innerText = prueba[res[2]].habitantes;
                respuestaTemporal.push(prueba[res[0]].habitantes,prueba[preguntaActual].habitantes,prueba[res[1]].habitantes,prueba[res[2]].habitantes);
            break;
            case "c":
                for (let index = 0; index < prueba.length; index++) {
                    if (res[index] == preguntaActual) {
                        res.splice(index, 1);
                    }
                }
                a_text.innerText = prueba[res[0]].habitantes;
                b_text.innerText = prueba[res[1]].habitantes;
                c_text.innerText = prueba[preguntaActual].habitantes;
                d_text.innerText = prueba[res[2]].habitantes;
                respuestaTemporal.push(prueba[res[0]].habitantes,prueba[res[1]].habitantes,prueba[preguntaActual].habitantes,prueba[res[2]].habitantes);
            break;
            case "d":
                for (let index = 0; index < prueba.length; index++) {
                    if (res[index] == preguntaActual) {
                        res.splice(index, 1);
                    }
                }
                a_text.innerText = prueba[res[0]].habitantes;
                b_text.innerText = prueba[res[1]].habitantes;
                c_text.innerText = prueba[res[2]].habitantes;
                d_text.innerText = prueba[preguntaActual].habitantes;
                respuestaTemporal.push(prueba[res[0]].habitantes,prueba[res[1]].habitantes,prueba[res[2]].habitantes,prueba[preguntaActual].habitantes);
            break;
            default:
            break;
        }  
    } else {
        let salida = "Cantidad de aciertos:"+ puntuacion+" de "+prueba.length;
        for(let index = 0; index < preguntasIncorrectas.length; index++){
            salida+="\n*Error en la pregunta: "+respuestaSeleccionada[index][0];
            salida+=", la respuesta era: "+preguntasIncorrectas[index]+", usted selecccionó: "+respuestaSeleccionada[index][1]+"\n";
        }
        quiz.innerText = salida;
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
                switch (e.id) {
                    case "a":
                        temporal.push(respuestaTemporal[0],respuestaTemporal[1]);
                    break;
                    case "b":
                        temporal.push(respuestaTemporal[0],respuestaTemporal[2]);
                    break;
                    case "c":
                        temporal.push(respuestaTemporal[0],respuestaTemporal[3]);
                    break;
                    case "d":
                        temporal.push(respuestaTemporal[0],respuestaTemporal[4]);
                    break;
                }
                respuestaTemporal=[];
                preguntasIncorrectas.push(prueba[preguntaActual].habitantes);
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
  

