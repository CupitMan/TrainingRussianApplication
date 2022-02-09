class SpellingWord:
    def __init__(self, word: str):

        self.word = word
        self.name = self.word.lower()

        for i in word:
            if i != i.lower():
                self.spell = word.index(i)

        self.number = self.spell + 1
