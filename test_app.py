from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_version():
    response = client.get("/version")

    assert response.status_code == 200

    data = response.json()

    assert "name" in data
    assert "version" in data


def test_get_words():
    response = client.get("/words")

    assert response.status_code == 200

    data = response.json()

    assert data["count"] == 5
    assert len(data["words"]) == 5


def test_get_word_by_id():
    response = client.get("/words/1")

    assert response.status_code == 200

    data = response.json()

    assert data["latin"] == "amicus"
    assert data["translation"] == "друг"


def test_get_unknown_word():
    response = client.get("/words/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Word not found"


def test_search_words():
    response = client.get("/search?q=aqua")

    assert response.status_code == 200

    data = response.json()

    assert data["count"] == 1
    assert data["results"][0]["latin"] == "aqua"


def test_quiz_correct_answer():
    response = client.get("/quiz/1?answer=друг")

    assert response.status_code == 200
    assert response.json()["correct"] is True


def test_quiz_wrong_answer():
    response = client.get("/quiz/1?answer=вода")

    assert response.status_code == 200
    assert response.json()["correct"] is False