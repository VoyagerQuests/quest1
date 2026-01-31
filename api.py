# api.py
from typing import Annotated

from fastapi import FastAPI, Query, Path

from application import Application
from dto import (
    CreateCharacterRequestDTO,
    CreateCharacterResponseDTO,
    UpdateCharacterAttributesRequestDTO,
    UpdateCharacterResponseDTO,
)
from domain import CharacterID, Character
from repository import CharacterRepositoryJsonFile


app = FastAPI(title="Characters API")

# Thin wiring: construct dependencies once
_repo = CharacterRepositoryJsonFile()
_app = Application(_repo)


@app.post("/characters", response_model=CreateCharacterResponseDTO, status_code=201)
def create_character(
    payload: CreateCharacterRequestDTO,
) -> CreateCharacterResponseDTO:
    return _app.create_character(payload)


@app.patch(
    "/characters/{character_id}/attributes",
    response_model=UpdateCharacterResponseDTO,
)
def update_character_attributes(
    character_id: Annotated[CharacterID, Path(...)],
    payload: UpdateCharacterAttributesRequestDTO,
) -> UpdateCharacterResponseDTO:
    return _app.update_character_attributes(character_id, payload)


@app.get("/characters", response_model=list[Character])
def get_characters(
    character_id: Annotated[CharacterID | None, Query()] = None,
) -> list[Character]:
    return list(_app.get_characters(character_id))
