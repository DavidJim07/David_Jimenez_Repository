<form action="javascript:buscarProyecto();" method="post" id="form-filtro">
    @csrf
    <div class="row">
        <div class="col-md-3"></div>
        <div class="col-md-3">
                <a  class="btn btn-primary btn-sm" href="proyecto/create">Registrar Proyecto</a>
        </div> 
        <div class="col-md-3">
            <input type="text" name="nombre" id="nombre" class="form-control" placeholder="Buscar por nombre">
        </div>
        <div class="col-md-3">
            <input type="submit" name="btn-filtro" id="btn-filtro" class="btn btn-info btn-block" value="Enviar">
        </div>
        <div class="col-md-3"></div>
    </div>
</form>