<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Proyecto extends Model
{
    use HasFactory;
    protected $table="proyectos";
    protected $fillable=['nombre','tiempoestimado','fentrega','descripcion','requerimientos','estado'];

    public function proyecto(){
        return $this->hasMany(Proyecto::class);
    }
}
