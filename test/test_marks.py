import pytest

@pytest.mark.skip
def test_skip():
    assert False

@pytest.mark.xfail
def test_xfail():
    assert False

@pytest.mark.group1
def test_group1_pass():
    assert True

@pytest.mark.group1
def test_group1_fail():
    assert False

@pytest.mark.group2
def test_group2_pass():
    assert True
