@extends('layouts.auth-master')

@section('content')
    <form method="post" action="{{ route('register.perform') }}" class="container w-25">

        <input type="hidden" name="_token" value="{{ csrf_token() }}" />
        <h1 class="h3 mb-3 fw-normal">Register</h1>

        <div class="form-group form-floating mb-3">
            <input type="text" class="form-control" name="name" value="{{ old('name') }}" placeholder="Juan Perez" required="required" autofocus>
            <label for="floatingEmail">Nombre</label>
            @if ($errors->has('name'))
                <span class="text-danger text-left">{{ $errors->first('name') }}</span>
            @endif
        </div>
        <div class="mb-3">
            <label class="col-form-label-lg">Apellido Paterno</label>
            <input type="text" class="form-control input-group-lg"  id="paterno" name="paterno">
        </div>
        <div class="mb-3">
            <label class="col-form-label-lg">Apellido Materno</label>
            <input type="text" class="form-control" id="materno" name="materno"></input>
        </div>
        <div class="mb-3">
            <label class="col-form-label-lg">Telefono</label>
            <input type="number" class="form-control" id="telefono" name="telefono"></input>
        </div>
        <div class="mb-3">
            <label class="col-form-label-lg">Cargo</label>
            <select class="form-select" aria-label="Default select example" id="role" name="role">
                <option selected>Seleeciona el Cargo</option>
                <option value="desarrollador">Desarrollador</option>
                <option value="administrador">Administrador</option>
            </select>
        </div>

        <div class="mb-3">
            <label for="genero">Selecciona tu Sexo</label>
            <select class="form-select" aria-label="Default select example" id="genero" name="genero">
                <option value="M">Masculino</option>
                <option value="F">Femenino</option>
            </select>
        </div>
        <div class="mb-3">
            <label for="nacimiento">Fecha de Nacimiento</label>
            <input type="date" class="form-control" id="nacimiento" name="nacimiento"></input>
        </div>

        <div class="form-group form-floating mb-3">
            <input type="email" class="form-control" name="email" value="{{ old('email') }}" placeholder="name@example.com" required="required" autofocus>
            <label for="floatingEmail">Email address</label>
            @if ($errors->has('email'))
                <span class="text-danger text-left">{{ $errors->first('email') }}</span>
            @endif
        </div>

        <div class="form-group form-floating mb-3">
            <input type="text" class="form-control" name="username" value="{{ old('username') }}" placeholder="Username" required="required" autofocus>
            <label for="floatingName">Username</label>
            @if ($errors->has('username'))
                <span class="text-danger text-left">{{ $errors->first('username') }}</span>
            @endif
        </div>
        
        <div class="form-group form-floating mb-3">
            <input type="password" class="form-control" name="password" value="{{ old('password') }}" placeholder="Password" required="required">
            <label for="floatingPassword">Password</label>
            @if ($errors->has('password'))
                <span class="text-danger text-left">{{ $errors->first('password') }}</span>
            @endif
        </div>

        <div class="form-group form-floating mb-3">
            <input type="password" class="form-control" name="password_confirmation" value="{{ old('password_confirmation') }}" placeholder="Confirm Password" required="required">
            <label for="floatingConfirmPassword">Confirm Password</label>
            @if ($errors->has('password_confirmation'))
                <span class="text-danger text-left">{{ $errors->first('password_confirmation') }}</span>
            @endif
        </div>
        <div class="mb-3">
            <input type="text" class="form-control" id="estado" name="estado" value="1" hidden></input>
        </div>
    </form>
    <a  class="btn btn-primary" href="/home">Regresar</a>
    <button class="btn btn-primary" type="submit">Registrar</button>
@endsection