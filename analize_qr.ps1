
param(
    [string]$image_path = ""
)
Add-Type -AssemblyName System.Windows.Forms
$python = "python"
$dir_script = ""
$current_location = Get-Location
Set-Location $dir_script
$timeoutSeconds = 10
$start = Get-Date
if ($image_path -ne "") {
    
    & $python ".\main.py" --image_path $image_path
    exit 1
} else {
    # Verficicar que en el portapales hay una imagen
    $clipboard = [Windows.Forms.Clipboard]::GetImage()
    Write-Host $clipboard
    if ($null -eq $clipboard) {
        Write-Host "Captura una imagen "
        Start-Process "ms-screenclip:"
        do {
            Start-Sleep -Milliseconds 500
            $clipboardImage = [Windows.Forms.Clipboard]::GetImage()
            $elapsed = (Get-Date) - $start
        } while ( $null -eq $clipboardImage -and $elapsed.TotalSeconds -lt $timeoutSeconds)
    }
    & $python ".\main.py"
}
Set-Location $current_location