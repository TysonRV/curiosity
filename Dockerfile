FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /curiosity
WORKDIR /curiosity

COPY . $WORKDIR
RUN pip install -r requirements.txt
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT