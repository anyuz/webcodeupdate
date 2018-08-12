FROM python:3.6.2

RUN mkdir -p /home/project/dash_app
WORKDIR /home/project/dash_app
COPY requirements.txt /home/project/dash_app
RUN pip install  -r requirements.txt
RUN pip install --no-deps pandas==0.23.0
COPY . /home/project/dash_app

CMD [ "python", "/home/project/dash_app/webdash.py" ]
