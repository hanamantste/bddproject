import random
import pytest
import requests
import json
import string

base_url ="https://gorest.co.in"
auth_token = "Bearer c2a14004e9754aaec57735cfa27f145c2b57e74800832cb53ebcd6b51d1b1c5a"

def email_id():
    email_len = 10
    email_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_len))
    return email_string+"@gmail.com"

print(email_id())

@pytest.mark.skip
def test_get_api():
    # base_url = "https://gorest.co.in"
    url = base_url+"/public/v2/users/"
    headers = {"Authorization":auth_token}
    response = requests.get(url=url,headers=headers)
    assert response.status_code==200
    data = response.json()
    json_data = json.dumps(data,indent=5)
    # print(json_data)


def test_post_api():
    # auth_token = "Bearer c2a14004e9754aaec57735cfa27f145c2b57e74800832cb53ebcd6b51d1b1c5a"
    url = base_url + "/public/v2/users/"
    headers = {"Authorization": auth_token}
    data ={
          "id": 82639941,
          "name": "TestQA",
          "email": email_id(),
          "gender": "female",
          "status": "active"
    }
    response = requests.post(url=url,json=data, headers=headers)
    assert response.status_code == 201
    data = response.json()
    json_data = json.dumps(data, indent=5)
    # email_1  = email_id()
    assert data['name']=='TestQA'
    # print(data['id'])
    return data['id']

def put_api(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    headers = {"Authorization": auth_token}
    data = {
        "name": "TestQA",
        "email": email_id(),
        "gender": "female",
        "status": "active"
    }
    response = requests.put(url=url, json=data, headers=headers)
    assert response.status_code == 200
    data = response.json()
    json_data = json.dumps(data, indent=5)
    # email_1  = email_id()
    assert data['name'] == 'TestQA'
    # print(json_data)

def test_put_api():
    put_api(8265574)

def delete_api(user_id,status_code):
    url = base_url + f"/public/v2/users/{user_id}"
    headers = {"Authorization": auth_token}
    response = requests.delete(url=url, headers=headers)
    assert response.status_code == status_code


def test_delete_api():
    test_get_api()
    user_id = test_post_api()
    put_api(user_id)
    delete_api(user_id,204)