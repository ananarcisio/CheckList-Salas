# Sistema de Checklist de Equipamentos

Sistema web desenvolvido para otimizar o processo de verificação de equipamentos por sala na empresa, com servidor Python integrado para acesso via rede local.

## 🎯 Problema Resolvido
- Substituiu processo manual em papel
- Eliminou perda de dados de verificações
- Padronizou processo de checklist
- Gerou relatórios automáticos
- Permitiu acesso via dispositivos móveis

## 🚀 Funcionalidades
- **Interface responsiva** (desktop/mobile)
- **Servidor Python local** para acesso via URL
- **QR Code automático** para acesso rápido no celular
- **Validação de campos obrigatórios**
- **Exportação de relatórios completos**
- **Controle de tipos de verificação** (dia de tomadas)
- **Contador de progresso** em tempo real

## 💻 Tecnologias
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Backend**: Python (servidor HTTP simples)
- **Design**: Responsivo com CSS Grid/Flexbox
- **Armazenamento**: LocalStorage do navegador
- **QR Code**: Biblioteca Python qrcode

## 🌐 Como Usar

### Método 1: Servidor Local (Recomendado)
```bash
# 1. Executar servidor
python servidor.py

# 2. Acessar no navegador
# PC: http://localhost:8000/checklist-equipamentos.html
# Celular: Escanear QR Code gerado
```

### Método 2: Arquivo Local
```bash
# Abrir diretamente no navegador
checklist-equipamentos.html
```

## 📱 Acesso Mobile
- **QR Code automático** gerado pelo servidor
- **URL da rede local** para acesso direto
- **Interface otimizada** para telas pequenas
- **Cards responsivos** no lugar de tabelas

## 📊 Impacto na Empresa
- ⏱️ **Redução de 70%** no tempo de verificação
- 📋 **100% digital** - eliminou papel
- 📈 **Relatórios padronizados** automáticos
- 📱 **Mobilidade** - verificação in-loco
- 🔄 **Controle de progresso** em tempo real

## 🛠️ Instalação
```bash
# Clonar repositório
git clone https://github.com/seuusuario/checklist-equipamentos

# Instalar dependências Python
pip install qrcode[pil]

# Executar servidor
python servidor.py
```

## 📁 Estrutura do Projeto
```
checklist-equipamentos/
├── checklist-equipamentos.html    # Aplicação principal
├── servidor.py                     # Servidor HTTP Python
├── iniciar_servidor.bat           # Script Windows
├── parar_servidor.bat             # Script para parar
├── cbm.png                        # Logo da empresa
└── README.md                      # Documentação
```

## 🎨 Screenshots
[Adicionar screenshots da aplicação]

## 🚀 Demo Online
[Link para GitHub Pages se disponível]
