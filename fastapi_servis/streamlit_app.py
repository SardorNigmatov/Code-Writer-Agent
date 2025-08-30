import streamlit as st
import requests

# FastAPI server manzili
API_URL = "http://localhost:8080/generate_code"

st.title("🤖 Python Code Writer & Tester")

# Foydalanuvchi topshirig‘i
task = st.text_input("Python uchun vazifani kiriting:")

if st.button("Kod yaratish va test qilish"):
    if not task.strip():
        st.warning("❗ Iltimos, avval vazifani kiriting.")
    else:
        with st.spinner("Kod yaratilmoqda va test qilinmoqda..."):
            response = requests.post(API_URL, json={"task": task})
            data = response.json()

        # Natijalar
        st.subheader("✍️ Yaratilgan kod:")
        st.code(data.get("code", ""), language="python")

        st.subheader("📖 Tushuntirish:")
        st.write(data.get("explanation", ""))

        st.subheader("✅ Test natijasi:")
        result = data.get("result", "ERROR")
        if result == "PASS":
            st.success("Kod testdan muvaffaqiyatli o‘tdi ✅")
        elif result == "FAIL":
            st.error("Kod testdan o‘tmadi ❌")
        else:
            st.warning("Test natijasi noaniq ⚠️")

        st.subheader("🔍 Batafsil ma'lumot:")
        st.write(data.get("details", ""))

        st.caption(f"Qayta urinishlar soni: {data.get('retries', 0)}")
