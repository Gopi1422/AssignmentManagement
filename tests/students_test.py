def test_get_assignments_student_1(client, h_student_1):
    """
    success case: List all student 1's created assignments
    """
    response = client.get(
        '/student/assignments',
        headers=h_student_1
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 1


def test_get_assignments_student_2(client, h_student_2):
    """
    success case: List all student 2's created assignments
    """
    response = client.get(
        '/student/assignments',
        headers=h_student_2
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['student_id'] == 2


def test_post_assignment_student_1(client, h_student_1):
    """
    success case: create a draft assignment
    """
    content = 'ABCD TESTPOST'

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'content': content
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['content'] == content
    assert data['state'] == 'DRAFT'
    assert data['teacher_id'] is None


def test_edit_assignment_student_1(client, h_student_1):
    """
    success case: edit a draft assignment
    """
    content = 'ABCD TESTPOST EDIT'

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'id': 2,
            'content': content
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['content'] == content
    assert data['state'] == 'DRAFT'
    assert data['teacher_id'] is None


def test_edit_assignment_submitted_assignment(client, h_student_1):
    """
    failure case: only draft assignment can be edited
    """
    content = 'ABCD TESTPOST EDIT'

    response = client.post(
        '/student/assignments',
        headers=h_student_1,
        json={
            'id': 1,
            'content': content
        })

    error_response = response.json
    assert response.status_code == 400
    assert error_response['error'] == 'FyleError'
    assert error_response["message"] == 'only assignment in draft state can be edited'


def test_submit_assignment_student_1(client, h_student_1):
    """
    success case: submit a draft assignment to a teacher
    """
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': 2,
            'teacher_id': 2
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['student_id'] == 1
    assert data['state'] == 'SUBMITTED'
    assert data['teacher_id'] == 2


def test_assingment_resubmitt_error(client, h_student_1):
    """
    failure case: once assignment is submitted, it can't be submitted again
    """
    response = client.post(
        '/student/assignments/submit',
        headers=h_student_1,
        json={
            'id': 2,
            'teacher_id': 2
        })
    error_response = response.json
    assert response.status_code == 400
    assert error_response['error'] == 'FyleError'
    assert error_response["message"] == 'only a draft assignment can be submitted'
