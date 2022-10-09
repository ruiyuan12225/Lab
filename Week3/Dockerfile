FROM python

COPY requirements.txt /temp/
RUN pip3 install -r /temp/requirements.txt

VOLUME [ "/app" ]
WORKDIR /app

EXPOSE 8000

#docker run -it -p8000:8000 -v $(pwd)/app:/app
