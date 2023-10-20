    <table class="table">
    <thead>
        <tr>
        <th scope="col">#</th>
        <th scope="col">Nombre</th>
        <th scope="col">FechaNacimiento</th>
        <th scope="col">Genero</th>
        <th scope="col">Rol</th>
        <th scope="col">Usuario</th>
        <th scope="col">Acciones</th>
        </tr>
    </thead>
    <tbody>
        @foreach($usuarios as $u)
            @if($u->estado==1)
            <tr>
            <th scope="row">{{$loop->iteration}}</th>
            <td>{{$u->name}} {{$u->paterno}} {{$u->materno}}</td>
            <td>{{ \Carbon\Carbon::parse($u->fecha_nacimiento)->format('d/m/Y')}}</td>
            <td>{{$u->genero}}</td>
            <td>{{$u->role}}</td>
            <td>{{$u->username}}</td>
            <td>
                <a href="/usuario/{{$u->id}}" class="btn btn-primary btn-sm">Consultar</a>
                <a href="/usuario/{{$u->id}}/edit" class="btn btn-warning btn-sm">Modificar</a>
                <!-- <a href="/usuario/{{$u->id}}/editPassword" class="btn btn-warning btn-sm">Modificar Contraseña</a> -->
                <!-- Button trigger modal -->
                <button type="button" class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#modal-{{$u->id}}">
                Eliminar
                </button>
                <!-- Modal -->
                <div class="modal fade" id="modal-{{$u->id}}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Eliminar Usuario</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form action="/usuario/{{$u->id}}" method="post" id="form-eliminar-{{$u->id}}">
                            @method('DELETE')
                            @csrf
                            ¿Estas seguro de borrar el usuario: {{$u->name}} {{$u->paterno}} {{$u->materno}}? 
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="submit" class="btn btn-danger" form="form-eliminar-{{$u->id}}">Eliminar</button>
                    </div>
                    </div>
                </div>
                </div>

            </td>
            </tr>
            @endif
        @endforeach
    </table>