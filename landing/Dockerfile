FROM python:3.8-alpine
WORKDIR /app
COPY ./app/requirements.txt /app/requirements.txt
RUN cd /app
RUN apk add --update && pip install --upgrade pip  && pip install -r requirements.txt  && rm -rf /var/cache/apk/*
COPY ./app /app
ENTRYPOINT ["python"]
CMD [ "app.py" ]