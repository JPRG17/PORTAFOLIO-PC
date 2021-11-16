<#Enrique Rocha Medina, Juan Pablo Rangel Guevara #>
Import-Module ModuloE6

function get-menu{
try{
    
[int]$respuesta = Read-Host  "`n`Elige una opción`n` [1] Ver StatusPerfil`n` [2] Cambiar StatusPerfil`n` [3] Ver Perfil de Red Actual`n` [4] Cambiar-PerfilRedActual`n` [5] Ver-ReglasBloqueo`n` [6] Salir`n`  Opción  "

switch ($respuesta)
{
    1{Ver-StatusPerfil}
    2{Cambiar-StatusPerfil}
    3{Ver-PerfilRedActual}
    4{Cambiar-PerfilRedActual}
    5{Ver-ReglasBloqueo}
    6{Exit}
    
}}catch{{write-host "opcion no valida intente nuevamente"}}}

do
{
 clear
 get-menu
 Read-Host "Pulsa intro para volver al menu"  
    
}while ($true)