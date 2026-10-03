$ErrorActionPreference = 'Stop'
$notesSource = $PSScriptRoot
$notesOutput = Split-Path -Parent $notesSource
$notesBuild = Join-Path $notesSource 'build'
New-Item -ItemType Directory -Path $notesBuild -Force | Out-Null
$volumes = @(
    '0. Mathematical background',
    '1. Learning fundamentals, shallow and Bayesian learning',
    '2. Reinforcement learning',
    '3. Neural networks and deep learning fundamentals',
    '4. CNNs and transfer learning'
)
Push-Location $notesSource
try {
    for ($topicIndex = 0; $topicIndex -lt $volumes.Count; $topicIndex++) {
        $topicSource = "Topic_$topicIndex.tex"
        # A populated two-page contents list can change pagination on pass 2.
        # Pass 3 resolves those updated destinations in a clean build.
        for ($compilePass = 1; $compilePass -le 3; $compilePass++) {
            $compileOutput = & pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build $topicSource 2>&1
            if ($LASTEXITCODE -ne 0) {
                $compileOutput | Select-Object -Last 35 | Write-Output
                throw "PDF compilation failed for $topicSource (pass $compilePass)."
            }
        }
        $compiledPdf = Join-Path $notesBuild "Topic_$topicIndex.pdf"
        $finalPdf = Join-Path $notesOutput ($volumes[$topicIndex] + '.pdf')
        Copy-Item -LiteralPath $compiledPdf -Destination $finalPdf -Force
        Write-Output "Built: $($volumes[$topicIndex]).pdf"
    }
}
finally {
    Pop-Location
}
