class UndefinedOperationError (Exception):
    def __init__(self, current_state, letter):
        super(f"The current state ({current_state}) does not have a"+\
               "operation corresponding to the letter '{letter}'.")
