@echo off
echo 🛑 PARANDO SERVIDOR CHECKLIST...
echo.

REM Verificar se existe arquivo PID
if not exist "servidor_pid.txt" (
    echo ❌ Servidor não está rodando ou arquivo PID não encontrado
    echo 💡 Tente fechar pelo Gerenciador de Tarefas: python.exe
    pause
    exit /b 1
)

REM Ler PID do arquivo
set /p PID=<servidor_pid.txt

REM Parar processo
taskkill /PID %PID% /F >nul 2>&1

if %errorlevel% equ 0 (
    echo ✅ Servidor parado com sucesso!
    del servidor_pid.txt >nul 2>&1
) else (
    echo ⚠️ Erro ao parar servidor ou já estava parado
    echo 💡 Tente pelo Gerenciador de Tarefas: python.exe
    del servidor_pid.txt >nul 2>&1
)

echo.
pause