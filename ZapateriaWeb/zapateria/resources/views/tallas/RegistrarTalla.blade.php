@extends('layouts.app-master')
@section('content')
<body>
  <div class="container">
    <h2>Registrar tallas</h2>
    <form action="/talla" method="POST">
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
        <label for="idInput">ID del zapato:</label>
        <input type="text" class="form-form-control-color " name="idzapato" value="{{$id}}" readonly>
      </div>
      <div class="form-group">
        <label for="precio">Precio:</label>
        <input type="text" class="form-control" name="precio" >
      </div>
      <div class="form-group">
        <label for="talla">Talla:</label>
        <select name="talla" class="form-select">
          @foreach($filtro as $l)
          <option value="{{$l}}">{{$l}}</option>
          @endforeach
      </select>
      </div>
      <div class="form-group">
        <label for="cantidad">Cantidad:</label>
        <input type="text" class="form-control" name="cantidad" >
        </div>
      <button type="submit" class="btn btn-success mt-2" >Registrar</button>
      <a type="submit" href="/talla/listado/{{$id}}" class="btn btn-dark mt-2" >Regresar</a>
</form>
</body>
    @endsection