import pytest
import allure
import requests

@allure.title("Verify Get Request for Restful Booker")
@allure.description("This is a happy path test case verify for booking id 2")
@pytest.mark.positive
def test_main_getrequest_positive():
    URL="https://restful-booker.herokuapp.com/booking/2"
    responseData=requests.get(url=URL)
    print(responseData.text)
    assert responseData.status_code==200
    #/assert requests.get("https://restful-booker.herokuapp.com/booking/1").status_code==200 not preferred

@allure.title("Verify Get Request for Restful Booker")
@allure.description("This is to verify for booking id invalid -1")
@pytest.mark.negative
def test_main_getrequest_negative():
    URL="https://restful-booker.herokuapp.com/booking/-1"
    responseData=requests.get(url=URL)
    print(responseData.text)
    assert responseData.status_code==404 #/Bad Request