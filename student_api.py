from fastapi import FastAPI, HTTPException


app = FastAPI()
students = {
    101: {
        "name" : "Manohar",
        "course": "Deep Learning",
        "marks" : 98
    },
    102: {
            "name" : "Abhilash",
            "course": "Machine Learning",
            "marks" : 92
        },
    103: {
            "name" : "Arun",
            "course": "Java Programming Language",
            "marks" : 89
        },
}


@app.get("/")
def home():
    return {"message": "Welcome to the student home page"}

@app.get("/student/{student_id}")
def get_student(student_id: int):
    student = students.get(student_id)
    if student is None:
        raise HTTPException(
            status_code=404,
            detail = "Student Not found"
        )
    return student