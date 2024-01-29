import yt_dlp as youtube_dl
while True:
    try:
        def download_audio_from_channel(channel_url):
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([channel_url])

        # Пример использования скрипта:
                
        channel_url = input('Введите ссылку на канал: ')
        download_audio_from_channel(channel_url)
    except Exception as exception:
        print(exception)