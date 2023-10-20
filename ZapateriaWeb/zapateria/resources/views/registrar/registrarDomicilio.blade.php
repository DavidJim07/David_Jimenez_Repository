@extends('layouts.app-master')
@section('content')
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registro Domicilio</title>
</head>
<body>
    <br>
    <div class="container-fluid" name='registro'>
        <div class="container-fluid">
            <div class="card">
                <div class="card-header text-center">
                    <h5>Domicilios Registrados</h5>
                </div>
                <div class="card-body">
                    @if(count($domicilios)!=0)
                        <form method="post" action="/domicilio/store" id="formulario2">
                            @csrf
                            <select name="selectorDomiclio" id="selectorDomiclio" class="form-select">
                            @foreach($domicilios as $key => $d)
                                <option value="{{$d->id}}" @if($d->id == $domicilio->id) selected @endif> {{$d->calle}} #{{$d->numext}}, {{$d->colonia}} {{$d->ciudad}}, {{$d->estado}}, {{$d->pais}}</option>
                            @endforeach
                            </select>
                            <br>
                            @auth
                                <input id="idUsuario" name="idUsuario" value="{{auth()->user()->id}}" hidden>
                            @endauth
                            <input id="esRegalo" name="esRegalo" value="{{$esRegalo}}" hidden>
                            <input id="idTarjeta" name="idTarjeta" value="{{$idTarjeta}}" hidden>
                            <input id="idDomicilio" name="idDomicilio" value="" hidden>
                            <input id="myInput" name="dataArray" value="" hidden>
                            <button type='submit' class="btn btn-success" onclick="cargarCarro(event,'0')">Aceptar</button>  
                        </form>
                    @else
                        <form class="d-grid gap-2" action="/proceder/pago" method="post">
                            @csrf
                            <div>
                                <h3 class="h3"> No tienes domicilios registradas, registra una.</h3>
                                @auth
                                    <input id="idUsuario" name="idUsuario" value="{{auth()->user()->id}}" hidden>
                                @endauth
                                <input id="esRegalo" name="esRegalo" value="{{$esRegalo}}" hidden>
                                <input id="myInput" name="dataArray" value="" hidden>
                                <input id="idTarjeta" name="idTarjeta" value="{{$idTarjeta}}" hidden>
                                <input id="idDomicilio" name="idDomicilio" value="" hidden>
                                <button type="submit" class="btn btn-info" onclick="cargarCarro(event,'0')">Regresar</a>
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
                    <form method="post" action="/domicilio/store" id="formulario1">
                        @csrf
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" name="flexCheckDefault" onclick="verificarCheckbox()">
                            <label class="form-check-label" for="flexCheckDefault">Agregar Nuevo Domicio</label>
                        </div>
                        @auth
                            <input id="idUsuario" name="idUsuario" value="{{auth()->user()->id}}" hidden>
                        @endauth
                        <input id="esRegalo" name="esRegalo" value="{{$esRegalo}}" hidden>
                        <input id="idTarjeta" name="idTarjeta" value="{{$idTarjeta}}" hidden>
                        <input id="idDomicilio2" name="idDomicilio2" value="" hidden>
                        <input id="myInput" name="dataArray" value="" hidden>
                        <input id="myInput2" name="dataArray2" value="" hidden>

                        <div class="row">
                            <div class="col">
                                <h5 class="card-header text-center" >Domicilio</h5>
                                <div class="row">
                                    <div class="col">
                                        <div class="mb-3">
                                            <label class="form-label" >Pais:</label>
                                            <input type='text' id='pais' name='pais' class="form-control" value="{{ old('pais') }}"/>
                                        </div>
                                        <div class="mb-3">
                                            <label class="form-label" >Estado:</label>
                                            <input type='text' id='estado' name='estado' class="form-control" value="{{ old('estado') }}"/>
                                        </div>
                                        <div class="mb-3">
                                            <label class="form-label" >Ciudad:</label>
                                            <input type='text' id='ciudad' name='ciudad' class="form-control" value="{{ old('ciudad') }}"/>
                                        </div>
                                        <div class="mb-3">
                                            <label class="form-label" >Colonia:</label>
                                            <input type='text' id='colonia' name='colonia' class="form-control" value="{{ old('colonia') }}"/>
                                        </div>
                                    </div>
                                    <div class="col">
                                        <div class="mb-3">
                                            <label class="form-label" >Codigo Postal:</label>
                                            <input type='text' id='codigoPostal' name='codigoPostal' class="form-control" value="{{ old('codigoPostal') }}"/>
                                        </div>
                                        <div class="mb-3">
                                            <label class="form-label" >Calle:</label>
                                            <input type='text' id='calle' name='calle' class="form-control" value="{{ old('calle') }}"/>
                                        </div>
                                        <div class="mb-3">
                                            <label class="form-label" >Numero:</label>
                                            <input type='number' id='numero' name='numero' class="form-control" value="{{ old('numero') }}"/>
                                        </div>
                                        <div class="mb-3">
                                            <label class="form-label" >EntreCalles:</label>
                                            <input type='text' id='entreCalles' name='entreCalles' class="form-control" value="{{ old('entreCalles') }}"/>
                                        </div>
                                    </div>
                                </div>
                                <hr>
                                <button type='submit' id='guardar' class="btn btn-success" onclick="cargarCarro(event,'1')">Registrar Domicilio</button>  
                                <button type='reset' id='limpiar' class="btn btn-warning">Limpiar Cajas</button> 
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</body>
<script type="text/javascript" src="{{ asset('js/registrarDomicilio.js') }}"></script>
<script type="text/javascript" src="{{ asset('js/habilitadorDomicilio.js') }}"></script>
</html>
    @endsection