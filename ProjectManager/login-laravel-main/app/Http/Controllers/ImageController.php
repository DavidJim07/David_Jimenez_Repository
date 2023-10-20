<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Actividad;
use App\Models\Proyecto;
use App\Models\User;
use App\Models\Relacion;
use App\Models\Image;

class ImageController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //
        $images = Image::all();
    	return view('imagen.index', compact('images'));
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
        $actividades = Actividad::all();
        $relacion = Relacion::all();
    	return view('imagen.create',compact('actividades','relacion'));
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     *hoy solo  @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
        $validated = $request->validate([
            'imagenes'=> 'required'
        ]);

        if(count($request->file('imagenes'))==1){
            $id=$request->get('id_relacion');

            $archivo=$request->file('imagenes');
            $total_imagenes = count(glob(public_path('images').'/{*.jpg,*.gif,*.png}',GLOB_BRACE));
            $archivo[0]->move(public_path('images'), $total_imagenes."_".$id."_".$archivo[0]->getClientOriginalName());

            $image = new Image([
                "id_rel" => $id,
                "image" => ($total_imagenes."_".$id."_".$archivo[0]->getClientOriginalName())
            ]);
            $image->save();
            return redirect()->to("/actividad"."/".$id."/imagen");
        }else{
            $id=$request->get('id_relacion');
            $archivos=$request->file('imagenes');

            for($i=0; $i<count($archivos); $i++){
                $total_imagenes = count(glob(public_path('images').'/{*.jpg,*.gif,*.png}',GLOB_BRACE));
                $archivos[$i]->move(public_path('images'), $total_imagenes."_".$id."_".$archivos[$i]->getClientOriginalName());

                $image = new Image([
                    "id_rel" => $id,
                    "image" => ($total_imagenes."_".$id."_".$archivos[$i]->getClientOriginalName())
                ]);
                $image->save(); 
            }
            return redirect()->to("/actividad"."/".$id."/imagen");
        }
        // $nameImage = $request->image->getClientOriginalName();

        // $image = new Image();

        // $image->image = $nameImage;

        // $request->image->move(public_path('imaages'),$nameImage);

        // // $image->save();

        // $image = new Image([
        //     "id_rel" => $request->get('id_relacion'),
        //     "image" => ($request->image->getClientOriginalName())
        // ]);
        
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
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
        //
    }
}
