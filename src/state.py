from operation import Operation
from errors import UndefinedOperationError

class State:
    def __init__(self, name, operations=[]):
        self.name = name
        self.operations = operations

    def add_operation(self, letter, to_state):
        operation = Operation(self, letter, to_state)
        self.operations.append(operation)

        return self

    def input(self, letter):
        operation = self._get_operation(letter)

        if not operation:
            raise UndefinedOperationError(self.name, letter)

        return operation

    def _get_operation(self, letter):
        for operation in self.operations:
            if operation.name == letter:
                return operation
