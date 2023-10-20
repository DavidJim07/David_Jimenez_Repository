@extends('layouts.app-master')
@section('content')

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    @if($errors->any())
        <div class="alert alert-danger">
            <ul>
                @foreach($errors->all() as $error)
                    <li>{{$error}}</li>
                @endforeach
            </ul>
        </div>
    @endif
    <br>
    <form action="/imagen/create" method="POST" enctype="multipart/form-data">
    @csrf
    <br>
    <div class="mb-3">
        <label class="col-form-label-lg">Actividad:</label>
        <div class="mb-3">
            <label class="col-form-label-lg">{{$relacion->actividad->descripcion}}</label>
        </div>
        <label class="col-form-label-lg">Usuario:</label>
        <div class="mb-3">
            <label class="col-form-label-lg">{{$relacion->user->name}} {{$relacion->user->paterno}} {{$relacion->user->materno}}</label>
            <input type="text" value="{{$relacion->id}}" name="id_relacion" hidden>
        </div>
    </div>
    <input multiple type="file" accept="imagenes/*" name="imagenes[]" class="form-control-file" >
    <br>
    <br><br>
    <a  class="btn btn-primary" href="/actividad">Regresar</a>
    <button type="submit" class="btn btn-success">Guardar archivo</button>
    </form>
</body>
</html>
@endsection