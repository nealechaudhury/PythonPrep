class GetArtist:
    def __init__(self, artist):
        self._artist = artist


    @property
    def artist(self):
        return (self._artist)


    @artist.setter
    def artist(self, newval):
        self._artist = newval





if __name__ == '__main__':
    v = GetArtist('Artist 1')
    print (v.artist)

