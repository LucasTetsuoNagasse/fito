clean vscode terminal history:
```bat
Set-PSReadlineOption -HistoryNoDuplicates
Remove-Item (Get-PSReadlineOption).HistorySavePath
```
