@extends('layouts.app-master')
@section('content')
<body>
    @auth
    @if(Auth::User()->hasRole('desarrollador') || Auth::User()->hasRole('administrador'))
    <table class="table">
    <thead>
        <tr>
        <th scope="col">#</th>
        <th scope="col">Actividad</th>
        <th scope="col">Proyecto</th>
        <th scope="col">Usuario</th>
        <th scope="col">Acciones</th>
        </tr>
    </thead>
    <tbody>
        @foreach($relaciones as $r)
        @if($r->id_usu==Auth::User()->id || $r->id_pro==$id)
            <tr>
            <th scope="row">{{$loop->iteration}}</th>
            <td>{{$r->actividad->descripcion}}</td>
            <td>{{$r->proyecto->nombre}}</td>
            <td>{{$r->user->name}} {{$r->user->paterno}} {{$r->user->materno}}</td> 
            <td>
            <a  class="btn btn-primary btn-sm" href="/actividad/{{$r->id}}">Consultar</a>
            </td>
            </tr>
        @endif
        @endforeach
    </tbody>
    </table>
    @endif
    @endauth
</body>
@endsection