from pydantic.alias_generators import to_camel
from typing import Annotated
from pydantic import Field, BaseModel, StringConstraints, ConfigDict

# *************** Type Aliases
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

type CharacterMight = Annotated[
    int,
    Field(description="A character's physical power", ge=0, le=100),
]

type CharacterAgility = Annotated[
    int,
    Field(description="A character's physical power", ge=0, le=100),
]

type CharacterVitality = Annotated[
    int,
    Field(description="A character's physical power", ge=0, le=100),
]

type CharacterInsight = Annotated[
    int,
    Field(description="A character's physical power", ge=0, le=100),
]

type CharacterArcana = Annotated[
    int,
    Field(description="A character's physical power", ge=0, le=100),
]

type CharacterPresence = Annotated[
    int,
    Field(description="A character's physical power", ge=0, le=100),
]

# *************** Data Models


class CharacterAttributes(BaseModel):
    """Attributes for a character"""

    might: CharacterMight
    agility: CharacterAgility
    vitality: CharacterVitality
    insight: CharacterInsight
    arcana: CharacterArcana
    presence: CharacterPresence


class Character(BaseModel):
    """A character in the game"""

    id: CharacterID
    name: CharacterName
    health: CharacterHealth
    attributes: CharacterAttributes


# *************** DTOs
class DTO(BaseModel):
    """Base class for Data Transfer Objects"""

    model_config = ConfigDict(
        alias_generator=to_camel,
        extra="forbid",
        validate_assignment=True,
        populate_by_name=True,
        from_attributes=True,
    )


class CharacterBaseDTO(DTO):
    """Data Transfer Object for character base information"""

    name: CharacterName
    attributes: CharacterAttributesDTO


class CharacterAttributesDTO(DTO):
    """Data Transfer Object for character's attributes"""

    might: CharacterMight
    agility: CharacterAgility
    vitality: CharacterVitality
    insight: CharacterInsight
    arcana: CharacterArcana
    presence: CharacterPresence


class CreateCharacterRequestDTO(CharacterBaseDTO):
    """Data Transfer Object for creating a new character"""

    pass


class CreateCharacterResponseDTO(CharacterBaseDTO):
    """Data Transfer Object for returning character data"""

    id: CharacterID


class UpdateCharacterAttributesRequestDTO(CharacterAttributesDTO):
    """Data Transfer Object for updating a character's attribute"""

    pass


class UpdateCharacterResponseDTO(CreateCharacterResponseDTO):
    """Data Transfer Object for returning updated character data"""

    pass
