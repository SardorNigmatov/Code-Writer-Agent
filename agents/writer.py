import os
from typing import Dict
from pydantic import BaseModel, Field
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# ---------------------------
# Muhit o‘zgaruvchilarini yuklash
# ---------------------------
load_dotenv()

# ---------------------------
# Pydantic chiqish modeli
# ---------------------------
class WriterOutput(BaseModel):
    """
    Model agentdan qaytadigan natijani tuzilgan ko'rinishda saqlash uchun.
    """
    code: str = Field(description="Yaratilgan Python kodi.")
    explanation: str = Field(description="Kod nima qilishi haqida tushuntirish.")

# ---------------------------
# LLM (GPT-4o-mini)
# ---------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

# ---------------------------
# Prompt (ko‘rsatma shabloni)
# ---------------------------
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "Siz Python dasturlash bo'yicha yordamchi agent siz. Toza va to'g'ri kod yozing."),
    ("human", "Quyidagi topshiriq uchun Python kodi yozing:\n{task}\n"
              "Shuningdek, kod nima qilishi haqida tushuntiring."),
])

# ---------------------------
# Chain (prompt + model + strukturalangan chiqish)
# ---------------------------
writer_chain = writer_prompt | llm.with_structured_output(WriterOutput)

# ---------------------------
# Writer tuguni (LangGraph node sifatida ishlatish uchun)
# ---------------------------
def writer_node(state: Dict) -> Dict:
    """
    Kiruvchi state ichidan 'task' matnini olib,
    kod va tushuntirishni qaytaradi.
    
    Parametrlar:
        state (Dict): {'task': "..."} ko'rinishida bo'lishi kerak.

    Qaytadi:
        Dict: {'code': ..., 'explanation': ...}
    """
    result: WriterOutput = writer_chain.invoke({"task": state["task"]})
    return {"code": result.code, "explanation": result.explanation}
