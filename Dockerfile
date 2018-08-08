FROM python:3-alpine

RUN mkdir /webcode
WORKDIR /webcode
ADD . /webcode/
RUN pip install -r requirements.txt
RUN pip install --no-deps pandas==0.23.0

EXPOSE 5000
CMD [ "python", "/webcode/webdash.py" ]
