"""
Python requests with Pytest API Testing Project

This file contains pytest functions for testing the JSONPlaceholder API,
It uses CRUD operations alongside the requests library to automate API testing
"""

import requests


def test_get(base_url):
    """Test the status code and content type to be correct for a get request and
    also makes sure the response body is valid"""
    response = requests.get(base_url + "/posts")
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    body = response.json()
    for post in body:
        assert post["userId"] is not None
        assert post["id"] is not None
        assert post["title"] is not None
        assert post["body"] is not None


def test_post(base_url):
    """Test the status code and content type to be correct for a post request and
    also makes sure the response body is valid"""
    json_payload = {
    "title": "test_post",
    "body": "test_body",
    "userId": 1
    }

    response = requests.post(base_url + "/posts", json=json_payload)
    assert response.status_code == 201
    assert "application/json" in response.headers["Content-Type"]

    body = response.json()
    assert body["userId"] == 1
    assert body["id"] == 101
    assert body ["title"] == "test_post"
    assert body["body"] == "test_body"


def test_put(base_url):
    """Test the status code and content type to be correct for a put request and
    also makes sure the response body is valid"""
    json_payload = {
    "title": "put_test_post",
    "body": "put_test_body",
    "userId": 1,
    "id": 1
    }

    response = requests.put(base_url + "/posts/1", json=json_payload)
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    body = response.json()
    assert body["userId"] == 1
    assert body["id"] == 1
    assert body["title"] == "put_test_post"
    assert body["body"] == "put_test_body"


def test_patch(base_url):
    """Test the status code and content type to be correct for a patch request and
    also makes sure the response body is valid"""
    json_payload = {
    "title": "patch_test_post"
    }

    response = requests.patch(base_url + "/posts/1", json=json_payload)
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    body = response.json()
    assert body["title"] == "patch_test_post"


def test_delete(base_url):
    """Test the status code and content type to be correct for a delete request and
    also makes sure the response body is valid"""
    response = requests.delete(base_url + "/posts/1")
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    body = response.json()
    assert body == {}