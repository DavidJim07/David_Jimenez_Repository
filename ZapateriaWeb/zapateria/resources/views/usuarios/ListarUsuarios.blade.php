@extends('layouts.app-master')
@section('content')
<a href="/usuario/create"  class="btn btn-link">Registrar Nuevo Usuario</a>
<hr>
<div class="container-fluid">
    <table class="table table-light">
        <thead class="table-secondary">
            <tr>
                <th>#</th>
                <th>Nombre</th>
                <th>Fecha Nacimiento</th>
                <th>Telefono</th>
                <th>Correo</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody id="tabla-productos" class="table-group-divider">
        @foreach($usuarios as $u)
            <td>{{$loop->iteration}}</td>
            <td>{{$u->name}} {{$u->paterno}} {{$u->materno}}</td>
            <td>{{$u->fechanacimiento}}</td>
            <td>{{$u->telefono}}</td>
            <td>{{$u->email}}</td>
            <td>
            @csrf
                <a href="/usuario/{{$u->id}}" class="btn btn-info btn-sm">Consultar</a>
                <a href="/usuario/{{$u->id}}/edit" class="btn btn-warning btn-sm">Modificar</a>
                
                <button type="button" class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#modal-{{$u->id}}">
                Eliminar Usuario
                </button>
                
                <div class="modal fade" id="modal-{{$u->id}}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Eliminar</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form action="/usuario/{{$u->id}}" method="post" id="form-eliminar-{{$u->id}}">
                            @method('DELETE')
                            @csrf
                            ¿Estas Seguro de Eliminar al Usuario: {{$u->name}} {{$u->paterno}} {{$u->materno}}? 
                            Nota: Esto incluye sus domicilios y tarjetas
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button type="submit" class="btn btn-danger" form="form-eliminar-{{$u->id}}">Eliminar Usuario</button>
                    </div>
                    </div>
                </div>
                </div>

            </td> </tr>
            
        @endforeach
        </tbody>
    </table>
</div>
@endsection

