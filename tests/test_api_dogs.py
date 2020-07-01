import requests
import pytest
import random

@pytest.fixture
def baseUrl():
    return "https://dog.ceo/api/"


@pytest.fixture
def breed():
    return "retriever"


subBreed = ""


def test_get_a_list_all_breeds(baseUrl, breed):

    resp = requests.get(baseUrl + "breeds/list/all")
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
    assert resp.json()['message'][breed] is not None
    print(resp.json())


def test_get_a_list_of_sub_breeds(baseUrl, breed):

    resp = requests.get(baseUrl + "breed/" + breed + "/list")
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
    assert len(resp.json()['message']) > 0
    print(resp.json())


def test_get_a_random_image(baseUrl, breed):

    resp = requests.get(baseUrl + "breed/" + breed + "/"+subBreed+"/images/random")
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
    assert len(resp.json()['message']) > 0
    print(resp.json())


