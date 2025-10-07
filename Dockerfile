FROM python:3.12-slim
WORKDIR /usr/local/testtodo
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "app.py"]
