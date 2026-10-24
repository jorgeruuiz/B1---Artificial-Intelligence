param([string[]]$Topics = @())
$ErrorActionPreference = 'Stop'
$notesSource = $PSScriptRoot
$notesOutput = Split-Path -Parent $notesSource
$notesBuild = Join-Path $notesSource 'build'
New-Item -ItemType Directory -Path $notesBuild -Force | Out-Null
$volumes = [ordered]@{
    '0' = '0. Mathematical background'
    '1' = '1. Learning fundamentals, shallow and Bayesian learning'
    '2' = '2. Reinforcement learning'
    '3' = '3. Neural networks and deep learning fundamentals'
    '4' = '4. CNNs and transfer learning'
    '5' = '5. Advanced deep learning'
}
foreach ($requestedTopic in $Topics) {
    if (-not $volumes.Contains($requestedTopic)) {
        throw "Unknown topic '$requestedTopic'. Use: $($volumes.Keys -join ', ')."
    }
}
Push-Location $notesSource
try {
    foreach ($topicIndex in $volumes.Keys) {
        if ($Topics.Count -gt 0 -and $topicIndex -notin $Topics) { continue }
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
        $logPath = Join-Path $notesBuild "Topic_$topicIndex.log"
        $layoutWarnings = Select-String -LiteralPath $logPath -Pattern 'Overfull|Missing character|undefined references'
        if ($layoutWarnings) { $layoutWarnings.Line | Write-Output }
        $compiledPdf = Join-Path $notesBuild "Topic_$topicIndex.pdf"
        $finalPdf = Join-Path $notesOutput ($volumes[$topicIndex] + '.pdf')
        Copy-Item -LiteralPath $compiledPdf -Destination $finalPdf -Force
        Write-Output "Built: $($volumes[$topicIndex]).pdf"
    }
}
finally {
    Pop-Location
}
