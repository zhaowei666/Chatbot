

class Bot:
    def __init__(self):
        self.input = ''

    def get_response(self, text):
        self.input = text
        if 'a' in text:
            return 'a'
