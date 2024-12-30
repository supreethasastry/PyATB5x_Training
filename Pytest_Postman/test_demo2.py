import pytest

@pytest.mark.smoke
def test_main_method1():
    print("Valid Pass method")

@pytest.mark.smoke
def test_main_method2():
    print("Invalid Fail method")
    assert 1+1==3