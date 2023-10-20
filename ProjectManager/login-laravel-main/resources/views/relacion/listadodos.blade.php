@extends('layouts.app-master')
@section('content')
<body>
    <p>bhfdjhdsfsdjkfsdjk</p>
    @auth
    @if(Auth::User()->hasRole('administrador'))
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
        @if($r->id_usu==$idd)
            <tr>
            <th scope="row">{{$loop->iteration}}</th>
            <td>@foreach($actividades as $ac) @if($ac->id==$r->id_act){{$ac->descripcion}} @endif @endforeach</td>
            <td>@foreach($proyectos as $pr) @if($pr->id==$r->id_pro){{$pr->nombre}} @endif @endforeach</td>
            <td>@foreach($usuarios as $us) @if($us->id==$r->id_usu){{$us->name}} {{$us->paterno}} {{$us->materno}}@endif @endforeach</td> 
            <td>
            <a  class="btn btn-primary btn-sm" @foreach($actividades as $ac) @if($ac->id==$r->id_act)href="/actividad/{{$r->id_act}}" @endif @endforeach>Consultar</a>
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