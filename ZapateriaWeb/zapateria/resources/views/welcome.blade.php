@extends('layouts.app-master')
@section('content')
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="{{asset('css/bootstrap.css')}}">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <style>
      body {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
      }
      .container-login {
        max-width: 400px;
        margin: 0 auto;
        margin-top: 100px;
      }
      .btn-register {
        background-color: #007bff;
        border-color: #007bff;
      }
    </style>
  </head>
  <body>
    <header class="bg-dark text-white py-2">
      <div class="container">
        <h1 class="mb-0">Zapateria</h1>
        <div><a href="/">Ir a la tienda</a></div>
      </div>
    </header>
    @include('layouts.partials.messages')
    <title>Inicio de sesión</title>
    <form method="post" action="{{ route('login.perform') }}" class="container flex-grow-1">
      <input type="hidden" name="_token" value="{{ csrf_token() }}" />
      <div class="container-login bg-light p-5 rounded">
        <h1 class="text-center mb-4">Iniciar sesión</h1>
          <div class="form-group">
            <label for="email">Correo electrónico:</label>
            <input type="text" class="form-control" id="email" name="email" required="required" autofocus>
          </div>
          <div class="form-group">
            <label for="password">Contraseña:</label>
            <input type="password" class="form-control" id="password" name="password" required="required">
          </div>
          <button type="submit" class="btn btn-primary btn-block">Iniciar sesión</button>
        <hr>
        <p class="text-center">¿No tienes una cuenta? <a href="/usuario/create" class="btn-register text-white">Regístrate aquí</a></p>
      </div>
    </form>
<script type="text/javascript" src="{{ asset('js/bootstrap.js') }}"></script>
<!-- <script src="../../js/LogIn.js"></script> -->
@endsection
