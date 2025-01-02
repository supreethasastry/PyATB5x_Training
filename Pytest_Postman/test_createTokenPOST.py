import pytest
import allure
import requests

base_url="https://restful-booker.herokuapp.com"
headers={
    "Content-Type" :"application/json"}

def test_create_token():
    base_path="/auth"
    full_url=base_url+base_path
    json={
        "username" : "admin",
        "password" : "password123"
    }
    responseData=requests.post(url=full_url,headers=headers, json=json)
    assert responseData.status_code==200
    responseData_json = responseData.json()
    token = responseData_json["token"]
    print(token)
    assert type(token)==str
    assert len(token)>0