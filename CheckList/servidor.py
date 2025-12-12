import http.server
import socketserver
import socket
import qrcode
import os
import signal
import sys
from PIL import Image

def obter_ip_local():
    """Obtém o IP local da máquina"""
    try:
        # Conecta a um endereço externo para descobrir o IP local
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

def gerar_qrcode(url, nome_arquivo="qrcode_checklist.png"):
    """Gera QR Code para o URL"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nome_arquivo)
    print(f"📱 QR Code salvo como: {nome_arquivo}")

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adicionar headers para permitir acesso de outros dispositivos
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

def salvar_pid():
    """Salva PID do processo para poder parar depois"""
    with open('servidor_pid.txt', 'w') as f:
        f.write(str(os.getpid()))

def iniciar_servidor():
    PORT = 8000
    ip_local = obter_ip_local()
    url = f"http://{ip_local}:{PORT}/checklist-equipamentos.html"
    
    print("🚀 SERVIDOR CHECKLIST INICIADO!")
    print("=" * 50)
    print(f"📱 Acesse no celular: {url}")
    print(f"💻 Acesse no PC: http://localhost:{PORT}/checklist-equipamentos.html")
    print("=" * 50)
    
    # Gerar QR Code
    try:
        gerar_qrcode(url)
        print("✅ QR Code gerado! Escaneie para acessar no celular")
    except Exception as e:
        print(f"⚠️ Erro ao gerar QR Code: {e}")
        print("💡 Instale: pip install qrcode[pil]")
    
    print("\n✅ SERVIDOR RODANDO EM BACKGROUND")
    print("❌ Pode fechar esta janela - servidor continua ativo")
    print("🛑 Para parar: execute 'parar_servidor.bat'")
    print("=" * 50)
    
    # Salvar PID para controle
    salvar_pid()
    
    # Iniciar servidor
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        try:
            httpd.serve_forever()
        except (KeyboardInterrupt, SystemExit):
            print("\n🛑 Servidor parado!")
        finally:
            # Limpar arquivo PID
            if os.path.exists('servidor_pid.txt'):
                os.remove('servidor_pid.txt')

if __name__ == "__main__":
    # Configurar handler para sinais do sistema
    def signal_handler(sig, frame):
        print('\n🛑 Parando servidor...')
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    iniciar_servidor()