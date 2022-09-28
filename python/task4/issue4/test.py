import one_hot_encoder as ohe
import pytest


def test_empty():
    ft = ohe.fit_transform([])
    assert ft == []


def test_invalid_input():
    with pytest.raises(TypeError):
        ohe.fit_transform(1)


def test_res_type():
    ft = ohe.fit_transform('A', 'B', 'C', 'D')
    assert isinstance(ft, list)


@pytest.mark.parametrize('data, target_ft', [
    (['promitto', 'me', 'laboraturum', 'esse', 'non', 'sordidi', 'lucri',
      'causa'], [
         ('promitto', [0, 0, 0, 0, 0, 0, 0, 1]),
         ('me', [0, 0, 0, 0, 0, 0, 1, 0]),
         ('laboraturum', [0, 0, 0, 0, 0, 1, 0, 0]),
         ('esse', [0, 0, 0, 0, 1, 0, 0, 0]),
         ('non', [0, 0, 0, 1, 0, 0, 0, 0]),
         ('sordidi', [0, 0, 1, 0, 0, 0, 0, 0]),
         ('lucri', [0, 1, 0, 0, 0, 0, 0, 0]),
         ('causa', [1, 0, 0, 0, 0, 0, 0, 0])
     ])])
def test_simple(data, target_ft):
    ft = ohe.fit_transform(data)
    assert ft == target_ft
