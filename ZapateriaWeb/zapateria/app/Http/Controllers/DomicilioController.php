<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Models\Domicilio;
use App\Models\Tarjeta;
use App\Models\Zapato;
use App\Models\Talla;
use App\Models\User;

class DomicilioController extends Controller
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
    public function create(Request $request)
    {
        //
        $dataArray = json_decode($request->input('dataArrayTarjeta'));
        //dd($dataArray,"create");
        if(!Auth::check()){
            return redirect()->route('login.show');
        }else{
            $data=$request->all();
            $idUser = $data['idUsuario'];
            $esRegalo = $data['esRegalo'];
            $idTarjeta = $data['idTarjeta'];
            $idDomicilio = $data['idDomicilio'];
            //dd($idTarjeta,$idDomicilio);
            $user = User::where('id','=',$idUser)->first();
            $domicilios = Domicilio::where('idUser','=',$idUser)->get();
            $domicilio = Domicilio::where('id','=',$idDomicilio)->first();
            return view('registrar.registrarDomicilio',compact('dataArray','user','domicilios','domicilio','esRegalo','idTarjeta'));
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
            $validated = $request->validate([
                'pais'=>'required',
                'estado'=>'required',
                'ciudad'=>'required',
                'colonia'=>'required',
                'codigoPostal'=>'required',
                'calle'=>'required',
                'numero'=>'required',
                'entreCalles'=>'required',
            ]);
            
            if(is_null($dataArray)){
                $dataArray=json_decode($request->input('dataArray2'));
            }
            //dd($dataArray,"dataArray2");
            $data=$request->all();

            $domicilio = new Domicilio();
            $domicilio->pais = $data['pais'];
            $domicilio->estado = $data['estado'];
            $domicilio->ciudad = $data['ciudad'];
            $domicilio->codpost = $data['codigoPostal'];
            $domicilio->colonia = $data['colonia'];
            $domicilio->calle = $data['calle'];
            $domicilio->numext = $data['numero'];
            $domicilio->entrecalle = $data['entreCalles'];
            $domicilio->idUser = $data['idUsuario'];
            $domicilio->save();

            $idUser = $data['idUsuario'];
            $esRegalo = $data['esRegalo'];
            $idTarjeta = $data['idTarjeta'];
            $idDomicilio="";
            if($request->has('idDomicilio2')){
                $idDomicilio=$data['idDomicilio2'];
            }else{
                dd("No existe idDomicilio2");
            }
            $user = User::where('id','=',$idUser)->first();
            $domicilios = Domicilio::where('idUser','=',$idUser)->get();
            //dd($idDomicilio);
            $domicilio = Domicilio::where('id','=',$idDomicilio)->first();
            return view('registrar.registrarDomicilio',compact('dataArray','user','domicilios','domicilio','esRegalo','idTarjeta'));
        }else{
            // El checkbox no está marcado
            //dd("Acción para cargar el domicilio seleccionado");
            $data=$request->all();
            //dd($data['idTarjeta']);
            $zapatos = array();
            $tallas = array();
            $idUser = $data['idUsuario'];
            $esRegalo = $data['esRegalo'];
            $idTarjeta = $data['idTarjeta'];
            $idDomicilio = $data['idDomicilio'];
            //dd($idTarjeta,$idDomicilio);
            $user = User::where('id','=',$idUser)->first();
            $domicilio = Domicilio::where('id','=',$idDomicilio)->first();
            $tarjeta = Tarjeta::where('id','=',$idTarjeta)->first();
            if(!is_null($dataArray)){
                foreach($dataArray as $datos){
                    array_push($zapatos, Zapato::where('id','=',$datos->idZapato)->first());
                    array_push($tallas, Talla::where('id','=',$datos->idTalla)->first());
                }
            }
           // return redirect()->route('/proceder/pago')->with(compact('zapatos','tallas','dataArray','user','esRegalo','domicilio','tarjeta'));
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
