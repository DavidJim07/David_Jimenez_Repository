<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Models\Zapato;
use App\Models\Talla;
use App\Models\User;
use App\Models\Domicilio;
use App\Models\Tarjeta;
use App\Models\Pedido;
use App\Models\RenglonPedido;

class VentaProducto extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index(Request $request)
    {
        //
        if(!Auth::check()){
            return redirect()->route('login.show');
        }else{

            return view('pago.ventaProducto');
        }
    }

    public function procederPago(Request $request)
    {
        //
        $dataArray = json_decode($request->input('dataArray'));
        //dd($dataArray,"store");
        if(!Auth::check()){
            return redirect()->route('login.show');
        }else{
            //dd($request->hasAny(['idTarjeta']));
            if ($request->hasAny(['idTarjeta', 'idDomicilio'])) {
                // Al menos uno de los parámetros está presente en la solicitud
                $zapatos = array();
                $tallas = array();
                $data=$request->all();
                $idUser = $data['idUsuario'];
                $esRegalo = $data['esRegalo'];
                $user = User::where('id','=',$idUser)->first();
                $domicilio = Domicilio::where('id','=',$data['idDomicilio'])->first();
                $tarjeta = Tarjeta::where('id','=',$data['idTarjeta'])->first();
                if(!is_null($dataArray)){
                    foreach($dataArray as $datos){
                        array_push($zapatos, Zapato::where('id','=',$datos->idZapato)->first());
                        array_push($tallas, Talla::where('id','=',$datos->idTalla)->first());
                    }
                }
                return view('pago.procederPago',compact('zapatos','tallas','dataArray','user','esRegalo','domicilio','tarjeta'));
            } else {
                // Ninguno de los parámetros está presente en la solicitud
                $zapatos = array();
                $tallas = array();
                $data=$request->all();
                $idUser = $data['idUsuario'];
                $esRegalo ="0";
                if ($request->hasAny(['esRegalo'])){
                    $esRegalo = $data['esRegalo'];
                }
                $user = User::where('id','=',$idUser)->first();
                $domicilio = Domicilio::where('idUser','=',$idUser)->first();
                $tarjeta = Tarjeta::where('idUser','=',$idUser)->first();
                if(!is_null($dataArray)){
                    foreach($dataArray as $datos){
                        array_push($zapatos, Zapato::where('id','=',$datos->idZapato)->first());
                        array_push($tallas, Talla::where('id','=',$datos->idTalla)->first());
                    }
                }
                return view('pago.procederPago',compact('zapatos','tallas','dataArray','user','esRegalo','domicilio','tarjeta'));
            }
        }
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $dataArray = json_decode($request->input('dataArray'));
        //dd($dataArray,"store");
        if(!Auth::check()){
            return redirect()->route('login.show');
        }else{
            $zapatos = array();
            $tallas = array();
            if(!is_null($dataArray)){
                foreach($dataArray as $datos){
                    array_push($zapatos, Zapato::where('id','=',$datos->idZapato)->first());
                    array_push($tallas, Talla::where('id','=',$datos->idTalla)->first());
                }
            }
            return view('pago.ventaProducto',compact('zapatos','tallas','dataArray'));
        }
    }

    public function realizarPedido(Request $request)
    {
        $dataArray = json_decode($request->input('dataArray3'));
        //dd($request->input('idUsuario'));
        if(!Auth::check()){
            return redirect()->route('login.show');
        }else{
            $zapatos = array();
            $tallas = array();
            $cantidades = array();
            if(!is_null($dataArray)){
                foreach($dataArray as $datos){
                    array_push($zapatos, Zapato::where('id','=',$datos->idZapato)->first());
                    array_push($tallas, Talla::where('id','=',$datos->idTalla)->first());
                    array_push($cantidades, $datos->cantidad);
                }
            }
            //dd($zapatos,$tallas,$cantidades);
            $cont=0;
            foreach($tallas as $talla){
                $talla=Talla::where('id','=',$talla->id)->first();
                $talla->cantidad=$talla->cantidad-$cantidades[$cont];
                $talla->save();
                $cont=$cont+1;
            }
            $pedido = new Pedido();
            $pedido->cantidad=$cont;
            $pedido->subtotal=$request->input('subtotal3');
            $pedido->fechaPedido=date('Y-m-d');
            $pedido->idUser=$request->input('idUsuario');
            $pedido->idDomicilio=$request->input('idDomicilio');
            $pedido->idTarjeta=$request->input('idTarjeta');
            $pedido->save();

            $pedidoId = $pedido->id;

            $cont=0;
            foreach($tallas as $talla){
                $renglonPedido=new RenglonPedido();
                $renglonPedido->cantidad=$cantidades[$cont];
                $renglonPedido->idTalla=$talla->id;
                $renglonPedido->idZapato=$zapatos[$cont]->id;
                $renglonPedido->idPedido=$pedidoId;
                $renglonPedido->save();
                $cont=$cont+1;
            }            
            return redirect("/pedidos");
        }
    }
    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
        $dataArray = json_decode($request->input('dataArray'));
        if(!Auth::check()){
            return redirect()->route('login.show');
        }else{
            $zapatos = array();
            $tallas = array();
            if(!is_null($dataArray)){
                foreach($dataArray as $datos){
                    array_push($zapatos, Zapato::where('id','=',$datos->idZapato)->first());
                    array_push($tallas, Talla::where('id','=',$datos->idTalla)->first());
                }
            }
            return view('pago.ventaProducto',compact('zapatos','tallas','dataArray'));
        }
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
