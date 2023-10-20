@extends('layouts.app-master')
@section('content')
  <div class="container">
    <h2>Registrar zapatos</h2>
    @if($errors->any())
            <div class="alert alert-danger">
                <ul>
                    @foreach($errors->all() as $error)
                        <li>{{$error}}</li>
                    @endforeach
                </ul>
            </div>
        @endif
    <form action="/zapatos/{{$zap->id}}"  method="post" enctype="multipart/form-data">
    @method('PUT')
    @csrf
      <div class="form-group">
        <label for="idInput">Codigo de Barras:</label>
        <input type="text" class="form-control" name="codbar" value="{{$zap->id}}" readonly >
      </div>
      <div class="form-group">
        <label for="modeloInput">Modelo:</label>
        <input type="text" class="form-control" name="modelo" value="{{$zap->modelo}}">
      </div>
      <div lass="form-group">
      <div class="form-group">
        <label for="imagenInput" >Imagen Actual del zapato:</label><br>
        <input type="text" class="form-control" name="url" value="{{$zap->url}}" readonly>
        <img src="{{URL::to('/')}}/imagenes/{{$zap->url}}" alt="Imagen del Zapato"  width="300 px" height="300 px" class="mb-8 zoom"/>
      </div>
      <label >Selecciona una Imagen o inserta el URL:</label>
      <input type="file" accept="image/*" name="image" class="form-control" value="{{$zap->url}}">
      </div>
     
      <div class="form-group">
        <label for="materialInput">Material:</label>
        <input type="text" class="form-control" name="material" value="{{$zap->material}}">
      </div>
      <div class="form-group">
        <label for="estiloInput">Estilo:</label>
        <input type="text" class="form-control" name="estilo" value="{{$zap->estilo}}">
      </div>
      <div class="form-group">
        <label for="colorInput">Color:</label>
        <input type="text" class="form-control" name="color" value="{{$zap->color}}">
      </div>
      <button type="submit" class="btn  btn-success mt-3">Modificar</button>
      <a type="submit" href="/zapatos" class="btn btn-dark mt-3">Regresar</a>
    </form>
  </div>
    @endsection

