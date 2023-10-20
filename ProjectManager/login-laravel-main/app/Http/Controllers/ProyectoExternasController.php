<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ActividadesExternasController extends Controller
{
    //
    public function index(){
        $proyectos=HTTP::get('https://backproyect.000webhostapp.com/api/proyectos');
        $proyectosArray=$proyectos->json();
        return view('extraer.listado_api_pro', compact('proyectosArray'));
    }
}
