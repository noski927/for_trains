class MediaPlayer:

    def open(self, filename):
        self.filename = filename
        
    def play(self):
        return f"Воспроизведение {self.filename}"

media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open(filename = 'filemedia1')
media2.open(filename = 'filemedia2')
print(media1.play())
print(media2.play())


