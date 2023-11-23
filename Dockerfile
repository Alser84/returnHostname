FROM python:3.6.9-slim
COPY . /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV app_port=7000
ENV FLASK_APP=main.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]