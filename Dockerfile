FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /curiosity
WORKDIR /curiosity

COPY . $WORKDIR
RUN pip install -r requirements.txt
#RUN python manage.py migrate --noinput

CMD python manage.py runserver 0.0.0.0:8000
