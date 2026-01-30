from dto import CreateCharacterRequestDTO, CreateCharacterResponseDTO, UpdateCharacterAttributesRequestDTO, UpdateCharacterResponseDTO
from domain import Character, CharacterAttributes
from nanoid import generate
from enum import StrEnum

ID_SIZE = 16

class IDPrefix(StrEnum):
    CHARACTER = "char"

def generate_id(prefix: IDPrefix) -> str:
    return f"{prefix}_{generate(size=ID_SIZE)}"


def create_character(
    req: CreateCharacterRequestDTO,
) -> CreateCharacterResponseDTO:
    character = Character(
        id=generate_id(IDPrefix.CHARACTER),
        name=req.name,
        attributes=CharacterAttributes.model_validate(req.attributes)
    )

    
    character = Character()
    return CreateCharacterResponseDTO(
        id=generate_id(IDPrefix.CHARACTER),
        name=req.name,
        attributes=CharacterAttributes(
            might=req.attributes.might,
            agility=req.attributes.agility,
            vitality=req.attributes.vitality,
            insight=req.attributes.insight,
            arcana=req.attributes.arcana,
            presence=req.attributes.presence,
        ),
    )