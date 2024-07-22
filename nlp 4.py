class PluralizerFSM:
    def __init__(self):
        self.transitions = {
            'default': self.default_plural,
            's': self.add_es,
            'x': self.add_es,
            'z': self.add_es,
            'sh': self.add_es,
            'ch': self.add_es,
            'y': self.change_y_to_ies
        }
    
    def default_plural(self, word):
        return word + 's'
    
    def add_es(self, word):
        return word + 'es'
    
    def change_y_to_ies(self, word):
        if word[-2] not in 'aeiou':
            return word[:-1] + 'ies'
        else:
            return word + 's'
    
    def pluralize(self, word):
        if word[-1] in self.transitions:
            return self.transitions[word[-1]](word)
        elif word[-2:] in self.transitions:
            return self.transitions[word[-2:]](word)
        elif word[-1] == 'y':
            return self.transitions['y'](word)
        else:
            return self.default_plural(word)
if __name__ == "__main__":
    words = ['cat', 'dog', 'box', 'buzz', 'dish', 'church', 'baby', 'day']
    fsm = PluralizerFSM()
    
    for word in words:
        plural = fsm.pluralize(word)
        print(f"{word} -> {plural}")
