@extends('layouts.app-master')
@section('content')
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="{{ asset('css/bootstrap.css')}}">
</head>
<body>
    <div class="container-fluid">
        <div class="card">
        <div class="card-header">
            Registro Usuario
        </div>
        @if($errors->any())
            <div class="alert alert-danger">
                <ul>
                    @foreach($errors->all() as $error)
                        <li>{{$error}}</li>
                    @endforeach
                </ul>
            </div>
        @endif
        <div class="card-body">
            <form action="/usuario" method="post">
            @csrf

            <div class="mb-3">
                <label for="nombre" class="form-label">Nombre:</label>
                <input type='text' name='nombre' id='nombre' class="form-control">
            </div>
            <div class="mb-3">
                <label for="paterno" class="form-label">A.Paterno:</label>
                <input type='text' name='paterno' id='paterno' class="form-control">
            </div>
            <div class="mb-3">
                <label for="materno" class="form-label">A.Materno:</label>
                <input type='text' name='materno' id='materno' class="form-control">
            </div>
            <div class="mb-3">
                <label for="fecha" class="form-label">F.Nacimiento:</label>
                <input type='date' name='fecha' id='fecha' class="form-control">
            </div>
            <div class="mb-3">
                <label for="genero" class="form-label">Género:</label><br>
                <input type='radio' name='genero' id='femenino' value='F' class="form-check-input"
                @if(old('genero')=='F')
                    checked
                @endif
                >Femenino <br>
                <input type='radio' name='genero' id='masculino' value='M' class="form-check-input"
                @if(old('genero')=='M')
                    checked
                @endif
                >Masculino
            </div>
            <div class="mb-3">
                <label for="telefono" class="form-label">Telefono:</label>
                <input type='text' name='telefono' id='telefono' class="form-control">
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Correo Electronico:</label>
                <input type='text' name='email' id='email' class="form-control">
            </div>
            <div class="mb-3">
                <label for="rol" class="form-label">Rol:</label><br>
                <input type='radio' name='rol' id='admin' value='administrador' class="form-check-input"
                @if(old('rol')=='administrador')
                    checked
                @endif
                >Administrador <br>
                <input type='radio' name='rol' id='dess' value='desarrollador' class="form-check-input"
                @if(old('rol')=='desarrollador')
                    checked
                @endif
                >Desarrollador
            </div>
            <div class="mb-3">
                <label for="usuario" class="form-label">Usuario:</label>
                <input type='text' name='usuario' id='usuario' class="form-control">
            </div>
            <div class="mb-3">
                <label for="contraseña" class="form-label">Password</label>
                <input type="password" name='contraseña' id='contraseña' class="form-control">
            </div>
            <a  class="btn btn-primary" href="/usuario">Regresar</a>
            <button type="submit" class="btn btn-primary">Agregar</button>
            </form>
        </div>
        </div>
    
    </div>
    
    <script type="text/javascript" src="{{ asset('js/bootstrap.js') }}"></script>
</body>
</html>
@endsection