$dl = "$env:USERPROFILE\Downloads"
$out = "$env:USERPROFILE\Desktop\roy-games\downloads-list.txt"
$images = Get-ChildItem $dl -Include *.png,*.jpg,*.jpeg,*.webp -Recurse | Sort-Object LastWriteTime -Descending | Select-Object -First 60
$images | ForEach-Object { $_.Name } | Out-File $out -Encoding UTF8
Write-Host "Found $($images.Count) images. List saved to downloads-list.txt"
Read-Host "Press Enter"
