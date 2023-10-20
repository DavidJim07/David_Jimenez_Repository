@extends('layouts.app-master')
@section('content')
<body>
  <div class="container">
    <h2>Consulta de Usuario</h2>
    <form action="/usuario"  method="post" >
        @csrf
        <div class="mb-3">
            <label class="form-label">Nombre:</label>
            <input type="text" class="form-control" name="nombre"  value="{{$user->name}}" readonly>
        </div>
        <div class="mb-3">
            <label class="form-label">Paterno:</label>
            <input type="text" class="form-control" name="paterno" value="{{$user->paterno}}" readonly>
        </div>
        <div class="mb-3">
            <label class="form-label">Materno:</label>
            <input type="text" class="form-control" name="materno"value="{{$user->materno}}" readonly>
        </div>
        <div class="mb-3">
            <label class="form-label" >Fecha de Nacimiento:</label>
            <input type='date' id='nacimiento' name='nacimiento' class="form-control" value="{{$user->fechanacimiento}}" readonly/>
        </div>
        <div class="mb-3">
            <label for="genero" class="form-label">Género:</label><br>
            <input type='radio' name='genero' id='femenino' value='F' class="form-check-input" disabled
            @if($user->genero=='F')
                checked
            @endif
            >Femenino <br>
            <input type='radio' name='genero' id='masculino' value='M' class="form-check-input" disabled
            @if($user->genero=='M')
                checked
            @endif
            >Masculino
        </div>
        <div class="mb-3">
            <label for="telefono" class="form-label">Telefono:</label>
            <input type='text' name='telefono' id='telefono' class="form-control" value="{{$user->telefono}}">
        </div>
        <a type="submit" href="/usuario" class="btn btn-info">Regresar</a>
    </form>
  </div>
</body>
    @endsection

