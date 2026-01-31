# dto.py
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from domain import (
    CharacterMight,
    CharacterAgility,
    CharacterVitality,
    CharacterInsight,
    CharacterArcana,
    CharacterPresence,
    CharacterName,
    CharacterID,
)


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

class CharacterAttributesDTO(DTO):
    """Data Transfer Object for character's attributes"""

    might: CharacterMight
    agility: CharacterAgility
    vitality: CharacterVitality
    insight: CharacterInsight
    arcana: CharacterArcana
    presence: CharacterPresence

class CharacterBaseDTO(DTO):
    """Data Transfer Object for character base information"""

    name: CharacterName
    attributes: CharacterAttributesDTO


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
