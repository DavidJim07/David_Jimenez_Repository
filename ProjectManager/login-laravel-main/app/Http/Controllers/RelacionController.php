<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Actividad;
use App\Models\Proyecto;
use App\Models\User;
use App\Models\Relacion;

class RelacionController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
       
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @param  int  $idpro
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        $relaciones = Relacion::where('id_pro','=',$id)->get();
        return view('relacion.listado', compact('relaciones','id'));
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        $relacion = Relacion::find($id);
        $evidencias=Imagen::find($id);
        $relacion->estado="0";
        $actividad = Actividad::where('id','=',$relacion->id_act)->first();
        $actividad->estado="0";
        $actividad->ffin=date('y-m-d');
        // $proyecto = Proyecto::where('id','=',$relacion->id_pro)->first();
        // $proyecto->estado="0";
        // $proyecto->save();
        $relacion->save();
        $actividad->save();
        return redirect('/actividad');
    }
}