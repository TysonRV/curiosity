FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /curiosity
WORKDIR /curiosity

COPY . $WORKDIR
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
