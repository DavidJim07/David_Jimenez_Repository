<?php

namespace App\Models;

use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Laravel\Sanctum\HasApiTokens;
use Illuminate\Support\Facades\Auth;

class User extends Authenticatable
{
    use HasApiTokens, HasFactory, Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<int, string>
     */
    protected $table = "users";
    protected $fillable = [
    'name',
    'paterno',
    'materno',
    'nacimiento',
    'genero',
    'telefono',
    'email',
    'role',
    'username',
    'password',
    'estado',
    'created_at',
    'updated_at'];

    /**
     * The attributes that should be hidden for serialization.
     *
     * @var array<int, string>
     */
    public function relacion(){
        return $this->hasMany(Relacion::class);
    }
    
    protected $hidden = [
        'password',
        'remember_token',
    ];

    /**
     * The attributes that should be cast.
     *
     * @var array<string, string>
     */
    protected $casts = [
        'email_verified_at' => 'datetime',
    ];

    public function setPasswordAttribute(string $password){
        $this->attributes['password'] = bcrypt($password);

    }

    public function hasRole($role)
    {
        return $this->role == $role;
    }
    public function compararId($id)
    {
        return $this->id == $id;
    }
}
