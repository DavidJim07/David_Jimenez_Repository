@extends('layouts.app-master')
@section('content')
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro Usuario</title>
</head>
<body>
    <br>
    <div class="container-fluid" name='registro'>
        @if($errors->any())
            <div class="alert alert-danger">
                <ul>
                    @foreach($errors->all() as $error)
                        <li>{{$error}}</li>
                    @endforeach
                </ul>
            </div>
        @endif
        <div class="container-fluid">
            <div class="card">
                <div class="card-header text-center">
                    Registro Usuario
                </div>
                <form action="/usuario" method="post" class="card-body">
                    @csrf
                    <div class="row">
                        <div class="col">
                            <h5 class="h5 text-center">Datos Personales</h5>
                            <div class="row">
                                <div class="col">
                                    <div class="mb-3">
                                        <label class="form-label" >Nombre:</label>
                                        <input type='text' id='nombre' name='nombre' class="form-control" value="{{ old('nombre') }}"/>
                                    </div>
                                    <div class="mb-3">
                                        <label class="form-label" >Apellido Paterno:</label>
                                        <input type='text' id='paterno' name='paterno' class="form-control" value="{{ old('paterno') }}"/>
                                    </div>
                                    <div class="mb-3">
                                        <label class="form-label" >Apellido Materno:</label>
                                        <input type='text' id='materno' name='materno' class="form-control" value="{{ old('materno') }}"/>
                                    </div>
                                    <div class="mb-3">
                                        <label class="form-label" >Fecha de Nacimiento:</label>
                                        <input type='date' id='nacimiento' name='nacimiento' class="form-control" value="{{ old('nacimiento') }}"/>
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
                                </div>
                                <div class="col">
                                    <div class="mb-3">
                                        <label for="telefono" class="form-label">Telefono:</label>
                                        <input type='text' name='telefono' id='telefono' class="form-control" value="{{ old('telefono') }}">
                                    </div>
                                    <hr>
                                    <h6 class="h6 text-center">Datos Para Crear Cuenta:</h6>
                                    <div class="mb-3">
                                        <label for="email" class="form-label">Correo Electronico:</label>
                                        <input type='text' name='email' id='email' class="form-control" value="{{ old('email') }}">
                                    </div>
                                    <!-- <div class="mb-3">
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
                                    </div> -->
                                    <div class="mb-3">
                                        <label for="password" class="form-label">Password</label>
                                        <input type="password" name='password' id='password' class="form-control" value="{{ old('password') }}">
                                    </div>
                                    @if(Auth::check())
                                        @auth
                                            @if(auth()->user()->role=="A")
                                            <div class="mb-3">
                                                <label for="rol" class="form-label">Género:</label><br>
                                                <input type='radio' name='rol' id='Usuario' value='Usuario' class="form-check-input"
                                                @if(old('rol')=='Usuario')
                                                    checked
                                                @endif
                                                >Usuario <br>
                                                <input type='radio' name='rol' id='Administrador' value='Administrador' class="form-check-input"
                                                @if(old('rol')=='Administrador')
                                                    checked
                                                @endif
                                                >Administrador
                                            </div>
                                            @endif
                                        @endauth
                                    @endif
                                </div>
                            </div>
                        </div>
                        <div class="col">
                            <h5 class="h5 text-center">Domicilio</h5>
                            <div class="row">
                                <div class="col">
                                    <div class="mb-3">
                                        <label class="form-label" >Pais:</label>
                                        <input type='text' id='pais' name='pais' class="form-control" value="{{ old('pais') }}"/>
                                    </div>
                                    <div class="mb-3">
                                        <label class="form-label" >Estado:</label>
                                        <input type='text' id='estado' name='estado' class="form-control" value="{{ old('estado') }}"/>
                                    </div>
                                    <div class="mb-3">
                                        <label class="form-label" >Ciudad:</label>
                                        <input type='text' id='ciudad' name='ciudad' class="form-control" value="{{ old('ciudad') }}"/>
                                    </div>
                                    <div class="mb-3">
                                        <label class="form-label" >Colonia:</label>
                                        <input type='text' id='colonia' name='colonia' class="form-control" value="{{ old('colonia') }}"/>
                                    </div>
                                    <div class="mb-3">
                                        <label class="form-label" >Codigo Postal:</label>
                                        <input type='text' id='codigoPostal' name='codigoPostal' class="form-control" value="{{ old('codigoPostal') }}"/>
                                    </div>
                                </div>
                                <div class="col">
                                    <div class="mb-3">
                                        <label class="form-label" >Calle:</label>
                                        <input type='text' id='calle' name='calle' class="form-control" value="{{ old('calle') }}"/>
                                    </div>
                                    <div class="mb-3">
                                        <label class="form-label" >Numero:</label>
                                        <input type='number' id='numero' name='numero' class="form-control" value="{{ old('numero') }}"/>
                                    </div>
                                    <div class="mb-3">
                                        <label class="form-label" >EntreCalles:</label>
                                        <input type='text' id='entreCalles' name='entreCalles' class="form-control" value="{{ old('entreCalles') }}"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <button type='submit' class="btn btn-success">Registrarse</button>
                    <button type='reset' id='limpiar2' class="btn btn-warning">Limpiar Cajas</button> 
                    <hr>
                    <div class="row">
                        <div class="col">
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="flexCheckDefault" onclick="verificarCheckbox()">
                                <label class="form-check-label" for="flexCheckDefault">Agregar datos Bancarios</label>
                            </div>
                            <div class="mb-3">
                                <label class="form-label" >Nombre Tarjeta:</label>
                                <input type='text' id='tarjeta' name='tarjeta' class="form-control" value="{{ old('tarjeta') }}"/>
                            </div>
                            <div class="mb-3">
                                <label class="form-label" >Número de la Tajeta:</label>
                                <input type='text' id='numeroTarjeta' name='numeroTarjeta' class="form-control" value="{{ old('numeroTarjeta') }}"/>
                            </div>
                            <div class="mb-3">
                                <label class="form-label" >Fecha de Vencimiento:</label>
                                <input type='date' id='vencimiento' name='vencimiento' class="form-control" value="{{ old('vencimiento') }}"/>
                            </div>
                            <div class="mb-3">
                                <label class="form-label" >CCV:</label>
                                <input type='number' id='ccv' name='ccv' class="form-control" maxlength="3" value="{{ old('ccv') }}"/>
                            </div>
                        </div>
                        <div class="col"></div>
                        <div class="col"></div>
                    </div>
                    <hr>
                    <button type='submit' id='guardar' class="btn btn-success">Registrarse</button>  
                    <button type='reset' id='limpiar' class="btn btn-warning">Limpiar Cajas</button> 
                </form>
            </div>
        </div>
    </div>
</body>
<script type="text/javascript" src="{{ asset('js/habilitador.js') }}"></script>
</html>
@endsection