<div>
    @auth
    @if(Auth::User()->hasRole('administrador'))
    <table class="table">
    <thead>
        <tr>
        <th scope="col">#</th>
        <th scope="col">Nombre</th>
        <th scope="col">Acciones</th>
        </tr>
    </thead>
    <tbody>
        @foreach($proyectos as $r)
        <tr>
            <th scope="row"  style="background-color:green">{{$loop->iteration}}</th>
            <td>{{$r->nombre}}</td>
            <td>
                <a href="/proyecto/{{$r->id}}" class="btn btn-primary btn-sm">Consultar</a>
                <a href="/proyecto/{{$r->id}}/edit" class="btn btn-secondary btn-sm">Modificar</a>
                <a href="/relacion/{{$r->id}}" class="btn btn-warning btn-sm">Actividades</a>
                <!-- Button trigger modal -->
                <button type="button" class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#modal-{{$r->id}}">
                Finalizar Proyecto
                </button>
                <!-- Modal -->
                <div class="modal fade" id="modal-{{$r->id}}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Eliminar</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form action="/proyecto/{{$r->id}}" method="post" id="form-eliminar-{{$r->id}}">
                            @method('DELETE')
                            @csrf
                            ¿Estas seguro de borrar a: {{$r->id}}? 
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="submit" class="btn btn-danger" form="form-eliminar-{{$r->id}}">Finalizar Tarea</button>
                    </div>
                    </div>
                </div>
                </div>

            </td>
            </tr>
            
        @endforeach
        @if(count($proyectos2)!=0)
            <tr>
                <td></td>
                <td>Terminados</td>
            </tr>
            @foreach($proyectos2 as $r)
            <tr>
                <th scope="row" style="background-color:red">{{$loop->iteration}}</th>
                <td>{{$r->nombre}}</td>
                <td>
                    <a href="/proyecto/{{$r->id}}" class="btn btn-primary btn-sm">Consultar</a>
                    <a href="/relacion/{{$r->id}}" class="btn btn-warning btn-sm">Actividades</a>
                </td>
            </tr>
            @endforeach
        @endif
    </tbody>
    </table>
    @endif
    @endauth
</div>