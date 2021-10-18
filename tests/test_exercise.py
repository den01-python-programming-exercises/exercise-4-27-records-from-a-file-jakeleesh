import pytest
import src.exercise
import os

def test_exercise():
    os.chdir('src')
    
    input_values = ["data.txt"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["Name of the file:","lily, age: 3 years","anton, age: 5 years","levi, age: 4 years","amy, age: 1 year"]
