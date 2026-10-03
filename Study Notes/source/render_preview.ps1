# Render representative pages using Windows' built-in PDF renderer.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]
$null = [Windows.Data.Pdf.PdfDocument, Windows.Data.Pdf, ContentType=WindowsRuntime]
$null = [Windows.Storage.Streams.InMemoryRandomAccessStream, Windows.Storage.Streams, ContentType=WindowsRuntime]
$asTaskGeneric = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq 'AsTask' -and $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and
    $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1'
} | Select-Object -First 1
$asTaskAction = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq 'AsTask' -and -not $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and
    $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncAction'
} | Select-Object -First 1
function Wait-PdfResult($operation, $resultType) {
    $task = $asTaskGeneric.MakeGenericMethod($resultType).Invoke($null, @($operation))
    $task.GetAwaiter().GetResult()
}
$previewDirectory = Join-Path $PSScriptRoot 'build\preview'
New-Item -ItemType Directory -Path $previewDirectory -Force | Out-Null
$previewPages = @{ 0 = @(0, 5); 1 = @(1, 9, 12); 2 = @(3, 9); 3 = @(4, 8); 4 = @(4, 7, 11) }
foreach ($topic in 0..4) {
    $pdfPath = Join-Path $PSScriptRoot "build\Topic_$topic.pdf"
    $file = Wait-PdfResult ([Windows.Storage.StorageFile]::GetFileFromPathAsync($pdfPath)) ([Windows.Storage.StorageFile])
    $document = Wait-PdfResult ([Windows.Data.Pdf.PdfDocument]::LoadFromFileAsync($file)) ([Windows.Data.Pdf.PdfDocument])
    Write-Output "Topic $topic : $($document.PageCount) pages"
    foreach ($pageIndex in $previewPages[$topic]) {
        $page = $document.GetPage([uint32]$pageIndex)
        $stream = New-Object Windows.Storage.Streams.InMemoryRandomAccessStream
        try {
            $renderTask = $asTaskAction.Invoke($null, @($page.RenderToStreamAsync($stream)))
            $null = $renderTask.GetAwaiter().GetResult()
            $stream.Seek(0)
            $readStream = [System.IO.WindowsRuntimeStreamExtensions]::AsStreamForRead($stream)
            $previewPath = Join-Path $previewDirectory "Topic_${topic}_page_$($pageIndex+1).png"
            $outputStream = [System.IO.File]::Create($previewPath)
            try { $readStream.CopyTo($outputStream) } finally { $outputStream.Dispose() }
        }
        finally { $page.Dispose(); $stream.Dispose() }
    }
}
