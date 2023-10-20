@extends('layouts.app-master')
@section('content')
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro Tarjetas</title>
</head>
<body>
    <br>
    <div class="container-fluid" name='registro'>
        <div class="container-fluid">
            <div class="card">
                <div class="card-header text-center">
                    <h5>Tarjetas Registradas</h5>
                </div>
                <div class="card-body">
                    
                    @if(count($tarjetas)!=0)
                        <form method="post" action="/tarjeta/store" id="formulario2">
                            @csrf
                            <select name="selectorTarjeta" id="selectorTarjeta" class="form-select">
                            @foreach($tarjetas as $key => $t)
                                @php
                                    $ultimosCuatro = substr($t->numerotarjeta, -4);
                                @endphp
                                @if(!is_null($tarjeta))
                                    <option value="{{$t->id}}" @if($t->id == $tarjeta->id) selected @endif> {{$t->nombre}}  -  ({{$ultimosCuatro}})</option>
                                @else
                                    <option value="{{$t->id}}" > {{$t->nombre}}  -  ({{$ultimosCuatro}})</option>
                                @endif
                            @endforeach
                            </select>
                            <br>
                            @auth
                                <input id="idUsuario" name="idUsuario" value="{{auth()->user()->id}}" hidden>
                            @endauth
                            <input id="esRegalo" name="esRegalo" value="{{$esRegalo}}" hidden>
                            <input id="idTarjeta" name="idTarjeta" value="" hidden>
                            <input id="idDomicilio" name="idDomicilio" value="{{$idDomicilio}}" hidden>
                            <input id="myInput" name="dataArray" value="" hidden>
                            <button type='submit' class="btn btn-success" onclick="cargarCarro(event,'0')">Aceptar</button>  
                        </form>
                    @else
                        <form class="d-grid gap-2" action="/proceder/pago" method="post" id="formulario3">
                            @csrf
                            <select name="selectorTarjeta" id="selectorTarjeta" class="form-select" hidden>
                                <option value="-1"></option>
                            </select>
                            <div>
                                <h3 class="h3"> No tienes tarjetas registradas, registra una.</h3>
                                @auth
                                    <input id="idUsuario" name="idUsuario" value="{{auth()->user()->id}}" hidden>
                                @endauth
                                <input id="esRegalo" name="esRegalo" value="{{$esRegalo}}" hidden>
                                <input id="myInput" name="dataArray" value="" hidden>
                                <input id="idTarjeta" name="idTarjeta" value="" hidden>
                                <input id="idDomicilio" name="idDomicilio" value="{{$idDomicilio}}" hidden>
                                <button type="submit" class="btn btn-info" onclick="cargarCarro(event,'2')">Regresar</a>
                            </div>
                        </form>
                    @endif
                    @foreach($dataArray as $key => $data)
                        <input type="text" name="idZapato{{$loop->iteration}}" id="idZapato{{$loop->iteration}}" value="{{$data->idZapato}}" hidden>
                        <input type="text" name="idTalla{{$loop->iteration}}" id="idTalla{{$loop->iteration}}" value="{{$data->idTalla}}" hidden>
                        <input type="text" name="cantidad{{$loop->iteration}}" id="cantidad{{$loop->iteration}}" value="{{$data->cantidad}}" hidden>
                    @endforeach
                    <input type="text" name="iteraciones" id="iteraciones" value="{{count($dataArray)}}" hidden>
                    <hr>
                    @if($errors->any())
                        <div class="alert alert-danger">
                            <ul>
                                @foreach($errors->all() as $error)
                                    <li>{{$error}}</li>
                                @endforeach
                            </ul>
                        </div>
                    @endif
                    <form method="post" action="/tarjeta/store" id="formulario1">
                        @csrf
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="flexCheckDefault" onclick="verificarCheckbox()">
                            <label class="form-check-label" for="flexCheckDefault">Agregar Nueva Tarjeta</label>
                        </div>
                        @auth
                            <input id="idUsuario" name="idUsuario" value="{{auth()->user()->id}}" hidden>
                        @endauth
                        <input id="esRegalo" name="esRegalo" value="{{$esRegalo}}" hidden>
                        <input id="idTarjeta2" name="idTarjeta2" value="" hidden>
                        <input id="idDomicilio" name="idDomicilio" value="{{$idDomicilio}}" hidden>
                        <input id="myInput" name="dataArray" value="" hidden>
                        <input id="myInput2" name="dataArray2" value="" hidden>

                        <div class="row">
                            <div class="col">
                                <h5 class="card-header text-center" >Tarjeta</h5>
                                <div class="row">
                                    <div class="col">
                                        <div class="mb-3">
                                            <label class="form-label" >Nombre Tarjeta:</label>
                                            <input type='text' id='tarjeta' name='tarjeta' class="form-control" value="{{ old('tarjeta') }}"/>
                                        </div>
                                        <div class="mb-3">
                                            <label class="form-label" >Número de la Tajeta:</label>
                                            <input type='text' id='numeroTarjeta' name='numeroTarjeta' class="form-control" value="{{ old('numeroTarjeta') }}"/>
                                        </div>
                                        <div class="mb-3">
                                            <label class="form-label" >Fecha de Vencimiento:</label>
                                            <input type='date' id='vencimiento' name='vencimiento' class="form-control" value="{{ old('vencimiento') }}"/>
                                        </div>
                                        <div class="mb-3">
                                            <label class="form-label" >CCV:</label>
                                            <input type='number' id='ccv' name='ccv' class="form-control" maxlength="3" value="{{ old('ccv') }}"/>
                                        </div>
                                    </div>
                                    <div class="col"></div>
                                    <div class="col"></div>
                                </div>
                                <hr>
                                <button type='submit' id='guardar' class="btn btn-success" onclick="cargarCarro(event,'1')">Registrar Tarjeta</button>  
                                <button type='reset' id='limpiar' class="btn btn-warning">Limpiar Cajas</button> 
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</body>
<script type="text/javascript" src="{{ asset('js/habilitador.js') }}"></script>
<script type="text/javascript" src="{{ asset('js/registrarTarjetas.js') }}"></script>
</html>
@endsection