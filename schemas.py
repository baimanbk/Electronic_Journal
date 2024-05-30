from pydantic import BaseModel
from typing import List

class ScoreBase(BaseModel):
    subject: str
    score: int
    student_id: int

class ScoreCreate(ScoreBase):
    pass

class ScoreUpdate(ScoreBase):
    pass

class Score(ScoreBase):
    id: int

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str
    age: int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    scores: List[Score] = []

    class Config:
        orm_mode = True
