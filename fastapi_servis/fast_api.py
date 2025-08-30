from fastapi import FastAPI
from pydantic import BaseModel
from graph_builder import graph_builder

# ---------------------------
# FastAPI app
# ---------------------------
app = FastAPI()

# Graphni yaratamiz
graph = graph_builder()

# ---------------------------
# Request body modeli
# ---------------------------
class RequestBody(BaseModel):
    task: str  # Foydalanuvchi bergan Python topshirig‘i

# ---------------------------
# Endpoint: kod generatsiya qilish va testdan o‘tkazish
# ---------------------------
@app.post("/generate_code")
async def generate_code(request_body: RequestBody):
    """
    Foydalanuvchidan vazifa qabul qiladi,
    Writer kod yozadi,
    Tester esa kodni PASS/FAIL qilib tekshiradi.
    """
    # Boshlang‘ich state
    state = {
        "task": request_body.task,
        "code": "",
        "explanation": "",
        "result": "",
        "details": "",
        "retries": 0
    }

    # Graph’ni async rejimda chaqiramiz
    result = await graph.ainvoke(state)

    return {
        "task": result.get("task", ""),
        "code": result.get("code", ""),
        "explanation": result.get("explanation", ""),
        "result": result.get("result", ""),
        "details": result.get("details", ""),
        "retries": result.get("retries", 0),
    }
