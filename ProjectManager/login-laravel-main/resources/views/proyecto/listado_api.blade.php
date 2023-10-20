<table class="table">
    <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Nombre</th>
            <th scope="col">Descripción</th>
            <th scope="col">Tiempo Estimado</th>
        </tr>
    </thead>
    <tbody>
        @foreach($proyectosArray as $r)
        <tr>
            <th scope="row"  style="background-color:green">{{$loop->iteration}}</th>
            <td>{{$r['nombre']}}</td>
            <td>{{$r['descripcion']}}</td>
            <td>{{$r['tiempoestimado']}}</td>
        </tr>
        @endforeach
</table>