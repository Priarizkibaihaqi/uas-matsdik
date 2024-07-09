class FiniteStateAutomaton:
    def __init__(self):
        self.states = []
        self.transitions = {}
        self.start_state = None
        self.accept_states = set()

    def add_state(self, state, is_accept=False):
        self.states.append(state)
        if is_accept:
            self.accept_states.add(state)

    def set_start_state(self, state):
        self.start_state = state

    def add_transition(self, from_state, to_state, symbol):
        if (from_state, symbol) not in self.transitions:
            self.transitions[(from_state, symbol)] = to_state

    def accepts(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False
        return current_state in self.accept_states

# 1. Definisikan FSA untuk pola "ab*c"
fsa = FiniteStateAutomaton()

# Tambahkan states
fsa.add_state('q0')  # initial state
fsa.add_state('q1')
fsa.add_state('q2', is_accept=True)  # accepting state

# Set start state
fsa.set_start_state('q0')

# Tambahkan transitions
fsa.add_transition('q0', 'q1', 'a')
fsa.add_transition('q1', 'q1', 'b')
fsa.add_transition('q1', 'q2', 'c')

# 2. Implementasikan FSA dalam Python dan 3. Gunakan FSA untuk mendeteksi pola dalam teks
test_strings = ["abc", "abbc", "ac", "a", "abbbc", "abcd"]

for string in test_strings:
    if fsa.accepts(string):
        print(f'The string "{string}" is accepted by the FSA.')
    else:
        print(f'The string "{string}" is not accepted by the FSA.')
