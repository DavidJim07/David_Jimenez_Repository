@extends('layouts.app-master')
@section('content')
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proceder Pago</title>
</head>
<body>
    <br>
    <div class="alert alert-secondary text-center" role="alert">
        <h2 class="h2" id="titulo" name="titulo">Proceder a Pago(CantidadArtículos)</h2>
    </div>
    <div class="row" >
        <div class="col-8">
            <div class="container-fluid" >
                <table class="table table-striped" style="background: white">
                    <tr>
                        <th scope="row"><h2>1</h2></th>
                        <td colspan="-1"><h2>Dirección De Envió</h2></td>
                        <td><div id="nombrePersona" name="nombrePersona">{{$user->name}} {{$user->paterno}} {{$user->materno}}</div> 
                            <div id="calleYNumero" name="calleYNumero">{{$domicilio->calle}} #{{$domicilio->numext}}</div> 
                            <div id="colonia" name="colonia">{{$domicilio->colonia}}</div> 
                            <div id="ciudadYEstado" name="ciudadYEstado">{{$domicilio->ciudad}}, {{$domicilio->estado}}, {{$domicilio->pais}}</div> 
                            <div id="codigoPostal" name="codigoPostal">{{$domicilio->codpost}}</div> 
                        </td>
                        <td>
                            <form class="d-grid gap-2" action="/domicilio/create" method="post">
                                @csrf
                                <div class="d-grid gap-2">
                                    @auth
                                        <input id="idUsuario" name="idUsuario" value="{{auth()->user()->id}}" hidden>
                                    @endauth
                                    <input id="esRegalo" name="esRegalo" value="{{$esRegalo}}" hidden>
                                    @if($tarjeta!=null  )
                                        <input id="idTarjeta" name="idTarjeta" value="{{$tarjeta->id}}" hidden>
                                    @else
                                        <input id="idTarjeta" name="idTarjeta" value="-1" hidden>
                                    @endif
                                    <input id="idDomicilio" name="idDomicilio" value="{{$domicilio->id}}" hidden>
                                    <input id="myInputTarjeta" name="dataArrayTarjeta" value="" hidden>
                                    <button type="submit" class="btn btn-link" onclick="registrarTarjeta('0')">Cambiar</a>
                                </div>
                            </form>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row"><h2>2</h2></th>
                        <td colspan="-1"><h2>Método de Pago</h2></td>
                        @if($tarjeta!=null  )
                            @php
                                $ultimosCuatro = substr($tarjeta->numerotarjeta, -4);
                            @endphp
                            <td><div id="nombreTarjeta" name="nombreTarjeta">{{$tarjeta->nombre}} con la terminación ('{{$ultimosCuatro}}')</div></td>
                        @else
                            <td><h4 class="h4">No hay tarjetas registradas</h4></td>
                        @endif
                        <td>
                            <form class="d-grid gap-2" action="/tarjeta/create" method="post">
                                @csrf
                                <div class="d-grid gap-2">
                                    @auth
                                        <input id="idUsuario" name="idUsuario" value="{{auth()->user()->id}}" hidden>
                                    @endauth
                                    <input id="esRegalo" name="esRegalo" value="{{$esRegalo}}" hidden>
                                    <input id="myInputTarjeta2" name="dataArrayTarjeta2" value="" hidden>
                                    @if($tarjeta!=null  )
                                        <input id="idTarjeta" name="idTarjeta" value="{{$tarjeta->id}}" hidden>
                                    @else
                                        <input id="idTarjeta" name="idTarjeta" value="-1" hidden>
                                    @endif
                                    <input id="idDomicilio" name="idDomicilio" value="{{$domicilio->id}}" hidden>
                                    <button type="submit" class="btn btn-link" onclick="registrarTarjeta('1')">Cambiar</a>
                                </div>
                            </form>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row"><h2>3</h2></th>
                        <td colspan="4"><h2>Revisar artículos y envíos</h2></td>
                    </tr>
                    <tr>
                        <td colspan="4">
                            <div class="container-fluid">
                                <div class="card">
                                    <div class="card-body">
                                        <div class="row" id="contenedorProductos" name="contenedorProductos">
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
                                            @endif
                                            <input type="text" name="iteraciones" id="iteraciones" value="{{count($zapatos)}}" hidden>
                                            <form class="card-header" action="/venta/producto" method="post" id="formularioBorrar">@csrf</form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </td>
                    </tr>
                </table>
                <br>
                <div class="container-fluid">
                    <div class="card">
                        <div class="card-body">
                            <div class="row">
                                <div class="col"></div>
                                <div class="col" style="text-align: right;"><strong id="subtotal" name="subtotal"></strong></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div  class="col">
            <div class="container-fluid">
                <div class="card">
                    <div class="card-body">
                        <form class="d-grid gap-2" action="/confirmar/pedido" method="post">
                            @csrf
                            <div class="d-grid gap-2">
                                @auth
                                    <input id="idUsuario" name="idUsuario" value="{{auth()->user()->id}}" hidden>
                                @endauth
                                <input id="myInput3" name="dataArray3" value="" hidden>
                                <input id="subtotal3" name="subtotal3" value="" hidden>
                                <input id="idDomicilio" name="idDomicilio" value="{{$domicilio->id}}" hidden>
                                @if($tarjeta!=null  )
                                    <button type="submit" class="btn btn-warning text-center" onclick="pagar()">Proceder a pagar</button>
                                    <input id="idTarjeta" name="idTarjeta" value="{{$tarjeta->id}}" hidden>
                                @else
                                    <button type="submit" class="btn btn-warning text-center" onclick="pagar()" disabled>Proceder a pagar</button>
                                    <input id="idTarjeta" name="idTarjeta" value="-1" hidden>
                                @endif
                            </div>
                        </form>
                        <p class="card-text text-center">Al realizar tu pedido aceptas los <a href="#">terminos y condiciones</a></p>
                        <hr>
                        <div class="text-center">
                            <strong>Confirmación del Pedido</strong><br>
                        </div>
                        <div>
                            <div class="row">
                                <div class="col">Productos:</div>
                                <div class="col" style="text-align: right;" id="totalProductos" name="totalProductos">Holaa</div>
                            </div>
                            <div class="row">
                                <div class="col">Envio:</div>
                                <div class="col" style="text-align: right;" id="totalEnvio" name="totalEnvio">$0</div>
                            </div>
                            <div class="row">
                                <div class="col">Promociones:</div>
                                <div class="col" style="text-align: right;" id="totalPromociones" name="totalPromociones">Ninguna</div>
                            </div>
                        </div>
                        <hr>
                        <div class="row">
                            @if($esRegalo==1)
                                <div class="col"id="totalPromociones" name="totalPromociones">Es un regalo</div>
                            @endif
                            <div class="col" style="text-align: right;" ><strong id="subtotal2" name="subtotal2"></strong></div>
                        </div>
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
<script type="text/javascript" src="{{ asset('js/procederPago.js') }}"></script>
@endsection