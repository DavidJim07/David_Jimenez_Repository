@extends('layouts.app-master')
@section('content')
<h1>Codigo del Zapato: {{$id}}</h1><br>
<a href="/talla/surtir/{{$id}}"  class="btn btn-link"> Registrar Nueva Talla</a>
<hr>
@if(count($zp))
<table class="table table-light">
    <thead class="table-secondary">
        <tr>
            <th>Existencia</th>
            <th>Talla</th>
            <th>Precio</th>
            <th>Acciones</th>
        </tr>
    </thead>
    <tbody id="tabla-productos" class="table-group-divider">

@foreach($zp as $z)
<td>{{$z->cantidad}}</td>
<td>{{$z->talla}}</td>
<td>{{$z->precio}}</td>
<td>
@csrf
    <a href="/talla/{{$z->id}}/edit" class="btn btn-warning btn-sm">Modificar</a>
    <a href="/talla/resurtir/{{$z->idzapato}}"  class="btn btn-info btn-sm">Surtir</a>
    <button type="button" class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#modal-{{$z->id}}">
    Eliminar Talla
    </button>    
    <div class="modal fade" id="modal-{{$z->id}}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Eliminar</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <form action="/talla/{{$z->id}}" method="post" id="form-eliminar-{{$z->id}}">
                @method('DELETE')
                @csrf
                ¿Estas Seguro de Eliminar la talla: {{$z->talla}}? 
            </form>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
            <button type="submit" class="btn btn-danger" form="form-eliminar-{{$z->id}}">Eliminar Talla</button>
        </div>
        </div>
    </div>
    </div>
</td>
</tr>
@endforeach
</tbody>
</table>
@else 
<h1>No existen Tallas registradas</h1>
@endif
<a type="submit" href="/zapatos" class="btn btn-dark mt-3">Regresar</a>
    @endsection