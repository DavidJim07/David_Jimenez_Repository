<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ActividadesExternasController extends Controller
{
    //
    public function index(){
        $actividades=HTTP::get('https://backproyect.000webhostapp.com/api/actividades');
        $actividadesArray=$actividades->json();
        return view('extraer.listado_api_act', compact('actividadesArray'));
    }
}
