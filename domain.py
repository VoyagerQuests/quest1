# domain.py
from typing import Annotated
from pydantic import BaseModel, Field, StringConstraints

type CharacterID = Annotated[
    str,
    Field(description="A unique identifier for a character", pattern=r"^char_.{12}$"),
]

type CharacterName = Annotated[
    str,
    StringConstraints(min_length=10, max_length=100),
    Field(description="A character's name"),
]

type CharacterHealth = Annotated[
    int,
    Field(description="A character's current health", ge=0, le=100),
]

type CharacterMight = Annotated[int, Field(ge=0, le=100)]
type CharacterAgility = Annotated[int, Field(ge=0, le=100)]
type CharacterVitality = Annotated[int, Field(ge=0, le=100)]
type CharacterInsight = Annotated[int, Field(ge=0, le=100)]
type CharacterArcana = Annotated[int, Field(ge=0, le=100)]
type CharacterPresence = Annotated[int, Field(ge=0, le=100)]


class CharacterAttributes(BaseModel):
    might: CharacterMight
    agility: CharacterAgility
    vitality: CharacterVitality
    insight: CharacterInsight
    arcana: CharacterArcana
    presence: CharacterPresence


class Character(BaseModel):
    id: CharacterID
    name: CharacterName
    health: CharacterHealth
    attributes: CharacterAttributes
