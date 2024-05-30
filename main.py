from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/AddStudents/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@app.get("/GetStudents/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.get("/GetAllStudents/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_all_students(db, skip=skip, limit=limit)
    return students

@app.patch("/UpdateStudents/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentUpdate, db: Session = Depends(get_db)):
    db_student = crud.update_student(db, student_id=student_id, student=student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.delete("/DeleteStudents/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    crud.delete_student(db, student_id=student_id)
    return {"message": "Student deleted successfully"}

@app.post("/PostScore/", response_model=schemas.Score)
def create_score(score: schemas.ScoreBase, db: Session = Depends(get_db)):
    return crud.create_score(db=db, score=score)

@app.get("/GetScore/{score_id}", response_model=schemas.Score)
def read_score(score_id: int, db: Session = Depends(get_db)):
    db_score = crud.get_score(db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score

@app.patch("/UpdateScore/{score_id}", response_model=schemas.Score)
def update_score(score_id: int, score: schemas.ScoreUpdate, db: Session = Depends(get_db)):
    db_score = crud.update_score(db, score_id=score_id, score=score)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score

@app.delete("/DeleteScore/{score_id}")
def delete_score(score_id: int, db: Session = Depends(get_db)):
    crud.delete_score(db, score_id=score_id)
    return {"message": "Score deleted successfully"}

@app.get("/GetTables/")
def get_tables(db: Session = Depends(get_db)):
    tables = db.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    table_info = {}
    for table in tables:
        table_name = table[0]
        columns = db.execute(f"PRAGMA table_info({table_name});").fetchall()
        column_info = [{"name": col[1], "type": col[2]} for col in columns]
        rows = db.execute(f"SELECT * FROM {table_name};").fetchall()
        table_info[table_name] = {"columns": column_info, "rows": rows}
    return table_info
