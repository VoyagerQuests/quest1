import json
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path

app = FastAPI(title="Quest 1 - Naive Character API")

ATTRIBUTE_NAMES = ["Might", "Agility", "Vitality", "Insight", "Arcana", "Presence"]
DATA_PATH = Path("characters.json")


def load_characters() -> List[Dict[str, Any]]:
    if not DATA_PATH.exists():
        return []
    raw = DATA_PATH.read_text(encoding="utf-8")
    if not raw:
        return []
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Failed to decode character data")
    if not isinstance(data, list):
        raise HTTPException(status_code=500, detail="Character data is not a list")
    return data


def save_characters(characters: List[Dict[str, Any]]) -> None:
    DATA_PATH.write_text(json.dumps(characters, indent=4), encoding="utf-8")


# Request Models


class AttributeUpdate(BaseModel):
    value: int


# ------------ API Endpoints


@app.put("/characters/{id}/attributes/{attribute_name}")
def update_character_attribute(id: int, attribute_name: str, body: AttributeUpdate):
    if attribute_name not in ATTRIBUTE_NAMES:
        raise HTTPException(status_code=400, detail="Invalid attribute name")
    chars = load_characters()
    for i, c in enumerate(chars):
        if c.get("id") == id:
            c["attributes"][attribute_name] = body.value
            chars[i] = c
            save_characters(chars)
            return c
    raise HTTPException(status_code=404, detail="Character not found")


@app.get("/characters")
def list_characters(name: Optional[str] = None):
    chars = load_characters()
    if name:
        search_term = name.casefold()
        chars = [
            c for c in chars if str(c.get("name", "")).casefold().find(search_term) >= 0
        ]
    return chars


@app.get("/characters/{id}")
def get_character(id: int):
    chars = load_characters()
    for c in chars:
        if c.get("id") == id:
            return c

    raise HTTPException(status_code=404, detail="Character not found")


@app.delete("/characters/{id}", status_code=204)
def delete_character(id: int) -> None:
    chars = load_characters()
    new_chars = [c for c in chars if c.get("id") != id]
    if len(new_chars) == len(chars):
        raise HTTPException(status_code=404, detail="Character not found")
    save_characters(new_chars)
    return None
