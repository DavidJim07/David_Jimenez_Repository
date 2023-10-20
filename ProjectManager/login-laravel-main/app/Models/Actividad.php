<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Actividad extends Model
{
    use HasFactory;
    protected $table="actividads";
    protected $fillable=['descripcion','finicio','ffin','testimado','prioridad','estado'];

    public function relacion(){
        return $this->hasMany(Relacion::class);
    }
}
