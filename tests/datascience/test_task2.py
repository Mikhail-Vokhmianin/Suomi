""" Test functions related to the Sentino API usage"""

import pytest
from suomi import sentino_test_results


class TestSentinoTestResults(object):

    def test_big5(self):
        assert sentino_test_results('I').size == 25

    def test_neo(self):
        assert sentino_test_results('I', 'neo').size == 150

    def test_nonstring(self):
        with pytest.raises(TypeError) as exception_info:
            sentino_test_results(1)
            # Check the error message:
        assert exception_info.match('First argument should be a text with at least 1 character')

    def test_empty(self):
        with pytest.raises(TypeError) as exception_info:
            sentino_test_results('')
            # Check the error message:
        assert exception_info.match('First argument should be a text with at least 1 character')


@pytest.mark.xfail(reason="The function cluster_analysis() is yet to be done")
class TestClusterAnalysis(object):

    def test_required_data_type(self):
        test_argument = "some text"
        with pytest.raises(TypeError) as exception_info:
            cluster_analysis(test_argument)
        expected_error_msg = "The argument of the function cluster_analysis() have to be type string "
        assert exception_info.match(expected_error_msg)
