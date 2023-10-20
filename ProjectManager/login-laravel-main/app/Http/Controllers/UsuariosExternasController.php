<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ActividadesExternasController extends Controller
{
    //
    public function index(){
        $usuarios=HTTP::get('https://backproyect.000webhostapp.com/api/usuarios');
        $usuariosArray=$usuarios->json();
        return view('extraer.listado_api_usu', compact('usuariosArray'));
    }
}
