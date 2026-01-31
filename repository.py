# repository.py
from pathlib import Path
from typing import Final
import json

from pydantic import TypeAdapter, ValidationError

from domain import Character, CharacterID, CharacterHealth
from dto import CharacterBaseDTO


CHARACTERS_FILE: Final = Path("characters.json")


class CharacterSchema(CharacterBaseDTO):
    id: CharacterID
    health: CharacterHealth


class CharacterRepositoryJsonFile:
    _adapter = TypeAdapter(list[CharacterSchema])

    def __init__(self, file_path: Path = CHARACTERS_FILE) -> None:
        self.file_path = file_path

    def list_all(self) -> list[Character]:
        schemas = self._read_validated()
        return [Character.model_validate(s.model_dump()) for s in schemas]

    def get_by_id(self, character_id: CharacterID) -> Character | None:
        return next((c for c in self.list_all() if c.id == character_id), None)

    def add(self, character: Character) -> None:
        schemas = self._read_validated()
        schemas.append(CharacterSchema.model_validate(character))
        self._write_validated(schemas)

    def update(self, character: Character) -> None:
        schemas = self._read_validated()
        updated = CharacterSchema.model_validate(character)

        for i, s in enumerate(schemas):
            if s.id == updated.id:
                schemas[i] = updated
                break

        self._write_validated(schemas)

    def delete(self, character_id: CharacterID) -> None:
        schemas = self._read_validated()
        schemas = [s for s in schemas if s.id != character_id]
        self._write_validated(schemas)

    def _read_raw(self) -> list[dict]:
        if not self.file_path.exists():
            return []
        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("characters.json must contain a JSON array")
        return data

    def _read_validated(self) -> list[CharacterSchema]:
        raw = self._read_raw()
        try:
            return self._adapter.validate_python(raw)
        except ValidationError as e:
            raise ValueError(f"Invalid characters.json: {e}") from e

    def _write_validated(self, schemas: list[CharacterSchema]) -> None:
        raw = [s.model_dump(mode="json", by_alias=True) for s in schemas]
        self._write_raw(raw)

    def _write_raw(self, data: list[dict]) -> None:
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
