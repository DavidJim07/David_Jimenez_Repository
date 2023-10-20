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
        <h2 class="h2" id="titulo" name="titulo">Pedidos de {{$usuario->name}} {{$usuario->paterno}} {{$usuario->materno}}</h2>
    </div>
    <div class="container-fluid">
        <div class="row">
            <div class="col">
                <div class="card">
                    @if(count($pedidos)!=0)
                        <table class="table">
                            <thead class="table-primary">
                                <tr>
                                <th scope="col">#</th>
                                <th scope="col">Productos</th>
                                <th scope="col">Total</th>
                                <th scope="col">Fecha</th>
                                <th scope="col">Domicilio</th>
                                <th scope="col">Tarjeta</th>
                                <th scope="col">Acción</th>
                                </tr>
                            </thead>
                            <tbody>
                                @foreach($pedidos as $key => $p)
                                <tr>
                                    <th scope="row">{{$loop->iteration}}</th>
                                    <td>{{$p->cantidad}}</td>
                                    <td>{{$p->subtotal}}</td>
                                    <td>{{$p->fechaPedido}}</td>
                                    <td>{{$domicilios[$key]->calle}} #{{$domicilios[$key]->numext}}, Col. {{$domicilios[$key]->colonia}}
                                        {{$domicilios[$key]->ciudad}} {{$domicilios[$key]->Estado}}
                                    </td>
                                    @php
                                        $ultimosCuatro = substr($tarjetas[$key]->numerotarjeta, -4);
                                    @endphp
                                    <td>{{$tarjetas[$key]->nombre}} con la terminación ('{{$ultimosCuatro}}')</td>
                                    <td>Consultar Pedido</td>
                                </tr>
                                @endforeach
                            </tbody>
                        </table>
                    @else
                        <div class="container"  style="background:white">
                            <div>
                                <h3 class="h3"> No tienes pedidos registrados</h3>
                                <a href="/" class="btn btn-info">Regresar</a>
                            </div>
                        </div>
                    @endif
                </div>
            </div>
        </div>
    </div>
</body>
</html>
@endsection