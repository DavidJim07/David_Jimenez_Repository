<?php

namespace App\Http\Controllers;
use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;
use App\Models\Image;
use App\Models\Actividad;
use App\Models\Proyecto;
use App\Models\User;
use App\Models\Relacion;

class ActividadController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $relaciones = Relacion::where('estado','=', '1')->get();
        $relAlta=array();
        $relMedia=array();
        $relBaja=array();
        foreach($relaciones as $r){
            if($r->actividad->prioridad=="Alta"){
                array_push($relAlta,$r);
            }elseif($r->actividad->prioridad=="Media"){
                array_push($relMedia,$r);
            }elseif($r->actividad->prioridad=="Baja"){
                array_push($relBaja,$r);
            }
        }
        $relaciones = array_merge($relAlta, $relMedia, $relBaja);
        $relaciones2 = Relacion::where('estado','=', '0')->get();
        $relAlta=array();
        $relMedia=array();
        $relBaja=array();
        foreach($relaciones2 as $r){
            if($r->actividad->prioridad=="Alta"){
                array_push($relAlta,$r);
            }elseif($r->actividad->prioridad=="Media"){
                array_push($relMedia,$r);
            }elseif($r->actividad->prioridad=="Baja"){
                array_push($relBaja,$r);
            }
        }
        $relaciones2 = array_merge($relAlta, $relMedia, $relBaja);
        return view('actividad.listado_act', compact('relaciones','relaciones2'));
        /*$actividades=DB::select(' SELECT relacion.id, actividads.descripcion, actividads.prioridad, users.name,users.paterno,users.materno, proyectos.nombre, relacion.estado from relacion,proyectos,actividads,users
        where relacion.id_pro=proyectos.id and relacion.id_act=actividads.id and relacion.id_usu=users.id group by relacion.id order by relacion.estado desc, actividads.prioridad asc;');
        return view('actividad.listado_act', compact('actividades'));*/
    }
    public function filtro(Request $request)
    {
        $data=$request->all();
        if($data['nombre']==""){
            $relaciones = Relacion::where('estado','=', '1')->get();
            $relAlta=array();
            $relMedia=array();
            $relBaja=array();
            foreach($relaciones as $r){
                if($r->actividad->prioridad=="Alta"){
                    array_push($relAlta,$r);
                }elseif($r->actividad->prioridad=="Media"){
                    array_push($relMedia,$r);
                }elseif($r->actividad->prioridad=="Baja"){
                    array_push($relBaja,$r);
                }
            }
            $relaciones = array_merge($relAlta, $relMedia, $relBaja);
            $relaciones2 = Relacion::where('estado','=', '0')->get();
            $relAlta=array();
            $relMedia=array();
            $relBaja=array();
            foreach($relaciones2 as $r){
                if($r->actividad->prioridad=="Alta"){
                    array_push($relAlta,$r);
                }elseif($r->actividad->prioridad=="Media"){
                    array_push($relMedia,$r);
                }elseif($r->actividad->prioridad=="Baja"){
                    array_push($relBaja,$r);
                }
            }
            $relaciones2 = array_merge($relAlta, $relMedia, $relBaja);
            return view('actividad.contenido', compact('relaciones','relaciones2'));
        }else{
            $actividades=Actividad::where('estado','1')
            ->where('descripcion','like','%'.$data['nombre'].'%')
            ->get();
            $relaciones=array();
            $relaciones2=array();
            //dd($actividades);
            foreach($actividades as $actividad){
                //dd($actividad->id);
                $relacion=Relacion::where('estado','1')
                ->where('id_act', $actividad->id)->first();
                if($relacion!=null){
                    array_push($relaciones,$relacion);
                }
                $relacion2=Relacion::where('estado','0')
                ->where('id_act', $actividad->id)->first();
                if($relacion2!=null){
                    array_push($relaciones2,$relacion2);
                }
            }
            $relAlta=array();
            $relMedia=array();
            $relBaja=array();
            //dd($relaciones);
            for($i=0; $i<count($relaciones); $i++){
                if($relaciones[$i]->actividad->prioridad=="Alta"){
                    array_push($relAlta,$relaciones[$i]);
                }elseif($relaciones[$i]->actividad->prioridad=="Media"){
                    array_push($relMedia,$relaciones[$i]);
                }elseif($relaciones[$i]->actividad->prioridad=="Baja"){
                    array_push($relBaja,$relaciones[$i]);
                }
            }
            $relaciones = array_merge($relAlta, $relMedia, $relBaja);
            //dd($relaciones);
            $relAlta=array();
            $relMedia=array();
            $relBaja=array();
            for($i=0; $i<count($relaciones2); $i++){
                if($relaciones2[$i]->actividad->prioridad=="Alta"){
                    array_push($relAlta,$relaciones2[$i]);
                }elseif($relaciones2[$i]->actividad->prioridad=="Media"){
                    array_push($relMedia,$relaciones2[$i]);
                }elseif($relaciones2[$i]->actividad->prioridad=="Baja"){
                    array_push($relBaja,$relaciones2[$i]);
                }
            }
            $relaciones2 = array_merge($relAlta, $relMedia, $relBaja);
            /*dd($actividades);
            $relaciones=Relacion::where('estado','1')
            ->where('descripcion','like','%'.$data['nombre'].'%')
            ->get();
            dd($relaciones);*/
            return view('actividad.contenido',compact('relaciones','relaciones2'));
            //return "Hola desde funcion filtro";
        }
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        $proyecto = Proyecto::all();
        $usu = User::all();
        return view('actividad.registrar_act', compact('proyecto','usu'));
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
            'descripcion'=> 'required',
            'inicioact'=>'required',
            'finact'=>'required',
            'tiempoes'=>'required',
            'proyecto'=>'required',
            'usu'=>'required',
            'prioridad'=>'required'
        ]);

        $data=$request->all();
        Actividad::create([
            'descripcion'=>$data['descripcion'], 
            'finicio'=>$data['inicioact'], 
            'ffin'=>$data['finact'], 
            'testimado'=>$data['tiempoes'], 
            'prioridad'=>$data['prioridad'], 
            'estado'=>'1'
        ]);

        $uid=Actividad::max('id');

        Relacion::create([
            'id_pro'=>$data['proyecto'], 
            'id_act'=>$uid, 
            'id_usu'=>$data['usu'],
            'estado'=>'1'
        ]);
        return redirect('/actividad');
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        $imagenes = Image::where('id_rel','=',$id)->get();
        $relacion = Relacion::where('id','=',$id)->first();
        return view('actividad.consultar_act',compact('relacion','imagenes'));
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        $relacion = Relacion::where('id','=',$id)->first();
        $proyecto = Proyecto::all();
        $usu = User::all();
        return view('actividad.modificar',compact('relacion','proyecto','usu'));
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
        $validated = $request->validate([
            'descripcion'=> 'required',
            'inicioact'=>'required',
            'finact'=>'required',
            'tiempoes'=>'required',
            'proyecto'=>'required',
            'usu'=>'required',
            'prioridad'=>'required'
        ]);

        $data = $request->all();

        $relacion = Relacion::find($id);
        $actividad = Actividad::find($relacion->id_act);
        
        $actividad->descripcion=$data['descripcion'];
        $actividad->finicio=$data['inicioact'];
        $actividad->ffin=$data['finact'];
        $actividad->testimado=$data['tiempoes'];
        $actividad->prioridad=$data['prioridad'];
        
        $relacion->id_pro=$data['proyecto'];
        $relacion->id_usu = $data['usu'];

        $actividad->save();
        $relacion->save();
        return redirect('/actividad');
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }

    public function imagen($id)
    {
        //
        $relacion = Relacion::where('id','=',$id)->first();
        return view('imagen.create',compact('relacion'));
    }
}
