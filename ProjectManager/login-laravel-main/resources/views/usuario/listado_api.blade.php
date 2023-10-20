<table class="table">
    <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Nombre</th>
            <th scope="col">FechaNacimiento</th>
            <th scope="col">Genero</th>
            <th scope="col">Rol</th>
            <th scope="col">Usuario</th>
        </tr>
    </thead>
    <tbody>
        @foreach($usuariosArray as $u)
            <tr>
                <th scope="row">{{$loop->iteration}}</th>
                <td>{{$u['name']}} {{$u['paterno']}} {{$u['materno']}}</td>
                <td>{{ \Carbon\Carbon::parse($u['nacimiento'])->format('d/m/Y')}}</td>
                <td>{{$u['genero']}}</td>
                <td>{{$u['role']}}</td>
                <td>{{$u['username']}}</td>
            </tr>
        @endforeach
    </table>