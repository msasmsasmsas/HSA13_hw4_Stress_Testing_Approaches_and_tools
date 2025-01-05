import subprocess

# Запуск FastAPI сервера
fastapi_command = ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Запуск Streamlit приложения
streamlit_command = ["streamlit", "run", "app.py"]

# Запускаем оба процесса
fastapi_process = subprocess.Popen(fastapi_command)
streamlit_process = subprocess.Popen(streamlit_command)

try:
    # Ожидание завершения процессов
    fastapi_process.wait()
    streamlit_process.wait()
except KeyboardInterrupt:
    # При остановке завершаем оба процесса
    fastapi_process.terminate()
    streamlit_process.terminate()
