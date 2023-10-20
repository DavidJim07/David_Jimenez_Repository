@extends('layouts.app-master')
@section('content')
<div>
    @auth
    @if(Auth::User()->hasRole('administrador'))
        <div class="container-fluid">
        <div class="card">
        <div class="card-header">
            CONSULTA DE PROYECTO
        </div>
        <div class="card-body">
            <form action="/proyecto" method="post">
            @csrf
            <div class="mb-3">
                <label for="nombre" class="form-label">Nombre:</label>
                <input type='text' name='nombre' id='nombre' class="form-control" value="{{$pro->nombre}}" readonly>
                <label for="tiempo" class="form-label">Tiempo de Desarrollo:</label>
                <input type='text' name='tiempo' id='tiempo' class="form-control" value="{{$pro->tiempoestimado}}" readonly>
                <label for="entrega" class="form-label">Fecha Entrega:</label>
                <input type='text' name='entrega' id='entrega' class="form-control" value="{{$pro->fentrega}}" readonly>
                <label for="descripcion" class="form-label">Descripcion:</label>
                <input type='text' name='descripcion' id='descripcion' class="form-control" value="{{$pro->descripcion}}" readonly>
                <label for="requerimientos" class="form-label">Requerimientos:</label>
                <input type='text' name='requerimientos' id='requerimientos' class="form-control" value="{{$pro->requerimientos}}" readonly>
            </div>
            </form>
            <a href="/proyecto" class="btn btn-primary btn-sm">Regresar</a>
        </div>
        </div>
    </div>
    @endif
    @endauth
</div>
@endsection