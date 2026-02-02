# application.py
from enum import StrEnum
from typing import Iterable

from nanoid import generate

from dto import (
    CreateCharacterRequestDTO,
    CreateCharacterResponseDTO,
    UpdateCharacterAttributesRequestDTO,
    UpdateCharacterResponseDTO,
    CharacterAttributesDTO
)
from domain import Character, CharacterAttributes, CharacterID
from repository import CharacterRepositoryJsonFile

ID_SIZE = 12  # must match CharacterID pattern (^char_.{12}$)


class IDPrefix(StrEnum):
    CHARACTER = "char"


def generate_id(prefix: IDPrefix) -> str:
    return f"{prefix}_{generate(size=ID_SIZE)}"


class Application:
    def __init__(self, repo: CharacterRepositoryJsonFile) -> None:
        self.repo = repo

    def create_character(self, req: CreateCharacterRequestDTO) -> CreateCharacterResponseDTO:
        new_id: CharacterID = generate_id(IDPrefix.CHARACTER)  # type: ignore[assignment]

        character = Character(
            id=new_id,
            name=req.name,
            health=100,
            attributes=CharacterAttributes.model_validate(req.attributes.model_dump()),
        )

        self.repo.add(character)

        return CreateCharacterResponseDTO(
            id=character.id,
            name=character.name,
            health=character.health,
            attributes=req.attributes,
        )

    def update_character_attributes(
        self,
        character_id: CharacterID,
        req: UpdateCharacterAttributesRequestDTO,
    ) -> UpdateCharacterResponseDTO:
        character = self.repo.get_by_id(character_id)
        if character is None:
            raise KeyError("Character not found")

        updated = character.model_copy(
            update={
                "attributes": CharacterAttributes.model_validate(
                    character.attributes.model_dump()
                    | req.model_dump(exclude_unset=True)
                )
            }
        )

        self.repo.update(updated)

        return UpdateCharacterResponseDTO(
            id=updated.id,
            name=updated.name,
            health=updated.health,
            attributes=CharacterAttributesDTO.model_validate(updated.attributes),
        )

    def get_characters(self, character_id: CharacterID | None = None) -> Iterable[Character]:
        if character_id is not None:
            character = self.repo.get_by_id(character_id)
            if character is None:
                raise KeyError("Character not found")
            return [character]
        return self.repo.list_all()
