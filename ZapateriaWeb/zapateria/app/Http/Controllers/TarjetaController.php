<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Models\Tarjeta;
use App\Models\User;
use App\Models\Domicilio;
use App\Models\Zapato;
use App\Models\Talla;


class TarjetaController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     */
    public function registrar(Request $request)
    {
        //
        $dataArray=array();
        $dataArray = json_decode($request->input('dataArrayTarjeta'));
        if(!Auth::check()){
            return redirect()->route('login.show');
        }else{
            if(is_null($dataArray)){
                $dataArray=json_decode($request->input('dataArrayTarjeta2'));
            }
            //dd($dataArray);
            $data=$request->all();
            $idUser = $data['idUsuario'];
            $esRegalo = $data['esRegalo'];
            $idTarjeta = $data['idTarjeta'];
            $idDomicilio = $data['idDomicilio'];
            //dd($idTarjeta,$idDomicilio);
            $user = User::where('id','=',$idUser)->first();
            $tarjetas = Tarjeta::where('idUser','=',$idUser)->get();
            $tarjeta = Tarjeta::where('id','=',$idTarjeta)->first();
            return view('registrar.registrarTarjetas',compact('dataArray','user','tarjetas','tarjeta','esRegalo','idDomicilio'));
        }
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        //
        $dataArray=array();
        $dataArray = json_decode($request->input('dataArray'));
        if ($request->has('flexCheckDefault')) {
            // El checkbox está marcado
            $validated = $request->validate([
                'tarjeta'=>'required',
                'numeroTarjeta'=>'required',
                'vencimiento'=>'required',
                'ccv'=>'required' 
            ]);
             
            if(is_null($dataArray)){
                $dataArray=json_decode($request->input('dataArray2'));
            }
            //dd($dataArray,"dataArray2");
            $data=$request->all();
            Tarjeta::create([
                'nombre'=>$data['tarjeta'],
                'numerotarjeta'=>$data['numeroTarjeta'],
                'fecha'=>$data['vencimiento'],
                'ccv'=>$data['ccv'],
                'idUser'=>$data['idUsuario']
            ]);

            $data=$request->all();
            $idUser = $data['idUsuario'];
            $esRegalo = $data['esRegalo'];
            $idTarjeta="";
            if($request->has('idTarjeta2')){
                $idTarjeta=$data['idTarjeta2'];
            }else{
                dd("No existe idDomicilio2");
            }
            $idDomicilio = $data['idDomicilio'];
            $user = User::where('id','=',$idUser)->first();
            $tarjetas = Tarjeta::where('idUser','=',$idUser)->get();
            $tarjeta = Tarjeta::where('id','=',$idTarjeta)->first();
            return view('registrar.registrarTarjetas',compact('dataArray','user','tarjetas','tarjeta','esRegalo','idDomicilio'));

        }else{
            $data=$request->all();
            //dd($data['idTarjeta']);
            $zapatos = array();
            $tallas = array();
            $idUser = $data['idUsuario'];
            $esRegalo = $data['esRegalo'];
            $idTarjeta = $data['idTarjeta'];
            $idDomicilio = $data['idDomicilio'];
            $user = User::where('id','=',$idUser)->first();
            $domicilio = Domicilio::where('id','=',$idDomicilio)->first();
            $tarjeta = Tarjeta::where('id','=',$idTarjeta)->first();
            if(!is_null($dataArray)){
                foreach($dataArray as $datos){
                    array_push($zapatos, Zapato::where('id','=',$datos->idZapato)->first());
                    array_push($tallas, Talla::where('id','=',$datos->idTalla)->first());
                }
            }
            //return redirect()->route('proceder.pago')->with('zapatos','tallas','dataArray','user','esRegalo','domicilio','tarjeta');
            //return redirectToPost('/proceder/pago',compact('zapatos','tallas','dataArray','user','esRegalo','domicilio','tarjeta'));
            return view('pago.procederPago',compact('zapatos','tallas','dataArray','user','esRegalo','domicilio','tarjeta'));
        }
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
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
