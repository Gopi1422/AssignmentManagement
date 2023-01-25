def test_server_ready(client):
    """
    success case: check that the server status is ready
    """
    response = client.get(
        '/',
    )

    assert response.status_code == 200
    response = response.json
    assert response['status'] == 'ready'


def test_authentication(client):
    """
    failure case: request header without principal is unauthorized
    """
    response = client.get(
        '/student/assignments',
    )

    error_response = response.json
    assert response.status_code == 401
    assert error_response['error'] == 'FyleError'
    assert error_response["message"] == 'principal not found'


def test_principal(client, h_teacher_1):
    """
    failure case: requester is a student, but principal header value does not contain student_id
    """
    response = client.get(
        '/student/assignments',
        headers=h_teacher_1
    )

    error_response = response.json
    assert response.status_code == 403
    assert error_response['error'] == 'FyleError'
    assert error_response["message"] == 'requester should be a student'


def test_api(client, h_student_1):
    """
    failure case: requested api is not available or not found
    """
    response = client.get(
        '/students/assignments',
        headers=h_student_1
    )

    error_response = response.json
    assert response.status_code == 404
    assert error_response['error'] == 'NotFound'
