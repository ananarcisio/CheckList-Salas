# 📱 COMO ACESSAR CHECKLIST NO CELULAR

## 🚀 MÉTODO 1: SERVIDOR LOCAL (RECOMENDADO)

### 1️⃣ Iniciar Servidor
```
📁 Clique duas vezes em: iniciar_servidor.bat
```

### 2️⃣ Resultado
```
🚀 SERVIDOR CHECKLIST INICIADO!
==================================================
📱 Acesse no celular: http://10.50.4.22:8000/checklist-equipamentos.html
💻 Acesse no PC: http://localhost:8000/checklist-equipamentos.html
==================================================
✅ QR Code gerado! Escaneie para acessar no celular
🛑 Para parar o servidor: Ctrl+C
```

### 3️⃣ Acessar no Celular
- **Opção A**: Escanear QR Code gerado (arquivo `qrcode_checklist.png`)
- **Opção B**: Digitar URL no navegador do celular
- **Opção C**: Enviar link por WhatsApp/Email para si mesmo

---

## 🌐 MÉTODO 2: HOSPEDAGEM ONLINE

### GitHub Pages (Gratuito)
1. Criar conta no GitHub
2. Criar repositório público
3. Upload do arquivo HTML
4. Ativar GitHub Pages
5. Acessar URL: `https://seuusuario.github.io/repositorio/checklist-equipamentos.html`

### Netlify (Gratuito)
1. Acessar netlify.com
2. Arrastar pasta do projeto
3. Receber URL automático
4. Acessar de qualquer lugar

---

## 📋 REQUISITOS

### Para Servidor Local:
- ✅ Python instalado
- ✅ Celular e PC na mesma rede WiFi
- ✅ Firewall liberado (porta 8000)

### Para Hospedagem Online:
- ✅ Conexão com internet
- ✅ Conta no serviço escolhido

---

## 🔧 SOLUÇÃO DE PROBLEMAS

### Celular não acessa servidor local:
1. **Verificar rede**: PC e celular na mesma WiFi
2. **Firewall**: Liberar porta 8000 no Windows
3. **IP correto**: Usar IP mostrado no terminal

### QR Code não funciona:
1. **Instalar dependência**: `pip install qrcode[pil]`
2. **Usar URL manual**: Copiar link do terminal
3. **Câmera**: Usar app leitor QR Code

### Servidor não inicia:
1. **Python**: Instalar de python.org
2. **Porta ocupada**: Fechar outros servidores
3. **Permissões**: Executar como administrador

---

## 💡 DICAS

### Produtividade:
- 📌 **Favoritar** URL no celular
- 🔖 **Adicionar à tela inicial** como app
- 📱 **Modo offline**: Funciona após carregar uma vez

### Segurança:
- 🔒 **Rede local**: Dados não saem da sua rede
- 💾 **Backup**: Exportar dados regularmente
- 🛡️ **Firewall**: Fechar servidor quando não usar