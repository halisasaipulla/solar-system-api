# from flask import jsonify
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client,two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mars",
        "description": "4th planet",
        "habitable": "False"
    }

def test_create_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Mars",
        "description": "4th planet",
        "habitable": "False"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    # assert "task" in response_body
    assert response_body == "Planet Mars successfully created"
    
    # new_task = Task.query.get(1)
    # assert new_task
    # assert new_task.title == "A Brand New Task"
    # assert new_task.description == "Test Description"
    # assert new_task.completed_at == None

def test_get_not_planet(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == None