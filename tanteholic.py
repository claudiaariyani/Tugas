import time
from threading import Thread
import sys

def aniumate_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  

def sing_lyric(lyric, delay, speed, line_delay=0):
    time.sleep(delay)
    aniumate_text(lyric, speed)
    time.sleep(line_delay)

def sing_song():
    lyrics = [
        ("Tantee...", 0.08),
        ("Sudah terbiasaa terjadi tante..", 0.09),
        ("Teman datang ketika lagi butuh saja...", 0.08),
        ("Coba kalau lagi susah...", 0.15),
        ("Mereka semua menghilanggggg....", 0.15),
    ]
    delays = [0.3, 2.5, 5.8, 9.5, 13.5]         

    thread = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed, 1))
        thread.append(t)
        t.start()
    for t in thread:
        t.join()
sing_song()