import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"  # URL вашего FastAPI приложения

st.title("Stress Test Practice")

# Форма для отправки данных
st.header("Добавить данные")
key = st.text_input("Введите ключ:")
value = st.text_input("Введите значение:")
if st.button("Отправить"):
    if key and value:
        response = requests.post(f"{BASE_URL}/data/", json={"key": key, "value": value})
        if response.status_code == 200:
            st.success("Данные успешно сохранены!")
        else:
            st.error(f"Ошибка: {response.json()}")

# Кнопка для отображения данных
st.header("Просмотр данных")
if st.button("Загрузить данные"):
    response = requests.get(f"{BASE_URL}/data/")
    if response.status_code == 200:
        data = response.json()
        if data:
            st.write(data)
        else:
            st.info("Данных нет.")
    else:
        st.error("Ошибка при загрузке данных.")
