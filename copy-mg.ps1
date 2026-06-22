$downloads = "C:\Users\Yairn\Downloads"
$dest = "C:\Users\Yairn\Desktop\roy-games\images\mg"
$files = @("top10","left10","right10","success10",
           "top11","left11","right11","success11",
           "top12","left12","right12","success12",
           "top13","left13","right13","success13",
           "top14","left14","right14","success14")

foreach ($f in $files) {
    $latest = Get-ChildItem -Path $downloads -Filter ($f + "*.jpg") |
              Sort-Object LastWriteTime -Descending |
              Select-Object -First 1
    if ($latest) {
        Copy-Item $latest.FullName (Join-Path $dest ($f + ".jpg")) -Force
        Write-Host "OK: $($latest.Name) ($($latest.Length) bytes) -> $f.jpg"
    } else {
        Write-Host "MISSING: $f"
    }
}

Write-Host ""
Write-Host "=== Git push ==="
Set-Location "C:\Users\Yairn\Desktop\roy-games"
if (Test-Path ".git\index.lock") { Remove-Item ".git\index.lock" -Force }
git add "images\mg\*.jpg"
git commit -m "add mr-gamish puzzle images 10-14 (20 images)"
git push origin master
Write-Host "Done!"
