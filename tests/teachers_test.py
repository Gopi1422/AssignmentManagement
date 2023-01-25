def test_get_assignments_teacher_1(client, h_teacher_1):
    """
    success case: list all assignments submitted to teacher 1
    """
    response = client.get(
        '/teacher/assignments',
        headers=h_teacher_1
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['teacher_id'] == 1
        assert assignment['state'] == 'SUBMITTED'


def test_get_assignments_teacher_2(client, h_teacher_2):
    """
    success case: list all assignments submitted to teacher 2
    """
    response = client.get(
        '/teacher/assignments',
        headers=h_teacher_2
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['teacher_id'] == 2
        assert assignment['state'] == 'SUBMITTED'


def test_grade_assignment_teacher_2(client, h_teacher_2):
    """
    success case: assignment is graded by corresponded teacher.
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_2,
        json={
            'id': 2,
            'grade': 'A'
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['teacher_id'] == 2
    assert data['state'] == 'GRADED'
    assert data['grade'] == 'A'


def test_grade_assignment_cross(client, h_teacher_2):
    """
    failure case: assignment 1 was submitted to teacher 1 and not teacher 2
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_2,
        json={
            "id": 1,
            "grade": "A"
        }
    )

    error_response = response.json
    assert response.status_code == 400
    assert error_response['error'] == 'FyleError'
    assert error_response["message"] == 'This assignment submitted to some other teacher'


def test_grade_assignment_bad_grade(client, h_teacher_1):
    """
    failure case: API should not allow only grades available in enum
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": 1,
            "grade": "AB"
        }
    )

    error_response = response.json
    assert response.status_code == 400
    assert error_response['error'] == 'ValidationError'


def test_grade_assignment_bad_assignment(client, h_teacher_1):
    """
    failure case: If an assignment does not exists check and throw 404
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": 100000,
            "grade": "A"
        }
    )

    error_response = response.json
    assert response.status_code == 404
    assert error_response['error'] == 'FyleError'
    assert error_response["message"] == 'No assignment with this id was found'


def test_grade_assignment_draft_assignment(client, h_teacher_1):
    """
    failure case: only a submitted assignment can be graded
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1, json={
            "id": 5,
            "grade": "A"
        }
    )

    error_response = response.json
    assert response.status_code == 400
    assert error_response['error'] == 'FyleError'
    assert error_response["message"] == 'Only assignment in submitted state can be graded!'


def test_grade_assignment_graded_assignment(client, h_teacher_2):
    """
    failure case: once assignment is graded, it can't be graded again.
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_2, json={
            "id": 2,
            "grade": "A"
        }
    )

    error_response = response.json
    assert response.status_code == 400
    assert error_response['error'] == 'FyleError'
    assert error_response["message"] == 'Assignment is already graded!'
