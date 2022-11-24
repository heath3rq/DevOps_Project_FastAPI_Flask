FROM python:3.10-bullseye
RUN mkdir -p /app
COPY ./menu_fastapi_app.py /app
COPY ./menu_flask_app.py /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "menu_fastapi_app.py" ]
ENTRYPOINT [ "python" ]