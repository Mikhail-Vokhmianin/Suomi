import pandas as pd
import pytest
from suomi import text_analysis


def test_big5():
    assert text_analysis('I').size == 25


def test_neo():
    assert text_analysis('I', 'neo').size == 150


def test_nonstring():
    with pytest.raises(TypeError):
        text_analysis(1)


def test_empty():
    with pytest.raises(TypeError):
        text_analysis('')
