FROM python:3.10-bullseye

WORKDIR /MS

COPY ./requirements.txt /MS
COPY ./menu_fastapi_app.py /MS
COPY ./menu_flask_app.py /MS

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT python menu_fastapi_app.py