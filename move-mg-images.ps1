$dl  = "$env:USERPROFILE\Downloads"
$dst = "$env:USERPROFILE\Desktop\roy-games\images\mg"

New-Item -ItemType Directory -Force $dst | Out-Null

$files = @(
  'top10','left10','right10','success10',
  'top11','left11','right11','success11',
  'top12','left12','right12','success12',
  'top13','left13','right13','success13',
  'top14','left14','right14','success14'
)

$moved = 0
$missing = @()
foreach ($n in $files) {
    $src = $null
    foreach ($ext in @('jpg','jpeg','png','webp')) {
        $candidate = Join-Path $dl "$n.$ext"
        if (Test-Path $candidate) { $src = $candidate; break }
    }
    if ($src) {
        $dest = Join-Path $dst "$n.jpg"
        Copy-Item $src $dest -Force
        Write-Host "OK: $n -> $dest"
        $moved++
    } else {
        Write-Host "MISSING: $n"
        $missing += $n
    }
}

Write-Host ""
Write-Host "Done: $moved / $($files.Count) copied."
if ($missing.Count -gt 0) {
    Write-Host "Missing: $($missing -join ', ')"
}
