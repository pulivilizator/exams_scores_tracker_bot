from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class ScoreBase(BaseModel):
    score_id: UUID
    user_id: int

class ScoreName(BaseModel):
    name: str

class ScoreQuantity(BaseModel):
    quantity: int

class ScoreTimestamp(BaseModel):
    created_at: datetime
    updated_at: datetime

class Score(ScoreBase, ScoreTimestamp, ScoreQuantity, ScoreName):
    pass
