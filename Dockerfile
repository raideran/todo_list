FROM python:3.10.12-alpine3.18

COPY [".", "usr/src"]

WORKDIR /usr/src

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]