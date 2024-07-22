class FiniteStateAutomaton:
    def __init__(self):
        self.start_state = 'q0'
        self.accept_state = 'q2'
        self.current_state = self.start_state
        self.transitions = {
            'q0': {'a': 'q1'},
            'q1': {'b': 'q2'},
            'q2': {'a': 'q1'}
        }
    def reset(self):
        self.current_state = self.start_state
    def process_input(self, input_string):
        self.reset()
        for char in input_string:
            if char in self.transitions[self.current_state]:
                self.current_state = self.transitions[self.current_state][char]
            else:
                self.current_state = self.start_state if char == 'a' else 'q0'
    def is_accepting(self):
        return self.current_state == self.accept_state
if __name__ == "__main__":
    fsa = FiniteStateAutomaton()
    test_strings = ['ab', 'aab', 'babab', 'bbab', 'aabb', 'abc']    
    for s in test_strings:
        fsa.process_input(s)
        if fsa.is_accepting():
            print(f'The string "{s}" is accepted.')
        else:
            print(f'The string "{s}" is not accepted.')
