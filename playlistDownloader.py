import yt_dlp

playlist_url = "https://www.youtube.com/playlist?list=SEU_ID_AQUI"

opcoes = {
    'format': 'bestaudio/best',
    'outtmpl': 'musicas/%(title)s.%(ext)s',
    'quiet': False,
    'ignoreerrors': True,
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
