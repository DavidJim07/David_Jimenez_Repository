@extends('layouts.app-master')
@section('content')
<body>
  <div class="container">
    <h2>Registrar zapatos</h2>
    <form action="/zapatos"  method="post" >
    
      <div class="form-group">
        <label for="idInput">Codigo de Barras:</label>
        <input type="text" class="form-control" name="codbar"  value="{{$zap->id}}" readonly>
      </div>
      <div class="form-group">
        <label for="modeloInput">Modelo:</label>
        <input type="text" class="form-control" name="modelo" value="{{$zap->modelo}}" readonly>
      </div>
      <div class="form-group">
        <label for="imagenInput" >Imagen del zapato:</label><br>
        <img src="{{URL::to('/')}}/imagenes/{{$zap->url}}" alt="Imagen del Zapato"  width="300 px" height="300 px" class="mb-8 zoom"/>
      </div>
     
      <div class="form-group">
        <label for="materialInput">Material:</label>
        <input type="text" class="form-control" name="material"value="{{$zap->material}}" readonly>
      </div>
      <div class="form-group">
        <label for="estiloInput">Estilo:</label>
        <input type="text" class="form-control" name="estilo"value="{{$zap->estilo}}" readonly>
      </div>
      <div class="form-group">
        <label for="colorInput">Color:</label>
        <input type="text" class="form-control" name="color"value="{{$zap->color}}" readonly>
      </div>
      <a type="submit" href="/zapatos" class="btn btn-dark mt-3">Regresar</a>
    </form>
  </div>
</body>
    @endsection

