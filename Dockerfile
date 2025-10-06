from python:3.12-slim
workdir /usr/local/testtodo
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]