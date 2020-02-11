class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

mmitw = Song(["I have seen what the darkness does",
              "Say goodbye to who I was",
              "I ain't ever been away so long",
              "Don't look back them days are gone",
              "Follow me into the endless night",
              "I can bring your fears to life",
              "Show me yours and I'll show you mine",
              "Meet me in the woods tonight"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

mmitw.sing_me_a_song()
