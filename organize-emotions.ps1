$dl  = "$env:USERPROFILE\Downloads"
$dst = "$env:USERPROFILE\Desktop\roy-games\images\emotions"

New-Item -ItemType Directory -Force "$dst\boy" | Out-Null
New-Item -ItemType Directory -Force "$dst\girl" | Out-Null

$names = @(
  'boy-face-happy','boy-face-sad','boy-face-angry','boy-face-surprised','boy-face-scared',
  'boy-eyes-happy','boy-eyes-sad','boy-eyes-angry','boy-eyes-surprised','boy-eyes-scared',
  'boy-mouth-happy','boy-mouth-sad','boy-mouth-angry','boy-mouth-surprised','boy-mouth-scared',
  'girl-face-happy','girl-face-sad','girl-face-angry','girl-face-surprised','girl-face-scared',
  'girl-eyes-happy','girl-eyes-sad','girl-eyes-angry','girl-eyes-surprised','girl-eyes-scared',
  'girl-mouth-happy','girl-mouth-sad','girl-mouth-angry','girl-mouth-surprised','girl-mouth-scared'
)

$moved = 0
foreach ($n in $names) {
    $gender = $n.Split('-')[0]
    $part   = $n -replace "^$gender-", ""
    $src = $null
    foreach ($ext in @('png','jpg','jpeg','webp')) {
        $candidate = Join-Path $dl "$n.$ext"
        if (Test-Path $candidate) { $src = $candidate; break }
    }
    if ($src) {
        $dest = Join-Path $dst "$gender\$part.jpg"
        Copy-Item $src $dest -Force
        $moved++
        Write-Host "OK: $n -> $gender/$part.jpg"
    } else {
        Write-Host "MISSING: $n"
    }
}
Write-Host "Done: $moved of $($names.Count) moved."
