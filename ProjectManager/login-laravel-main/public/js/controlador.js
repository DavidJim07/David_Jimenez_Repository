function buscarUsuario(){
    //alert("bucarUsuario");
    var request = new XMLHttpRequest();
    var formData=new FormData(document.querySelector('#form-filtro'));
    request.open("POST", "/usuario/filtro", true);
    request.onreadystatechange=function(){
        if(this.readyState==4){
            if(this.status==200){
                if(this.responseText!=null){
                    //alert(this.responseText);
                    document.getElementById('contenidoTabla').innerHTML=this.responseText;
                }else alert("Comunication Error: No data received");
            }else alert("Comunication Error: "+this.statusText);
        }
    }

    request.send(formData);
}

function buscarActividad(){
    //alert("buscarActividad");
    var request = new XMLHttpRequest();
    var formData=new FormData(document.querySelector('#form-filtro'));
    request.open("POST", "/actividad/filtro", true);

    request.onreadystatechange=function(){
        if(this.readyState==4){
            if(this.status==200){
                if(this.responseText!=null){
                    //alert(this.responseText);
                    document.getElementById('contenidoTabla').innerHTML=this.responseText;
                }else alert("Comunication Error: No data received");
            }else alert("Comunication Error: "+this.statusText);
        }
    }

    request.send(formData);
}

function buscarProyecto(){
    //alert("buscarProyecto");
    var request = new XMLHttpRequest();
    var formData=new FormData(document.querySelector('#form-filtro'));
    request.open("POST", "/proyecto/filtro", true);

    request.onreadystatechange=function(){
        if(this.readyState==4){
            if(this.status==200){
                if(this.responseText!=null){
                    //alert(this.responseText);
                    document.getElementById('contenidoTabla').innerHTML=this.responseText;
                }else alert("Comunication Error: No data received");
            }else alert("Comunication Error: "+this.statusText);
        }
    }

    request.send(formData);
}