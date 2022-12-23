from typing import Union

from pydantic import BaseModel


class SprocketDto(BaseModel):
    id: Union[str, None]
    teeth: int
    pitch_diameter: int
    outside_diameter: int
    pitch: int
