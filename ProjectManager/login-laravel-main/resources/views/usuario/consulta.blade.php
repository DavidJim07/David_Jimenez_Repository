<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="{{asset('css/bootstrap.css')}}">
</head>
<body>
    @include('menu')
    <div class="container-fluid">
        <div class="card">
        <div class="card-header">
            Registro Usuario
        </div>
        <div class="card-body">
            <form action="/usuario" method="post">
            @csrf

            <div class="mb-3">
                <label for="nombre" class="form-label">Nombre:</label>
                <input type='text' name='nombre' id='nombre' class="form-control" value="{{$usuario->name}}" readonly>
            </div>
            <div class="mb-3">
                <label for="paterno" class="form-label">A.Paterno:</label>
                <input type='text' name='paterno' id='paterno' class="form-control" value="{{$usuario->paterno}}" readonly>
            </div>
            <div class="mb-3">
                <label for="materno" class="form-label">A.Materno:</label>
                <input type='text' name='materno' id='materno' class="form-control" value="{{$usuario->materno}}" readonly>
            </div>
            <div class="mb-3">
                <label for="fecha" class="form-label">F.Nacimiento:</label>
                <input type='date' name='fecha' id='fecha' class="form-control" value="{{$usuario->nacimiento }}" readonly>
            </div>
            <div class="mb-3">
                <label for="genero" class="form-label">Género:</label>
                <input type='text' name='genero' id='genero' class="form-control" value="{{$usuario->genero}}" readonly>
            </div>
            <div class="mb-3">
                <label for="telefono" class="form-label">Telefono:</label>
                <input type='text' name='telefono' id='telefono' class="form-control" value="{{$usuario->telefono}}" readonly>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Correo Electronico:</label>
                <input type='text' name='email' id='email' class="form-control" value="{{$usuario->email}}" readonly>
            </div>
            <div class="mb-3">
                <label for="rol" class="form-label">Rol:</label>
                <input type='text' name='genero' id='genero' class="form-control" value="{{$usuario->role}}" readonly>
            </div>
            <div class="mb-3">
                <label for="usuario" class="form-label">Usuario:</label>
                <input type='text' name='usuario' id='usuario' class="form-control" value="{{$usuario->username}}" readonly>
            </div>
            <div class="mb-3">
                <label for="contraseña" class="form-label">Password</label>
                <input type="password" name='contraseña' id='contraseña' class="form-control" value="{{$usuario->password}}" readonly>
            </div>
            </form>
            <a  class="btn btn-primary btn-sm" href="/usuario">Regresar</a>
        </div>
        </div>
    
    </div>
    
    <script type="text/javascript" src="{{ asset('js/bootstrap.js') }}"></script>
</body>
</html>