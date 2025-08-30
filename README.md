# 🤖 CodeWriterBot

Python kod yozib beruvchi va test qiluvchi AI agent.  
U **LangChain + LangGraph + FastAPI + Streamlit** yordamida qurilgan.  

---

## 📌 Loyihaning asosiy qismlari

### 🔹 `agents/`
- `writer.py` → foydalanuvchi bergan vazifa asosida **kod yozadi** va tushuntirish beradi.  
- `tester.py` → yozilgan kodni **test qiladi (PASS/FAIL)**.  

### 🔹 `fastapi_servis/`
- `graph_builder.py` → Writer va Tester tugunlarini ulanadigan **LangGraph pipeline**.  
- `fast_api.py` → **FastAPI server**, endpoint: `/generate_code`.  
- `streamlit_app.py` → **Streamlit UI**, foydalanuvchi interfeysi.  

### 🔹 `main.py`
- Konsol rejimida ishlash uchun oddiy kirish nuqtasi.  

---

## 📂 Fayl tuzilishi
- CodeWriterBot/
- ├── agents/
- │ ├── writer.py
- │ ├── tester.py
- ├── fastapi_servis/
- │ ├── graph_builder.py
- │ ├── fast_api.py
- │ ├── streamlit_app.py
- ├── main.py
- ├── requirements.txt
- └── README.md

## FastAPI backendni ishga tushirish
uvicorn fastapi_servis.fast_api:app --reload --port 8000
## Streamlit frontendni ishga tushirish
streamlit run fastapi_servis/streamlit_app.py


## 🔹 Streamlit interfeysi
<img width="1165" height="841" alt="image" src="https://github.com/user-attachments/assets/df7bd354-c4e1-4424-b4be-312c06ec9311" />

## 🔹 Yakuniy natija (PASS/FAIL)
<img width="1017" height="803" alt="image" src="https://github.com/user-attachments/assets/5ffbc810-19c9-4aa7-8b3f-63df8f38b411" />
 
