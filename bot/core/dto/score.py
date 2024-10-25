from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class ScoreBase(BaseModel):
    score_id: UUID

class ScoreUser(BaseModel):
    user_id: int

class ScoreName(BaseModel):
    exam_name: str

class ScoreQuantity(BaseModel):
    quantity: int

class ScoreTimestamp(BaseModel):
    created_at: datetime
    updated_at: datetime

class Score(ScoreBase, ScoreUser, ScoreTimestamp, ScoreQuantity, ScoreName):
    pass

class CreateScore(ScoreName, ScoreQuantity, ScoreUser):
    pass
