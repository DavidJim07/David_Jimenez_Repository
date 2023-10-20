<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Talla extends Model
{
    use HasFactory;
    protected $table="talla";
    protected $fillable=['cantidad','talla','precio','idzapato','estado'];
    public function talla(){
        return $this->hasMany(Talla::class);
    }
}
