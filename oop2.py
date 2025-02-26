class Playlist:
  def __init__(self, songs, shuffle=False):
    self.songs = songs
    self.index = 0

    if shuffle:
      random.shuffle(self.songs)

  def __iter__(self):
    return self

  def __next__(self):
    if self.index >= len(self.songs):
      raise StopIteration

    print(f"Playing {self.songs[self.index]}")
    self.index += 1

# Create a classic rock playlist using the songs list
songs = ["Hooked on a Feeling", "Yesterday", "Mr. Blue Sky"]
classic_rock_playlist = Playlist(songs, shuffle=True)

while True:
    try:
        next(classic_rock_playlist)
    except StopIteration:
        break