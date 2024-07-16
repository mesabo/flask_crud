# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/15
🚀 Welcome to the Awesome Python Script 🚀

User: mesabo
Email: mesabo18@gmail.com / messouaboya17@gmail.com
Github: https://github.com/mesabo
Univ: Hosei University
Dept: Science and Engineering
Lab: Prof YU Keping's Lab
"""

import json
from io import BytesIO
from datetime import datetime

def test_get_users(client):
    response = client.get('/users/')
    assert response.status_code == 200

def test_add_user(client, test_data):
    user_data = test_data['user']
    response = client.post('/users/', data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 201
    data = json.loads(response.data.decode())
    assert 'message' in data

def test_get_user(client, test_data):
    user_data = test_data['user']
    post_response = client.post('/users/', data=json.dumps(user_data), content_type='application/json')
    user_id = json.loads(post_response.data.decode())['message'].split()[-1]

    response = client.get(f'/users/{user_id}/')
    assert response.status_code == 200
    user = json.loads(response.data.decode())
    assert user['username'] == user_data['username']

def test_update_user(client, test_data):
    user_data = test_data['user']
    post_response = client.post('/users/', data=json.dumps(user_data), content_type='application/json')
    user_id = json.loads(post_response.data.decode())['message'].split()[-1]

    updated_data = user_data.copy()
    updated_data['fullname'] = 'Updated Test User'
    response = client.put(f'/users/{user_id}/', data=json.dumps(updated_data), content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert 'message' in data

def test_delete_user(client, test_data):
    user_data = test_data['user']
    post_response = client.post('/users/', data=json.dumps(user_data), content_type='application/json')
    user_id = json.loads(post_response.data.decode())['message'].split()[-1]

    response = client.delete(f'/users/{user_id}/')
    assert response.status_code == 200
    data = json.loads(response.data.decode())
    assert 'message' in data

def test_upload_csv(client):
    data = (
        "username,fullname,email,phone,address.street,address.city,address.state,address.zipcode,address.country,is_active,created_at,updated_at\n"
        "test_user_csv,Test User CSV,test.user.csv@example.com,1234567893,123 CSV St,CSV City,CS,12346,CSVland,true,2024-07-14 20:00:00,2024-07-14 20:00:00\n"
    )
    response = client.post('/users/upload_csv', content_type='multipart/form-data', data={
        'file': (BytesIO(data.encode('utf-8')), 'test.csv')
    })
    assert response.status_code == 201
    data = json.loads(response.data.decode())
    assert data['message'] == 'CSV content uploaded and saved successfully'

def test_download_csv(client):
    response = client.get('/users/download_csv')
    assert response.status_code == 200
    assert response.content_type == 'text/csv; charset=utf-8'
