@extends('layouts.app-master')
@section('content')
    <div class="row">
        <div class="col">
            <div class="row" id="contenedorCarro">
                @foreach($zapatos as $z)
                    <div class="col" >
                        <div class="card" style="width: 18rem;">
                            <div class="p-3">
                                <img src="{{URL::to('/')}}/imagenes/{{$z->url}}" class="card-img-top" alt="Aqui va la imagen del producto">
                                <h5 class="card-title text-center">{{$z->modelo}}</h5>
                                <p class="card-text text-center">
                                    <ul>
                                        <li>{{$z->estilo}}</li>
                                        <li>{{$z->color}}</li>
                                        <li>{{$z->material}}</li>
                                        <li id="cantidad{{$loop->iteration}}"></li>
                                        <li id="precio{{$loop->iteration}}"></li>
                                    </ul>
                                </p>
                                <div class="row">
                                    <div class="col">
                                        <button class="btn btn-danger" onclick="agregarAlCarrito('{{$loop->iteration}}','{{$z->id}}')" id="agregar{{$loop->iteration}}">Agregar</button>
                                    </div>
                                    <div class="col">
                                        <h6 class="h6">Tallas:</h6>
                                    </div>
                                    <div class="col">
                                        <select class="form-select" onchange="opcionAlterada('{{$loop->iteration}}')" id="{{$loop->iteration}}">
                                            @foreach($total as $t)
                                                @if($t->id==$z->id)
                                                    <option value="{{$t->cantidad}}*{{$t->precio}}*{{$t->idTalla}}*{{$z->id}}">{{$t->talla}}</option>
                                                @endif
                                            @endforeach
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <input type="text" name="modelo{{$z->id}}" id="modelo{{$z->id}}" value="{{$z->modelo}}" hidden>
                @endforeach
                <input type="text" name="iteraciones" id="iteraciones" value="{{count($zapatos)}}" hidden>
            </div>
        </div>
        <div class="col">
            <div class="row">
                <div class="col">
                    <main id="items" class="col-sm-8 row"></main>
                    <aside class="col-sm-8 custom-carrito">
                        <h2>Carrito</h2>
                        <div class="row">
                            <div class="col">Modelo:</div>
                            <div class="col">Cantidad:</div>
                            <div class="col">Precio:</div>
                            <div class="col">Talla:</div>
                            <div class="col">ELIMINAR</div>
                        </div>
                        <ul id="carrito" class="list-group"></ul>
                        <hr>
                        <p class="text-right">Total: &dollar;<span id="total"></span></p>
                        <form action="/venta/producto" method="post">
                            @csrf
                            <input id="myInput" name="dataArray" value="" hidden>
                            <button class="btn btn-warning" type="submit">Pagar</a>
                        </form>
                    </aside>
                </div>
            </div>
        </div>
    </div>
<script type="text/javascript" src="{{ asset('js/Carrito.js') }}"></script>
    @endsection