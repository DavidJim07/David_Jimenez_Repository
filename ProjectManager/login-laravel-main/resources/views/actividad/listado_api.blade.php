<table class="table">
    <thead>
        <tr>
        <th scope="col">#</th>
        <th scope="col">Actividad</th>
        <th scope="col">Fecha Inicio</th>
        <th scope="col">Fecha Fin</th>
        <th scope="col">Prioridad</th>
        </tr>
    </thead>
    <tbody>
        @foreach($actividadesArray as $a)
        <tr>
            <th scope="row" style="background-color:green">{{$loop->iteration}}</th>
            <td>{{$a['descripcion']}}  </td>
            <td>{{$a['finicio']}}  </td>
            <td>{{$a['ffin']}}  </td>
            <td>{{$a['prioridad']}}</td> 
        </tr>
        @endforeach
</table>