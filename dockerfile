FROM ubuntu:16.04

# RUN apt-get update && apt-get install -y --no-install-recommends \
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

RUN pip3 install psutil
RUN pip3 install flask waitress 

RUN git clone https://github.com/EarlWaud/intuit-a4a.git

EXPOSE 8080
ENV PYTHONPATH=/intuit-a4a
WORKDIR /intuit-a4a

CMD ["/usr/bin/python3", "/intuit-a4a/getresources.py"]
