import pytest
import allure

@allure.title("Create Booking Positive test case")
@allure.description("This test case verifies valid positive scenario for create booking")
@pytest.mark.positive
def test_main_createbooking():
    print("Postive test case")
    assert 1-1==2

@allure.title("Create Booking Negative test case")
@allure.description("This test case verifies valid negative scenario for create booking")
@pytest.mark.negative
def test_main_createbooking_neg1():
    print("Negative1 test case")
    assert 1+1==2

@allure.title("Create Booking Positive test case")
@allure.description("This test case verifies valid negative scenario for create booking")
@pytest.mark.negative
def test_main_createbooking_neg2():
    print("Negative2 test case")
    assert 1+1==2

