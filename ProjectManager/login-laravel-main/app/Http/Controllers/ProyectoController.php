<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Models\Proyecto;

class ProyectoController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //$proyectos = Proyecto::all();
        $proyectos = Proyecto::where('estado','=', '1')->get();
        $proyectos2 = Proyecto::where('estado','=', '0')->get();
        return view('proyecto.listado_pro',compact('proyectos','proyectos2'));
    }
    public function filtro(Request $request)
    {
        $data=$request->all();
        $proyectos=Proyecto::where('estado','1')
        ->where('nombre','like','%'.$data['nombre'].'%')
        ->get();
        $proyectos2=Proyecto::where('estado','0')
        ->where('nombre','like','%'.$data['nombre'].'%')
        ->get();
        return view('proyecto.contenido',compact('proyectos','proyectos2'));
        //return "Hola desde funcion filtro";
    }
    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        return view('proyecto.registrar_pro');
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $validated = $request->validate([
            'nombre'=> 'required',
            'tiempod'=>'required',
            'fechaentrega'=>'required',
            'descripcion'=>'required',
            'requerimientos'=>'required'
        ]);

        $data=$request->all();
        //dd($data);
        Proyecto::create([
        'nombre'=>$data['nombre'], 
        'tiempoestimado'=>$data['tiempod'], 
        'fentrega'=>$data['fechaentrega'], 
        'descripcion'=>$data['descripcion'], 
        'requerimientos'=>$data['requerimientos'], 
        'estado'=>'1'
    ]);
    return redirect('/proyecto');

    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        $pro = Proyecto::where('id','=',$id)->first();
        return view('proyecto.consulta_pro',compact('pro'));
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
        $proyecto = Proyecto::where('id','=',$id)->first();
        return view('proyecto.modificar',compact('proyecto'));
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
        $validated = $request->validate([
            'nombre'=> 'required',
            'tiempod'=>'required',
            'fechaentrega'=>'required',
            'descripcion'=>'required',
            'requerimientos'=>'required'
        ]);

        $data=$request->all();

        $proyecto  = Proyecto::find($id);
        //dd($usuario);

        $proyecto->nombre=$data['nombre'];
        $proyecto->tiempoestimado=$data['tiempod'];
        $proyecto->fentrega=$data['fechaentrega'];
        $proyecto->descripcion=$data['descripcion'];
        $proyecto->requerimientos=$data['requerimientos'];

        $proyecto->save();

        return redirect('/proyecto');
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        $pro  = Proyecto::find($id);
        $pro->estado="0";
        $pro->fentrega=date('y-m-d');
        $pro->save();

        return redirect('/proyecto');
    }
}
