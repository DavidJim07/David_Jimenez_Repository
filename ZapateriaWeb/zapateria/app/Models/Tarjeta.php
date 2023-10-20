<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Tarjeta extends Model
{
    use HasFactory;
    protected $table="tarjeta";
    protected $fillable=['id','numerotarjeta','ccv','nombre','fecha','idUser'];

    public function tarjeta(){
        return $this->hasMany(Tarjeta::class);
    }
}
