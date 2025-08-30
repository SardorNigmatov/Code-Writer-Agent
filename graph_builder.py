from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from agents.writer import writer_node
from agents.tester import tester_node

# ---------------------------
# State: agent ishlash jarayonida saqlanadigan ma'lumotlar
# ---------------------------
class State(TypedDict):
    task: str           # Foydalanuvchi bergan topshiriq
    code: str           # Writer yozgan kod
    explanation: str    # Kod haqida tushuntirish
    result: str         # Tester bergan natija (PASS, FAIL, ERROR)
    details: str        # Tester batafsil javobi
    retries: int        # Qayta urinib ko‘rish soni

# ---------------------------
# Maksimal qayta urinish soni
# ---------------------------
MAX_RETRIES = 3

# ---------------------------
# Yo‘nalish qarori
# ---------------------------
def route_decision(state: State) -> str:
    """
    Tester natijasiga qarab keyingi qadamni belgilaydi.
    - Agar PASS bo‘lsa → tugatadi.
    - Agar maksimal urinishdan oshsa → tugatadi.
    - Aks holda qaytadan Writer bosqichiga qaytadi.
    """
    if state["result"] == "PASS":
        return END
    elif state["retries"] >= MAX_RETRIES:
        return END
    
    # Urinish sonini oshiramiz
    state["retries"] += 1
    return "writer"

# ---------------------------
# Graph quruvchi
# ---------------------------
def build_graph() -> StateGraph[State]:
    """
    Writer → Tester → Route oqim grafigini quradi.
    """
    graph_builder = StateGraph(State)

    # Tugunlar
    graph_builder.add_node("writer", writer_node)
    graph_builder.add_node("tester", tester_node)

    # Yo‘nalishlar
    graph_builder.add_edge(START, "writer")
    graph_builder.add_edge("writer", "tester")
    graph_builder.add_conditional_edges("tester", route_decision)

    return graph_builder.compile()
