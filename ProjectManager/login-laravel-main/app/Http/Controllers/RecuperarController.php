<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class RecuperarController extends Controller
{
    //
    public function index(){
        $proyectos=HTTP::get('');
        $proyectosArray=$proyectos;
        
        $actividades=HTTP::get('');
        $actividadesArray=$actividades;

        $usuarios=HTTP::get('');
        $usuariosArray=$usuarios;
    }
}
