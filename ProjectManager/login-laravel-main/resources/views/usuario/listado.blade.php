@extends('layouts.app-master')
@section('content')
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{{ asset('css/bootstrap.css')}}">
    <title>Document</title>
</head>
<body>
    @include('usuario.filtro')
    <div id="contenidoTabla">
        @include('usuario.contenido',['usuarios'=>$usuarios])
    </div>
    <script text="text/javascript" src="{{asset('js/controlador.js')}}"></script>
    <script text="text/javascript" src="{{asset('js/bootstrap.js')}}"></script>
</body>
</html>
@endsection