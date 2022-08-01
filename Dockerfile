FROM python:3.9.1

WORKDIR /content

COPY src/ .

RUN pip install -r requirements.txt

COPY model.pt .

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
