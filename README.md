# 🎵 YouTube Playlist MP3 Downloader (yt-dlp)

Este é um script Python simples que baixa todos os vídeos de uma playlist do YouTube e os converte automaticamente em arquivos `.mp3` de alta qualidade, salvando-os na pasta padrão de **Downloads** do seu sistema.

---

## ✅ Requisitos Obrigatórios

1. **Python 3.8+**

   * Baixe e instale em: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   * Certifique-se de marcar a opção **Add Python to PATH** (Windows).

2. **yt-dlp**

   * Ferramenta para download do YouTube.
   * Instale com:

     ```bash
     pip install yt-dlp
     ```

3. **FFmpeg** (**obrigatório**)

   * Necessário para converter o áudio em MP3 e garantir qualidade.
   * **Windows**:

     1. Baixe uma build em: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
     2. Extraia o conteúdo e adicione a pasta `bin` ao PATH do sistema.
   * **Linux (Debian/Ubuntu)**:

     ```bash
     sudo apt update
     sudo apt install ffmpeg -y
     ```
   * **macOS** (Homebrew):

     ```bash
     brew install ffmpeg
     ```
   * **Android (Termux)**:

     ```bash
     pkg update && pkg upgrade
     pkg install ffmpeg python
     pip install yt-dlp
     ```

---

## 🌐 Plataformas e Execução

### 🖥️ Windows

1. Abra o **PowerShell** ou **Prompt de Comando**.
2. Clone ou copie este repositório.
3. Instale o yt-dlp e verifique o FFmpeg:

   ```powershell
   pip install yt-dlp
   ffmpeg -version
   ```
4. Salve o script (veja abaixo) em um arquivo chamado `baixar.py`.
5. Execute:

   ```powershell
   python baixar.py
   ```

### 🐧 Linux

1. Abra o terminal.
2. Instale dependências:

   ```bash
   sudo apt update
   sudo apt install python3 python3-pip ffmpeg -y
   pip install yt-dlp
   ```
3. Salve o script como `baixar.py`.
4. Execute:

   ```bash
   python3 baixar.py
   ```

### 📱 Android (Termux)

1. Abra o **Termux**.
2. Atualize e instale pacotes:

   ```bash
   pkg update && pkg upgrade
   pkg install python ffmpeg
   pip install yt-dlp
   ```
3. Crie o script:

   ```bash
   nano baixar.py
   ```

   Cole o conteúdo e salve com `CTRL+X`, `Y`.
4. Execute:

   ```bash
   python baixar.py
   ```

---

## 📄 Script `baixar.py`

```python
import yt_dlp

# Insira o ID da playlist abaixo:
playlist_url = "https://www.youtube.com/playlist?list=SEU_ID_AQUI"

opcoes = {
    'format': 'bestaudio/best',
    'outtmpl': 'musicas/%(title)s.%(ext)s',
    'quiet': False,
    'ignoreerrors': True,  # Ignora vídeos que não podem ser baixados
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'noplaylist': False
}

with yt_dlp.YoutubeDL(opcoes) as ydl:
    ydl.download([playlist_url])

print("✅ Download finalizado (os vídeos com erro foram ignorados).")
```

**Observações**:

* Os arquivos serão salvos na pasta `musicas/` criada automaticamente no diretório do script.
* Se preferir salvar na pasta Downloads do sistema, edite `outtmpl` para:

  ```python
  'outtmpl': '~/Downloads/musicas/%(title)s.%(ext)s'
  ```
