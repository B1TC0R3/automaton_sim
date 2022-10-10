'''
This module represents an automaton.
'''
class Automaton:
    '''
    This class represents an automaton.
    It contains:
        - States
        - Initial state
        - Final states
        - Alphabet
        - Operations
    '''
    def __init__(self,
                 states="",
                 initial_state="",
                 final_states="",
                 alphabet="",
                 operations=""):
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.alphabet = alphabet
        self.operations = operations

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)
