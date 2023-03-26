""" Test greets function """

from suomi import greets


def test_greets():
    expected_output = 'Vasya!'
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output

    greets('Vasya')
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip()[-6:] == expected_output
