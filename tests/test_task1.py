""" Test greets function """
import io
import sys
from suomi import greets


class TestGreets(object):

    # if we want to skip this test for the python version below 2.7
    # @pytest.mark.skipif(sys.version_info > (2, 7), reason="requires Python 2.7")
    def test_greets(self):
        expected_output = 'Vasya!'
        captured_output = io.StringIO()
        sys.stdout = captured_output

        greets('Vasya')
        sys.stdout = sys.__stdout__
        assert captured_output.getvalue().strip()[-6:] == expected_output
