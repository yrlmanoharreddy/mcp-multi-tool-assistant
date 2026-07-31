import requests

def get_student(student_id: int)->dict:
    url = f"http://127.0.0.1:8000/student/{student_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

print(get_student(101))
