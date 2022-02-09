class AccentWord:
    def __init__(self, word):
        self.word = word
        self.name = word.lower()
        self.index_stress = self.__get_stress()
        self.number_stress = self.index_stress + 1

    def __get_stress(self):
        for symbol in range(len(self.word)):
            if self.word[symbol].upper() == self.word[symbol]:
                return symbol