<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Zapato;
use Illuminate\Support\Facades\Auth;

class ZapatoController extends Controller
{
   
    public function index()
    {
        if(Auth::check()){
            if(Auth::user()->role=="U"){
                return redirect()->route('home.index');
            }
        }
        $zp = Zapato::where('estado','=', '1')->get();
        return view('inventario.ListadoZapato',compact('zp'));
    }

   
    public function create()
    {
        return view('inventario.RegistrarZapato');
    }

  
    public function store(Request $request)
    {
        $validated = $request->validate([
            'codbar'=> 'required',
            'color'=>'required',
            'estilo'=>'required',
            'material'=>'required',
            'modelo'=>'required',
            'image'=>'required'
        ]);

        $data=$request->all();
        $nameImage = $request->image->getClientOriginalName();
        $request->image->move(public_path('imagenes'),$nameImage);
        Zapato::create([
            'id'=>$data['codbar'], 
            'color'=>$data['color'], 
            'estilo'=>$data['estilo'], 
            'material'=>$data['material'], 
            'modelo'=>$data['modelo'],             
            'url'=> $nameImage,             
            'estado'=>'1'
        ]);        
        
        return redirect('/zapatos');
    }


    public function show(string $id)
    {
        $zap = Zapato::where('id','=',$id)->first();
       return view('inventario.ConsultarZapato',compact('zap'));
    }

   
    public function edit(string $id)
    {
        $zap = Zapato::where('id','=',$id)->first();
        return view('inventario.EditarZapato',compact('zap'));
    }

 
    public function update(Request $request, string $id)
    {
        $validated = $request->validate([
            'color'=>'required',
            'estilo'=>'required',
            'material'=>'required',
            'modelo'=>'required'
        ]);
       
        $data=$request->all();
        $zap  = Zapato::find($data['codbar']);
        $zap->color=$data['color'];
        $zap->estilo=$data['estilo'];
        $zap->material=$data['material'];
        $zap->modelo=$data['modelo'];
        if($request->has('image')){
            $nameImage = $request->image->getClientOriginalName();
            unlink(public_path('imagenes/'.$data['url']));
            $request->image->move(public_path('imagenes'),$nameImage);
            $zap->url=$nameImage;
        }else{
            $zap->url=$data['url'];
        }
        
        $zap->save();
        return redirect('/zapatos');
       
    }

  
    public function destroy(string $id)
    {
        $zap  = Zapato::find($id);
        $zap->estado="0";
        $zap->save();

        return redirect('/zapatos');
    }
}
