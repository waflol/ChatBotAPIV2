FROM python:3.7-slim
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . /app/
# CMD python app.py
CMD exec gunicorn --bind 0.0.0.0:80 --workers 1 --threads 8 --timeout 0 app:app