function Ver-StatusPerfil{  

param([Parameter(Mandatory)] [ValidateSet("Public","Private")] [string] $perfil)  

$status = Get-NetFirewallProfile -Name $perfil  

Write-Host "Perfil:" $perfil  

if($status.enabled){  

Write-Host "Status: Activado"  

} else{  

Write-Host "Status: Desactivado"  

} 

} 

  

 function Cambiar-StatusPerfil{  

param([Parameter(Mandatory)] [ValidateSet("Public","Private")] [string] $perfil)  

$status = Get-NetFirewallProfile -Name $perfil  

Write-Host "Perfil:" $perfil  

if($status.enabled){  

Write-Host "Status actual: Activado"  

$opc = Read-Host -Promt "Deseas desactivarlo? [Y] Si [N] No"  

if ($opc -eq "Y"){  

Set-NetFirewallProfile -Name $perfil -Enabled False  

}  

} else{  

Write-Host "Status: Desactivado"  

$opc = Read-Host -Promt "Deseas activarlo? [Y] Si [N] No"  

if ($opc -eq "Y"){  

Write-Host "Activando perfil"  

Set-NetFirewallProfile -Name $perfil -Enabled True  

}  

}  

Ver-StatusPerfil -perfil $perfil  

}  

function Ver-PerfilRedActual{  

$perfilRed = Get-NetConnectionProfile  

Write-Host "Nombre de red:" $perfilRed.Name  

Write-Host "Perfil de red:" $perfilRed.NetworkCategory  

}  

function Cambiar-PerfilRedActual{  

$perfilRed = Get-NetConnectionProfile  

if($perfilRed.NetworkCategory -eq "Public"){  

Write-Host "El perfil actual es p�blico"  

$opc = Read-Host -Prompt "Quieres cambiar a privado? [Y] Si [N] No"  

if($opc -eq "Y"){  

Set-NetConnectionProfile -Name $perfilRed.Name -NetworkCategory Private  

Write-Host "Perfil cambiado"  

}  

} else{  

Write-Host "El perfil actual es privado"  

$opc = Read-Host -Prompt "Quieres cambiar a p�blico? [Y] Si [N] No"  

if($opc -eq "Y"){  

Set-NetConnectionProfile -Name $perfilRed.Name -NetworkCategory Public 

Write-Host "Perfil cambiado"  

}  

}  

Ver-PerfilRedActual  

}  


function Ver-ReglasBloqueo{  

if(Get-NetFirewallRule -Action Block -Enabled True -ErrorAction SilentlyContinue){  

Get-NetFirewallRule -Action Block -Enabled True  

} else{  

Write-Host "No hay reglas definidas a�n"  

}  

} 



