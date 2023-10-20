@extends('layouts.app-master')
@section('content')
    <div class="bg-light p-5 rounded">
        @auth
        <h1>ITZ BACK</h1>
        @if(Auth::User()->hasRole('administrador'))
            <p>Bienvenido es momento de administrar y trabajar</p>
            <a class="btn btn-lg btn-primary" href="/proyecto" role="button">Ver proyectos pendientes &raquo;</a>
        @endif 
        @if(Auth::User()->hasRole('desarrollador'))
            <p class="lead">Bienvenido es momento de trabajar</p>
            <a class="btn btn-lg btn-primary" href="/actividad" role="button">Ver actividades pendientes &raquo;</a>
        @endif 
        @endauth

        @guest
        <h1>ITZ BACK</h1>
        <p class="lead">ITZ BACK.</p>
        @endguest
    </div>
@endsection