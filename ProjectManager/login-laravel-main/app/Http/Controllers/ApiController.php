<?php

namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;

use Illuminate\Http\Request;

class ApiController extends Controller
{
    //
    public function proyectos(Request $request){
        $proyectos = DB::select("SELECT * FROM proyectos");
        return response()->json($proyectos);
    }
    public function actividades(Request $request){
        $actividades = DB::select("SELECT * FROM actividads");
        return response()->json($actividades);
    }
    public function usuarios(Request $request){
        $usuarios = DB::select("SELECT * FROM users");
        return response()->json($usuarios);
    }
}
