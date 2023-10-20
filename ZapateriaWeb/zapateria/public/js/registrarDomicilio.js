function cargarCarro(event,tipo){
    event.preventDefault();
    if(tipo==0){
        let zapatos=[];
        var iteraciones = document.getElementById("iteraciones").value;
        for(let i=1; i<=iteraciones; i++){
            var zapato = {
                idZapato: document.getElementById("idZapato"+i).value,
                idTalla: document.getElementById("idTalla"+i).value,
                cantidad: document.getElementById("cantidad"+i).value,
            };
            zapatos.push(zapato);
        }
        var myInput = document.getElementById("myInput");
        myInput.value = JSON.stringify(zapatos);
    
        var selectElement = document.getElementById("selectorDomiclio");
        var selectedOption = selectElement.options[selectElement.selectedIndex];
    
        var elemento = document.getElementById("idDomicilio");
        elemento.value=selectedOption.value;

        document.getElementById("formulario2").submit();
    }else if(tipo==1){
        let zapatos=[];
        var iteraciones = document.getElementById("iteraciones").value;
        for(let i=1; i<=iteraciones; i++){
            var zapato = {
                idZapato: document.getElementById("idZapato"+i).value,
                idTalla: document.getElementById("idTalla"+i).value,
                cantidad: document.getElementById("cantidad"+i).value,
            };
            zapatos.push(zapato);
        }
        var myInput = document.getElementById("myInput");
        myInput.value = JSON.stringify(zapatos);
        var myInput2 = document.getElementById("myInput2");
        myInput2.value = JSON.stringify(zapatos);
        console.log(myInput2,JSON.stringify(zapatos));
    
        var selectElement = document.getElementById("selectorDomiclio");
        var selectedOption = selectElement.options[selectElement.selectedIndex];
    
        var elemento2 = document.getElementById("idDomicilio2");
        elemento2.value=selectedOption.value;
        console.log(elemento2);

        document.getElementById("formulario1").submit();
    }
}