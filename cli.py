# cli.py
import sys
from typing import Any

import fire

from application import Application
from dto import (
    CreateCharacterRequestDTO,
    UpdateCharacterAttributesRequestDTO,
    CharacterAttributesDTO,
)
from repository import CharacterRepositoryJsonFile


sys.tracebacklimit = 0  # Hide traceback for cleaner CLI output

ATTRIBUTE_KEYS = {"might", "agility", "vitality", "insight", "arcana", "presence"}


def _normalize_attributes(kwargs: dict[str, Any]) -> dict[str, Any]:
    normalized = {k.lower(): v for k, v in kwargs.items()}
    unknown = set(normalized.keys()) - ATTRIBUTE_KEYS
    if unknown:
        unknown_list = ", ".join(sorted(unknown))
        raise ValueError(f"Unknown attribute(s): {unknown_list}")
    return normalized


class CharacterCLI:
    def __init__(self) -> None:
        repo = CharacterRepositoryJsonFile()
        self.app = Application(repo)

    def create(self, name: str, **kwargs: Any) -> dict[str, Any]:
        attributes = _normalize_attributes(kwargs)
        attributes_dto = CharacterAttributesDTO(**attributes)
        request = CreateCharacterRequestDTO(name=name, attributes=attributes_dto)
        response = self.app.create_character(request)
        return response.model_dump(by_alias=True)

    def update_attributes(self, character_id: str, **kwargs: Any) -> dict[str, Any]:
        attributes = _normalize_attributes(kwargs)
        request = UpdateCharacterAttributesRequestDTO(**attributes)
        response = self.app.update_character_attributes(character_id, request)
        return response.model_dump(by_alias=True)

    def get(self, character_id: str | None = None) -> list[dict[str, Any]]:
        characters = self.app.get_characters(character_id)
        return [c.model_dump() for c in characters]


def main() -> None:
    fire.Fire(CharacterCLI)


if __name__ == "__main__":
    main()
