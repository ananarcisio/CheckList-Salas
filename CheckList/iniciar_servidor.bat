@echo off
echo 🚀 INICIANDO SERVIDOR CHECKLIST...
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado!
    echo 💡 Instale Python em: https://python.org
    pause
    exit /b 1
)

REM Verificar se servidor já está rodando
if exist "servidor_pid.txt" (
    echo ⚠️ Servidor já está rodando!
    echo 💡 Para parar: execute 'parar_servidor.bat'
    timeout /t 5 >nul
    exit /b 0
)

REM Instalar dependências se necessário
echo 📦 Verificando dependências...
pip install qrcode[pil] >nul 2>&1

REM Iniciar servidor em background
echo ✅ Iniciando servidor...
start /min python servidor.py

REM Aguardar servidor inicializar
timeout /t 3 >nul

echo.
echo ✅ SERVIDOR INICIADO EM BACKGROUND!
echo 📱 Escaneie o QR Code ou acesse pelo navegador
echo 🛑 Para parar: execute 'parar_servidor.bat'
echo.
timeout /t 10 >nul