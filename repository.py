from pathlib import Path
from typing import Final
from domain import Character
from domain import CharacterID
import json

CHARACTERS_FILE: Final = Path("characters.json")

class CharacterRepositoryJsonFile:
    def __init__(self, file_path: Path = CHARACTERS_FILE) -> None:
        self.file_path = file_path

    def list_all(self) -> list[Character]:
        """List all characters from the JSON file"""
        return [
            Character.model_validate(item)
            for item in self._read_raw()
        ]
        
    def get_by_id(self, character_id: CharacterID) -> Character | None:
        """Get a character by ID from the JSON file"""
        return next(
            (char for char in self.list_all() if char.id == character_id),
            None, 
        )
    
    def add(self, character: Character) -> None:
        """Add a new character to the JSON file"""
        data = self._read_raw()
        data.append(character.model_dump())
        self._write_raw(data)

    def update(self, character: Character) -> None:
        """Update an existing character in the JSON file"""
        data = self._read_raw()
        for index, item in enumerate(data):
            if item["id"] == character.id:
                data[index] = character.model_dump()
                break
        self._write_raw(data)

    def delete(self, character_id: CharacterID) -> None:
        """Delete a character by ID from the JSON file"""
        data = [c for c in self._read_raw() if c["id"] != character_id
        ]
        self._write_raw(data)


    # -------- Helper methods


    def _read_raw(self) -> list[dict]:
        if not self.file_path.exists():
            return []
        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("characters.json must contain a JSON array")
        return data

    def _write_raw(self, data: list[dict]) -> None:
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)