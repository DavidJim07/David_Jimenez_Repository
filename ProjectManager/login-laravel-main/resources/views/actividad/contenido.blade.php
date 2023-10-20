
<div>
    <table class="table">
    <thead>
        <tr>
        <th scope="col">#</th>
        <th scope="col">Actividad</th>
        <th scope="col">Prioridad</th>
        <th scope="col">Proyecto</th>
        <th scope="col">Usuario</th>
        <th scope="col">Acciones</th>
        </tr>
    </thead>
    <tbody>
    @if(Auth::User()->hasRole('administrador'))
        @foreach($relaciones as $r)
        <tr>
            <th scope="row" style="background-color:green">{{$loop->iteration}}</th>
            <td>{{$r->actividad->descripcion}}  </td>
            <td>{{$r->actividad->prioridad}}  </td>
            <td>{{$r->proyecto->nombre}}  </td>
            <td>{{$r->user->name}} {{$r->user->paterno}} {{$r->user->materno}}</td> 
            <td>
            <a  class="btn btn-primary btn-sm" href="actividad/{{$r->id}}">Consultar</a>
            <a  class="btn btn-success btn-sm" href="/actividad/{{$r->id}}/imagen">Subir evidencia</a>
            <a href="/actividad/{{$r->id}}/edit" class="btn btn-secondary btn-sm">Modificar</a>
            <button type="button" class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#modal-{{$r->id}}">
                Finalizar Actividad
            </button>
            <div class="modal fade" id="modal-{{$r->id}}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Eliminar</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form action="/relacion/{{$r->id}}" method="post" id="form-eliminar-{{$r->id}}">
                            @method('DELETE')
                            @csrf
                            ¿Estas seguro de borrarlo a: '{{$r->actividad->descripcion}}' del proyecto '{{$r->proyecto->nombre}}'?  
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="submit" class="btn btn-danger" form="form-eliminar-{{$r->id}}">Finalizar Tarea</button>
                    </div>
                </div>
            </div>
            </td>
        </tr>
        @endforeach
        @if(count($relaciones2)!=0)
            <tr>
                <td></td>
                <td>Terminados</td>
            </tr>
            @foreach($relaciones2 as $r)
            <tr>
                <th scope="row" style="background-color:red">{{$loop->iteration}}</th>
                <td>{{$r->actividad->descripcion}}  </td>
                <td>{{$r->actividad->prioridad}}  </td>
                <td>{{$r->proyecto->nombre}}  </td>
                <td>{{$r->user->name}} {{$r->user->paterno}} {{$r->user->materno}}</td> 
                <td> <a  class="btn btn-primary btn-sm" href="actividad/{{$r->id}}">Consultar</a> </td>
            </tr>
            @endforeach
        @endif
    @else
    @foreach($relaciones as $r)
        @if(Auth::User()->compararId($r->user->id))
        <tr>
            <th scope="row" style="background-color:green">{{$loop->iteration}}</th>
            <td>{{$r->actividad->descripcion}}  </td>
            <td>{{$r->actividad->prioridad}}  </td>
            <td>{{$r->proyecto->nombre}}  </td>
            <td>{{$r->user->name}} {{$r->user->paterno}} {{$r->user->materno}}</td> 
            <td>
            <a  class="btn btn-primary btn-sm" href="actividad/{{$r->id}}">Consultar</a>
            <a  class="btn btn-success btn-sm" href="actividad/{{$r->id}}/imagen">Subir evidencia</a>
            <button type="button" class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#modal-{{$r->id}}">
                Finalizar Actividad
            </button>
            <div class="modal fade" id="modal-{{$r->id}}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Eliminar</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form action="/relacion/{{$r->id}}" method="post" id="form-eliminar-{{$r->id}}">
                            @method('DELETE')
                            @csrf
                            ¿Estas seguro de borrarlo a: '{{$r->actividad->descripcion}}' del proyecto '{{$r->proyecto->nombre}}'?  
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="submit" class="btn btn-danger" form="form-eliminar-{{$r->id}}">Finalizar Tarea</button>
                    </div>
                </div>
            </div>
            </td>
        </tr>
        @endif
        @endforeach
            @if(count($relaciones2)!=0)
                <tr>
                    <td></td>
                    <td>Terminados</td>
                </tr>
                @foreach($relaciones2 as $r)
                @if(Auth::User()->compararId($r->user->id))
                <tr>
                    <th scope="row" style="background-color:red">{{$loop->iteration}}</th>
                    <td>{{$r->actividad->descripcion}}  </td>
                    <td>{{$r->actividad->prioridad}}  </td>
                    <td>{{$r->proyecto->nombre}}  </td>
                    <td>{{$r->user->name}} {{$r->user->paterno}} {{$r->user->materno}}</td> 
                    <td> <a  class="btn btn-primary btn-sm" href="actividad/{{$r->id}}">Consultar</a> </td>
                </tr>
                @endif
                @endforeach
            @endif
    @endif
    </tbody>
    </table>
</div>