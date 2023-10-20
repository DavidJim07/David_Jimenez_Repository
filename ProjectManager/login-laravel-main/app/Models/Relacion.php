<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Relacion extends Model
{
    use HasFactory;
    protected $table="relacion";
    protected $fillable=[
    'id',
    'id_pro',
    'id_act',
    'id_usu',
    'estado'];

    public function actividad(){
        return $this->belongsTo(Actividad::class,'id_act');
    }
    public function proyecto(){
        return $this->belongsTo(Proyecto::class,'id_pro');
    }
    public function user(){
        return $this->belongsTo(User::class,'id_usu');
    }
}
