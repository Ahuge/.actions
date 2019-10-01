FROM alpine:3.10

COPY main.py /main.py
COPY requirements.txt /requirements.txt

RUN apt-get install -qy python3
RUN apt-get install -qy python3-pip
RUN pip3 install -r /requirements.txt

ENTRYPOINT ["python3",  "/main.py",  "head=$1", "base=$2"]
