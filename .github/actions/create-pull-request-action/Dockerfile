FROM centos:7

COPY entrypoint.sh /entrypoint.sh
COPY main.py /main.py
COPY requirements.txt /requirements.txt

RUN yum install -qy python3
RUN yum install -qy python3-pip
RUN pip3 install -r /requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
