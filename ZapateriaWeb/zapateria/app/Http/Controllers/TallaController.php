<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Zapato;
use App\Models\Talla;
use Illuminate\Support\Facades\DB;

class TallaController extends Controller
{
  
    public function index(String $id)
    {
        $zp = Talla::where('idzapato','=', $id)->where('estado','=','1')->get();
         
        return view('tallas.ListarTalla',compact('zp','id'));
    }
    
    public function create(String $id)
    {
        $talla=array();
        $exist=array();
        $total=DB::select('SELECT  talla from talla where idzapato='.$id);
        for ($i = 0; $i < count($total); ++$i){array_push($exist,$total[$i]->talla);}
        for ($i=20; $i <=31 ; $i++) {array_push($talla,$i);}
        $filtro=array_diff($talla,$exist);        
        return view('tallas.RegistrarTalla',compact('id','filtro'));
    }

    
    public function store(Request $request)
    {
        $validated = $request->validate([
            'idzapato'=> 'required',
            'precio'=>'required',
            'talla'=>'required',
            'cantidad'=>'required'
        ]);

        $data=$request->all();
        
        Talla::create([
            'cantidad'=>$data['cantidad'], 
            'talla'=>$data['talla'], 
            'precio'=>$data['precio'], 
            'idzapato'=>$data['idzapato'],            
            'estado'=>'1'
        ]);        
        
        return redirect('/talla/listado/'.$data['idzapato']);
    }
    


    
    public function edit(string $id)
    {
        $talla=array();
        $exist=array();
        $zap = Talla::where('id','=',$id)->first();
        $total=DB::select('SELECT  talla from talla where idzapato='.$zap->idzapato);
        for ($i = 0; $i < count($total); ++$i){array_push($exist,$total[$i]->talla);}
        for ($i=20; $i <=31 ; $i++) {array_push($talla,$i);}
        $filtro=array_diff($talla,$exist);
        return view('tallas.ModificarTalla',compact('zap','filtro'));
    }

    public function resurtir(String $id){
        dd('si jala');
    }


   
    public function update(Request $request, string $id)
    {
        $validated = $request->validate([
            'idzapato'=> 'required',
            'precio'=>'required',
            'talla'=>'required',
            'cantidad'=>'required'
        ]);

        $data=$request->all();
        $zap  = Talla::find($id);
        $zap->precio=$data['precio'];
        $zap->talla=$data['talla'];
        $zap->cantidad=$data['cantidad'];
        $zap->save();
        return redirect('/talla/listado/'.$data['idzapato']);
    }

    
    public function destroy(string $id)
    {
         $zap  = Talla::find($id);
        $zap->estado="0";
        $zap->save();

        return redirect('/zapatos');
    }
}