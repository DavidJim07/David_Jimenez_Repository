@extends('layouts.app-master')
@section('content')
<div>
    @auth
    @if(Auth::User()->hasRole('desarrollador') || Auth::User()->hasRole('administrador'))
    <div class="container-fluid">
        <h1> Consulta de Actividades</h1>
    <form action="/actividad" method="post" class="form-group">
        @csrf
        <div class="row">
            <div class="col-md-4">
                <div class="mb-3">
                    <label class="col-form-label-lg"> Descripcion de la actividad</label>
                    <input type="text" class="form-control input-group-lg" id="descripcion" name="descripcion" value="{{$relacion->actividad->descripcion}}" readonly>
                </div>
                <div class="mb-3">
                    <label class="col-form-label-lg">Selecciona el Proyecto</label>
                    <input type="text" class="form-control input-group-lg" id="proyecto" name="proyecto" value="{{$relacion->proyecto->nombre}}" readonly>
                </div>

                <div class="mb-3">
                    <label class="col-form-label-lg">Selecciona el desarrollador</label>
                    <input type="text" class="form-control input-group-lg" id="desarrollador" name="desarrollador" value="{{$relacion->user->name}} {{$relacion->user->paterno}} {{$relacion->user->materno}}" readonly>
                </div>
                
                <div class="mb-3">
                    <label class="col-form-label-lg">Selecciona la Prioridad</label>
                    <input type="text" class="form-control input-group-lg" id="prioridad" name="prioridad" value="{{$relacion->actividad->prioridad}}" readonly>
                </div>
        </div>
        <div class="col-md-4">
            <div class="mb-3">
                <label class="col-form-label-lg"> Tiempo estimado la Actividad</label>
                <input type="text" class="form-control" id="tiempoes" name="tiempoes" rows="3" value="{{$relacion->actividad->testimado}}" readonly></input>
            </div>
            <div class="input-group mb-3">
                <label class="col-form-label-lg">Fecha de Inicio</label>
                <input type="text" class="form-control" id="fechaInicio" name="fechaInicio" rows="3" value="{{$relacion->actividad->finicio}}" readonly></input>
            </div>
            <div class="input-group mb-3">
                <label class="col-form-label-lg">Fecha de Entrega</label>
                <input type="text" class="form-control" id="fechaFin" name="fechaFin" rows="3" value="{{$relacion->actividad->ffin}}" readonly></input>
            </div>
        </div>       
        </div>
        @foreach($imagenes as $imagen)
            <table align="center">
                <td><img src="{{URL::to('/')}}/images/{{$imagen->image}}" alt="Not Found" width="300 px" height="300 px"></td>
            </table>
        @endforeach
        <div class="mb-3">
            <a  class="btn btn-primary" href="/actividad">Regresar</a>
        </div>
    </form>
    </div>
    @endif
    @endauth
</div>
@endsection