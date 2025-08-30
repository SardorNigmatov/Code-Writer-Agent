from typing import Dict, Any
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent


# ---------------------------
# Tool: Python kodini bajaruvchi
# ---------------------------
@tool("execute_python")
def execute_python_code(code: str) -> str:
    """
    Python kodini bajaradi va natijani qaytaradi.
    
    Parametr:
        code (str): Python kodi matn ko‘rinishida
    
    Qaytadi:
        str: "Code executed successfully" yoki xatolik xabari
    """
    print("[Tool] Executing Python code...")
    try:
        exec_globals: Dict[str, Any] = {}
        exec(code, {}, exec_globals)
        return "Code executed successfully ✅"
    except Exception as e:
        return f"Error: {e}"


# ---------------------------
# LLM model
# ---------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

# ---------------------------
# ReAct Agent
# ---------------------------
agent = create_react_agent(llm, [execute_python_code])

# ---------------------------
# Tester Node
# ---------------------------
def tester_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Writer yozgan kodni test qiladi.
    
    Parametr:
        state (Dict): {'code': "..."} ko‘rinishida bo‘lishi kerak
    
    Qaytadi:
        Dict: {'result': 'PASS/FAIL/ERROR', 'details': agent_javobi}
    """
    # Foydalanuvchi xabari
    message = [{
        "role": "user",
        "content": f"Test this Python code and respond with PASS or FAIL:\n{state['code']}"
    }]

    # Agentni ishga tushirish
    response = agent.invoke({"messages": message})
    final_message = response["messages"][-1].content

    # Natijani aniqlash
    if "PASS" in final_message.upper():
        result = "PASS"
    elif "FAIL" in final_message.upper():
        result = "FAIL"
    else:
        result = "ERROR"

    return {"result": result, "details": final_message}
