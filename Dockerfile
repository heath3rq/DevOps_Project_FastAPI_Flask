FROM python:3.10-bullseye

WORKDIR /MS

COPY ./requirements.txt /MS
COPY ./main.py /MS
COPY ./test.py /MS

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT python main.py