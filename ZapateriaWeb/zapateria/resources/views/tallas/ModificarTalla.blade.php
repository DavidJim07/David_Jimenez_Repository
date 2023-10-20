@extends('layouts.app-master')
@section('content')
<body>
  <div class="container">
    <h2>Registrar tallas</h2>
    <form action="/talla/{{$zap->id}}" method="POST">
    @if($errors->any())
            <div class="alert alert-danger">
                <ul>
                    @foreach($errors->all() as $error)
                        <li>{{$error}}</li>
                    @endforeach
                </ul>
            </div>
        @endif
        @method('PUT')
    @csrf
      <div class="form-group">
        <label for="idInput">ID del zapato:</label>
        <input type="text" class="form-form-control-color " name="idzapato" value="{{$zap->idzapato}}" readonly>
      </div>
      <div class="form-group">
        <label for="precio">Precio:</label>
        <input type="text" class="form-control" name="precio" value="{{$zap->precio}}" >
      </div>
      <div class="form-group">
        <label for="talla">Nueva talla:</label>
        <select name="talla" class="form-select">
          <option value="{{$zap->talla}}">{{$zap->talla}}</option>
          @foreach($filtro as $l)
          <option value="{{$l}}">{{$l}}</option>
          @endforeach
      </select>
      </div>
      <div class="form-group">
        <label for="cantidad">Cantidad:</label>
        <input type="text" class="form-control" name="cantidad" value="{{$zap->precio}}">
        </div>
      <button type="submit" class="btn btn-success mt-2" >Modificar</button>
      <a type="submit" href="/talla/listado/{{$zap->idzapato}}" class="btn btn-dark mt-2" >Regresar</a>
</form>
</body>
    @endsection