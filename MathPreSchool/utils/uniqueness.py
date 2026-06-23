class UniqueQuestionGenerator:

    def __init__(self):
        self.used = set()

    def add(self, text):

        if text in self.used:
            return False

        self.used.add(text)
        return True
