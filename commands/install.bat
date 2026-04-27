nssm install rpa-monitor-scripts "%~dp0..\.venv\Scripts\python.exe"
nssm set rpa-monitor-scripts AppDirectory "%~dp0.."
nssm set rpa-monitor-scripts AppParameters "main.py"