# tests/test_api.py
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

import api
from application import Application
from repository import CharacterRepositoryJsonFile


@pytest.fixture
def client(tmp_path: Path) -> TestClient:
    repo = CharacterRepositoryJsonFile(file_path=tmp_path / "characters.json")
    api._repo = repo
    api._app = Application(repo)
    return TestClient(api.app)


def test_create_and_list_characters(client: TestClient) -> None:
    payload = {
        "name": "Some Character",
        "attributes": {
            "might": 10,
            "agility": 20,
            "vitality": 30,
            "insight": 40,
            "arcana": 50,
            "presence": 60,
        },
    }

    create_resp = client.post("/characters", json=payload)
    assert create_resp.status_code == 201
    created = create_resp.json()
    assert created["id"].startswith("char_")
    assert created["name"] == payload["name"]
    assert created["attributes"]["might"] == 10

    list_resp = client.get("/characters")
    assert list_resp.status_code == 200
    data = list_resp.json()
    assert len(data) == 1
    assert data[0]["id"] == created["id"]


def test_update_character_attributes(client: TestClient) -> None:
    payload = {
        "name": "Another Character",
        "attributes": {
            "might": 1,
            "agility": 2,
            "vitality": 3,
            "insight": 4,
            "arcana": 5,
            "presence": 6,
        },
    }
    create_resp = client.post("/characters", json=payload)
    character_id = create_resp.json()["id"]

    update_payload = {
        "might": 11,
        "agility": 22,
        "vitality": 33,
        "insight": 44,
        "arcana": 55,
        "presence": 66,
    }
    update_resp = client.patch(
        f"/characters/{character_id}/attributes",
        json=update_payload,
    )
    assert update_resp.status_code == 200
    updated = update_resp.json()
    assert updated["id"] == character_id
    assert updated["attributes"]["might"] == 11

    get_one = client.get("/characters", params={"character_id": character_id})
    assert get_one.status_code == 200
    assert get_one.json()[0]["attributes"]["presence"] == 66
