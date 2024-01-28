from pytubemp3 import YouTube 
from pytube import Playlist
from moviepy.editor import AudioFileClip
import os
from tkinter import Tk, Label, Entry, Button

class Dowload_audio():
    def __init__(self):
        root = Tk()
        root.grid_rowconfigure(4)
        root.grid_columnconfigure(1)
    
        self.label1 = Label(root, text = "Вставьте ссылку на плейлист")
        self.label1.grid(row = 1,column = 1)
        self.entry1 = Entry(root)
        self.entry1.grid(row = 2,column = 1)
        print(type(self.entry1))
        self.label2 = Label(root, text = "")
        self.label2.grid(row = 3,column = 1)
        but = Button(root, command = self.click_on_button, text ='Начать').grid(row = 4,column = 1) 
        playlist = ''

    def click_on_button(self):
        print(type(self.entry1))
        result = self.check(self.entry1.get())
        print(result)
        if not result:
            return
        else:
            self.get_paths(result)
        
    def check(self, link):
        print(link)
        if "https://www.youtube.com/playlist?list" in link:
            playlist = Playlist(link)
            return playlist
        else:
            self.label2["text"] = "Ссылка не корректна"
            return False
        



    def mov_to_audio(self, path):
        path = path.replace(",","")
        return AudioFileClip(str(path)).to_audiofile(f"{path.replace('.mp4', '')}.mp3")
    
    def get_paths(self, playlist):
        for video in playlist.videos:
            log_list = []
            try:
                self.label2["text"] = f"{video.title}, обработка..."
                video.streams.filter(only_audio=True).first().download()
                self.mov_to_audio(f"{str(video.title)}.mp4")
                log_list.append(f"")
                os.remove(f"{video.title.replace(",","")}.mp4")
            except:
                self.label2["text"] = "видео недоступно для просмотра"

Dowload_audio()   
input()