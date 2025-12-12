@echo off
echo 📊 STATUS DO SERVIDOR CHECKLIST
echo ================================

if exist "servidor_pid.txt" (
    set /p PID=<servidor_pid.txt
    tasklist /FI "PID eq %PID%" 2>nul | find /i "python.exe" >nul
    if %errorlevel% equ 0 (
        echo ✅ Servidor ATIVO (PID: %PID%)
        echo 🌐 Acesse: http://localhost:8000/checklist-equipamentos.html
    ) else (
        echo ❌ Servidor INATIVO (processo não encontrado)
        del servidor_pid.txt >nul 2>&1
    )
) else (
    echo ❌ Servidor PARADO
)

echo.
timeout /t 5 >nul