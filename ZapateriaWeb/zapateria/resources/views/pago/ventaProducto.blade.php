@extends('layouts.app-master')
@section('content')
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Venta Producto</title>
</head>
<body>
    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-8">
                <div class="container-fluid">
                    <div class="card">
                        <form class="card-header" action="/venta/producto" method="post" id="formularioBorrar">
                            <h1 class="h1">Carrito</h1>
                            @csrf
                            @if(count($zapatos)!=0)
                                <button class="btn btn-link" type="submit" onclick="vaciarCarrito(event)">Deseleccionar todos los artículos </button>
                            @endif
                        </form>
                        <div class="card-body">
                            <div class="container-fluid">
                                <div class="row g-4" id="contenedorCarrito" name="contenedorCarrito">
                                    @if(count($zapatos)!=0)
                                    @foreach($zapatos as $key => $z)
                                        <div class="col" id="contenedor{{$loop->iteration}}">
                                            <div class="card" style="width: 18rem;">
                                                <div class="p-3">
                                                    <img src="{{URL::to('/')}}/imagenes/{{$z->url}}" class="img-thumbnail" alt="Aqui va la imagen del producto">
                                                    <h5 class="card-title text-center">{{$z->modelo}}</h5>
                                                    <p class="card-text">
                                                        <ul>
                                                            <li>{{$z->estilo}}</li>
                                                            <li>{{$z->color}}</li>
                                                            <li>{{$z->material}}</li>
                                                            <li>{{$tallas[$key]->talla}}</li>
                                                            <li id="total{{$loop->iteration}}"></li>
                                                        </ul>
                                                    </p>
                                                    <div class="row">
                                                        <div class="col">
                                                            <button class="btn btn-danger" onclick="quitar('{{$loop->iteration}}')" >Quitar</button>
                                                        </div>
                                                        <div class="col">
                                                            <h6 class="h6">Cantidad:</h6>
                                                        </div>
                                                        <div class="col">
                                                            <select name="talla" class="form-select" onchange="opcionAlterada('{{$loop->iteration}}','1')" id="{{$loop->iteration}}">
                                                                @for($i = 1; $i <= $tallas[$key]->cantidad; $i++)
                                                                    <option value="{{$tallas[$key]->precio}}" @if($i == $dataArray[$key]->cantidad) selected @endif>{{ $i }}</option>
                                                                @endfor
                                                            </select>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <input type="text" name="opcionDefecto{{$loop->iteration}}" id="opcionDefecto{{$loop->iteration}}" value="{{$dataArray[$key]->cantidad}}" hidden>

                                            <input type="text" name="idZapato{{$loop->iteration}}" id="idZapato{{$loop->iteration}}" value="{{$z->id}}" hidden>
                                            
                                            <input type="text" name="idTalla{{$loop->iteration}}" id="idTalla{{$loop->iteration}}" value="{{$tallas[$key]->id}}" hidden>
                                        </div>
                                    @endforeach
                                    @else
                                        <div>
                                            <h3 class="h3"> No tienes productos en tú carrito</h3>
                                            <a href="/" class="btn btn-info">Regresar</a>
                                        </div>
                                    @endif
                                    <input type="text" name="iteraciones" id="iteraciones" value="{{count($zapatos)}}" hidden>

                                </div>
                            </div>
                        </div>
                        <hr>
                        <div class="container-fluid" style="text-align: right;"><strong id="subtotal" name="subtotal"></strong></div>
                    </div>
                </div>
            </div>
            @if(count($zapatos)!=0)
            <div class="col">
                <div class="container-fluid">
                    <div class="card">
                        <div class="card-body">
                            <p class="card-text" id="tipoEnvio" name="tipoEnvio">Tu pedido es con envio gratis o mostrar el costo del envio</p>
                            <strong id="subtotal2" name="subtotal2"></strong>
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                                <label class="form-check-label" for="flexCheckDefault" id="regalo">Es un regalo</label>
                            </div>
                            <hr>
                            <form class="d-grid gap-2" action="/proceder/pago" method="post">
                                @csrf
                                @auth
                                    <input id="idUsuario" name="idUsuario" value="{{auth()->user()->id}}" hidden>
                                @endauth
                                <input id="esRegalo" name="esRegalo" value="" hidden>
                                <input id="myInput" name="dataArray" value="" hidden>
                                <button type="submit" class="btn btn-warning text-center" onclick="pagar()">Proceder a pagar</a>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            @endif
        </div>
    </div>
    <br><br>
</body>
</html>
<script type="text/javascript" src="{{ asset('js/ventaProducto.js') }}"></script>
    @endsection

