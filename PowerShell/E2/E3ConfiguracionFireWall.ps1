<#Enrique Rocha Medina, Juan Pablo Rangel Guevara #>
Import-Module modulofirewall

function get-menu{
    
[int]$respuesta = Read-Host  "`n`Elige una opción`n` [1] Ver StatusPerfil`n` [2] Cambiar StatusPerfil`n` [3] Ver Perfil de Red Actual`n` [4] Cambiar-PerfilRedActual`n` [5] Ver-ReglasBloqueo`n` [6] Agregar-ReglasBloqueo`n` [7] Eliminar-ReglasBloqueo`n` [8] Salir`n`  Opción  "

switch ($respuesta)
{
    1{Ver-StatusPerfil}
    2{Cambiar-StatusPerfil}
    3{Ver-PerfilRedActual}
    4{Cambiar-PerfilRedActual}
    5{Ver-ReglasBloqueo}
    6{Agregar-ReglasBloqueo}
    7{Eliminar-ReglasBloqueo}
    8{Exit}
    Default {write-host "opcion no valida"}
}}

do
{
 clear
 get-menu
 Read-Host "Pulsa intro para volver al menu"  
    
}while ($true)