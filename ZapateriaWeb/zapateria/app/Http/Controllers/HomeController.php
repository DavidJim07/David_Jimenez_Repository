<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Models\Zapato;

use Illuminate\Support\Facades\DB;

class HomeController extends Controller
{
    //

    public function index() 
    {
        if(Auth::check()){
            if(Auth::user()->role=="A"){
                return redirect('/zapatos');
            }
        }
        $zap = Zapato::where('estado','=','1')->get();
        $total=DB::select('select zapato.id, talla.id as idTalla, cantidad, talla, precio from talla, zapato where cantidad>0 and talla.idzapato=zapato.id');
        $zapatos=array();
        $zapatosID=array();
        foreach($total as $t){
            if(!in_array($t->id, $zapatosID)){
                array_push($zapatosID, $t->id);
            }
        }
        foreach($zap as $z){
            if(in_array($z->id, $zapatosID)){
                array_push($zapatos, $z);
            }
        }
        return view('Index', compact('zapatos','total'));
    }
}
