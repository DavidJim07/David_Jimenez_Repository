
document.addEventListener('DOMContentLoaded', () => {
    let prueba = [];
    let nuevo = JSON.parse(localStorage.getItem("series"));
    for (const key in nuevo) {
        prueba[key] = nuevo[key];
    }
    let DOMitems = document.querySelector('#items');

    function actualizarVista() {
        let cont=0
        prueba.forEach((producto) => {
            let contenedor = document.createElement('div');
            contenedor.style.marginLeft = "13px";
            contenedor.style.marginTop = "13px";
            contenedor.classList.add('card', 'col-sm-2');

            let cuerpo = document.createElement('div');
            cuerpo.classList.add('card-body');

            let titulo = document.createElement('h5');
            titulo.classList.add('card-title');
            titulo.textContent = producto.titulo;
            
            let video = document.createElement('img');
            video.classList.add('embed-responsive-item');
            video.setAttribute('src', producto.imagen);
            video.setAttribute('width', "125");
            video.setAttribute('height', "175");
            video.setAttribute('frameborder', "0");

            let br = document.createElement("br");
            let br2 = document.createElement("br");

            let ver = document.createElement("button");
            ver.classList.add("btn", "btn-success");
            ver.textContent = "Ver";
            ver.setAttribute("id", cont);
            ver.addEventListener("click", visualizar);

            cuerpo.appendChild(titulo);
            cuerpo.appendChild(video);
            cuerpo.appendChild(br);
            cuerpo.appendChild(br2);
            cuerpo.appendChild(ver);
            contenedor.appendChild(cuerpo);
            DOMitems.appendChild(contenedor);
            cont++;
        });


    }
    actualizarVista();
    });

    function searchBar() {
        var titleName = document.getElementById("search").value;
        let prueba = [];
        let salida = [];
        let nuevo = JSON.parse(localStorage.getItem("series"));
        for (const key in nuevo) {
            prueba[key] = nuevo[key];
        }

        for (let index = 0; index < prueba.length; index++) {
            if (!prueba[index].titulo.toUpperCase().indexOf(titleName.toUpperCase())) {
                salida[index] = prueba[index];
            }
        }
        document.getElementById("items").innerHTML = "";
        let DOMitems = document.querySelector('#items');
        let cont=0;
        salida.forEach((producto) => {
            let contenedor = document.createElement('div');
            contenedor.style.marginLeft = "13px";
            contenedor.style.marginTop = "13px";
            contenedor.classList.add('card', 'col-sm-2');

            let cuerpo = document.createElement('div');
            cuerpo.classList.add('card-body');

            let titulo = document.createElement('h5');
            titulo.classList.add('card-title');
            titulo.textContent = producto.titulo;
            
            let video = document.createElement('img');
            video.classList.add('embed-responsive-item');
            video.setAttribute('src', producto.imagen);
            video.setAttribute('width', "125");
            video.setAttribute('height', "175");
            video.setAttribute('frameborder', "0");

            let br = document.createElement("br");
            let br2 = document.createElement("br");

            let ver = document.createElement("button");
            ver.classList.add("btn", "btn-success");
            ver.textContent = "Ver";
            ver.setAttribute("id", cont);
            ver.addEventListener("click", visualizar);

            cuerpo.appendChild(titulo);
            cuerpo.appendChild(video);
            cuerpo.appendChild(br);
            cuerpo.appendChild(br2);
            cuerpo.appendChild(ver);
            contenedor.appendChild(cuerpo);
            DOMitems.appendChild(contenedor);
            cont++;
        });
    }

    function visualizar(Evento){
        localStorage.setItem("identificador", Evento.target.getAttribute("id"));
        window.location.replace("vistaSeriesAdmin.html");
        
    }

