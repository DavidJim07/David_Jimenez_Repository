@extends('layouts.app-master')
@section('content')
  <div class="container-fluid">
    <h2>Registrar zapatos</h2>
    <form action="/zapatos"  method="post" enctype="multipart/form-data">
    @if($errors->any())
            <div class="alert alert-danger">
                <ul>
                    @foreach($errors->all() as $error)
                        <li>{{$error}}</li>
                    @endforeach
                </ul>
            </div>
        @endif
    @csrf
      <div class="form-group">
        <label for="idInput">Codigo de Barras:</label>
        <input type="text" class="form-control" name="codbar" >
      </div>
      <div class="form-group">
        <label >Modelo:</label>
        <input type="text" class="form-control" name="modelo" >
      </div>
      
      <div lass="form-group">
      <label >Selecciona una Imagen o inserta el URL:</label>
      <input type="file" accept="image/*" name="image" class="form-control" >
      </div>
     
      <div class="form-group">
        <label for="materialInput">Material:</label>
        <input type="text" class="form-control" name="material" >
      </div>
      <div class="form-group">
        <label for="estiloInput">Estilo:</label>
        <input type="text" class="form-control" name="estilo" >
      </div>
      <div class="form-group">
        <label for="colorInput">Color:</label>
        <input type="text" class="form-control" name="color" >
      </div>
      <button type="submit" class="btn btn-primary mt-3">Guardar</button>
      <a type="submit" href="/zapatos" class="btn btn-danger mt-3">Cancelar</a>
    </form>
  </div>
    @endsection
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>

