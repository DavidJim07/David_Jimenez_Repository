@extends('layouts.app-master')
@section('content')
<a href="/zapatos/create"  class="btn btn-link">Registrar Nuevo Zapato</a>
<hr>
<div class="container-fluid">
    <table class="table table-light">
        <thead class="table-secondary">
            <tr>
                <th>Codigo de Barras</th>
                <th>Modelo</th>
                <th>Material</th>
                <th>Estilo</th>
                <th>Color</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody id="tabla-productos" class="table-group-divider">
        @foreach($zp as $z)
            <td>{{$z->id}}</td>
            <td>{{$z->modelo}}</td>            
            <td>{{$z->material}}</td>
            <td>{{$z->estilo}}</td>
            <td>{{$z->color}}</td>
            <td>
            @csrf
                <a href="/zapatos/{{$z->id}}" class="btn btn-info btn-sm">Consultar</a>
                <a href="/zapatos/{{$z->id}}/edit" class="btn btn-warning btn-sm">Modificar</a>
                <a href="/talla/listado/{{$z->id}}"  class="btn btn-secondary btn-sm">Inventario</a>
                
                <button type="button" class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#modal-{{$z->id}}">
                Eliminar Zapato
                </button>
                
                <div class="modal fade" id="modal-{{$z->id}}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Eliminar</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form action="/zapatos/{{$z->id}}" method="post" id="form-eliminar-{{$z->id}}">
                            @method('DELETE')
                            @csrf
                            ¿Estas Seguro de Eliminar el Zapato: {{$z->id}}? 
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="submit" class="btn btn-danger" form="form-eliminar-{{$z->id}}">Eliminar Zapato</button>
                    </div>
                    </div>
                </div>
                </div>
            </td>
            </tr>
        @endforeach
        </tbody>
    </table>
</div>
@endsection

