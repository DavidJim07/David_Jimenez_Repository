@extends('layouts.app-master')
@section('content')
<div>
    @auth
    @if(Auth::User()->hasRole('desarrollador') || Auth::User()->hasRole('administrador'))
    <div class="container-fluid">
        <h1> Registro de Actividades</h1>
    <form action="/actividad" method="post" class="form-group">
        @if($errors->any())
            <div class="alert alert-danger">
                <ul>
                    @foreach($errors->all() as $error)
                        <li>{{$error}}</li>
                    @endforeach
                </ul>
            </div>
        @endif
        @csrf
        <div class="row">
            <div class="col-md-4">
                <div class="mb-3">
                    <label class="col-form-label-lg"> Descripcion de la actividad</label>
                    <input type="text" class="form-control input-group-lg" id="descripcion" name="descripcion" value="{{ old('descripcion') }}">
                </div>
                <div class="mb-3">
                    <label class="col-form-label-lg">Selecciona el Proyecto</label>
                        <select class="form-select" aria-label="Default select example" id="proyecto" name="proyecto" value="{{ old('proyecto') }}">
                        @foreach($proyecto as $p)
                            @if($p->estado!=0)             
                                <option value="{{ $p->id}}">{{ $p->nombre}}</option>
                            @endif
                        @endforeach
                        </select>
                </div>

                <div class="mb-3">
                    <label class="col-form-label-lg">Selecciona el desarrollador</label>
                        <select class="form-select" aria-label="Default select example" id="usu" name="usu" value="{{ old('usu') }}">
                        @foreach($usu as $u)
                            @if($u->estado!=0)             
                                <option value="{{$u->id}}">{{$u->name}} {{$u->paterno}} {{$u->materno}}</option>
                            @endif
                        @endforeach
                        </select>
                </div>
                
                <div class="mb-3">
                    <label class="col-form-label-lg">Selecciona la Prioridad</label>
                        <select class="form-select" aria-label="Default select example" id="prioridad" name="prioridad">
                            <option value="Alta">Alta</option>
                            <option value="Media">Media</option>
                            <option value="Baja">Baja</option>
                        </select>
                </div>
        </div>
        <div class="col-md-4">
            <div class="mb-3">
                <label class="col-form-label-lg"> Tiempo estimado la Actividad</label>
                <input type="text" class="form-control" id="tiempoes" name="tiempoes" rows="3" value="{{ old('tiempoes') }}"></input>
            </div>
            <label class="col-form-label-lg">Fecha de Inicio</label>
            <div class="input-group mb-3">
                <span class="input-group-text">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-calendar-date" viewBox="0 0 16 16">
                        <path d="M6.445 11.688V6.354h-.633A12.6 12.6 0 0 0 4.5 7.16v.695c.375-.257.969-.62 1.258-.777h.012v4.61h.675zm1.188-1.305c.047.64.594 1.406 1.703 1.406 1.258 0 2-1.066 2-2.871 0-1.934-.781-2.668-1.953-2.668-.926 0-1.797.672-1.797 1.809 0 1.16.824 1.77 1.676 1.77.746 0 1.23-.376 1.383-.79h.027c-.004 1.316-.461 2.164-1.305 2.164-.664 0-1.008-.45-1.05-.82h-.684zm2.953-2.317c0 .696-.559 1.18-1.184 1.18-.601 0-1.144-.383-1.144-1.2 0-.823.582-1.21 1.168-1.21.633 0 1.16.398 1.16 1.23z"/>
                        <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z"/>
                    </svg>
                </span>
                <input type="date" class="form-control" id="inicioact" name="inicioact" value="{{ old('inicioact') }}"></input>
            </div>
            <label class="col-form-label-lg">Fecha de Entrega</label>
            <div class="input-group mb-3">
                <span class="input-group-text">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-calendar-date" viewBox="0 0 16 16">
                        <path d="M6.445 11.688V6.354h-.633A12.6 12.6 0 0 0 4.5 7.16v.695c.375-.257.969-.62 1.258-.777h.012v4.61h.675zm1.188-1.305c.047.64.594 1.406 1.703 1.406 1.258 0 2-1.066 2-2.871 0-1.934-.781-2.668-1.953-2.668-.926 0-1.797.672-1.797 1.809 0 1.16.824 1.77 1.676 1.77.746 0 1.23-.376 1.383-.79h.027c-.004 1.316-.461 2.164-1.305 2.164-.664 0-1.008-.45-1.05-.82h-.684zm2.953-2.317c0 .696-.559 1.18-1.184 1.18-.601 0-1.144-.383-1.144-1.2 0-.823.582-1.21 1.168-1.21.633 0 1.16.398 1.16 1.23z"/>
                        <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z"/>
                    </svg>
                </span>
                <input type="date" class="form-control" id="finact" name="finact" value="{{ old('finact') }}"></input>
            </div>
        </div>       
        </div>
        <a  class="btn btn-primary" href="/actividad">Regresar</a>
        <button type="submit" class="btn btn-primary">Agregar</button>
    </form>
    </div>
    @endif
    @endauth
</div>
@endsection