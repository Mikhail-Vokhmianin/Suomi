import pytest
from suomi import text_analysis


class TestTextAnalysis(object):

    def test_big5(self):
        assert text_analysis('I').size == 25

    def test_neo(self):
        assert text_analysis('I', 'neo').size == 150

    def test_nonstring(self):
        with pytest.raises(TypeError) as exception_info:
            text_analysis(1)
            # Check the error message:
        assert exception_info.match('First argument should be a text with at least 1 character')

    def test_empty(self):
        with pytest.raises(TypeError) as exception_info:
            text_analysis('')
            # Check the error message:
        assert exception_info.match('First argument should be a text with at least 1 character')
