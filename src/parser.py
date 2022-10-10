'''
This module can parse an automaton from a .auto file
'''
from automaton import Automaton

_COMMENT_CHAR = "#"

_BLOCK_DESCRIPTORS = {
        "states": "Q",
        "initial_state": "q",
        "alphabet": "S",
        "operations": "s",
        "final_states": "F",
        # "output_alphabet": "L",
        # "ouput_operations": "l"
        }

_IGNORED_CHARS = [
        " ",
        "\n",
        "\t",
        ]

def parse(path) -> Automaton:
    '''
    Parse the file at 'path' into an automaton

    :param path: file path (.auto)
    :returns: an object of type Automaton
    '''
    automaton = Automaton()

    with open(path, 'r', encoding="utf-8") as file:
        script = file.read()
        script = _simplify(script)

        for name, letter in _BLOCK_DESCRIPTORS.items():
            block_begin = script.find(f"{letter}<", 0, len(script)) + 2
            block_end = script.find(f">{letter}", 0, len(script)) - 2

            block_content = script[block_begin:block_end]

            if name == "initial_state":
                automaton[name] = block_content

            elif name in ("states", "final_states", "alphabet", "operations"):
                automaton[name] = _as_list(block_content)


def _simplify(script) -> str:
    script = _remove_comments(script)

    for char in _IGNORED_CHARS:
        script.remove(char)

    return script

def _remove_comments(script) -> str:
    while _COMMENT_CHAR in script:
        comment_begin = script.find("#", 0, len(script)) - 1
        comment_end = script.find("\n", comment_begin, len(script))

        script = script[:comment_begin] + script[comment_end:]

    return script

def _as_list(string):
    return string.split(",")
