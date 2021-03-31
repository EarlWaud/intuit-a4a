# Intuit A4A Craft Demo files

## getresources.py
This file contains the brief source code for the python "app".  

The app, through get methods expose the system utilization metrics from a server.

Examples:
```
curl -k http://blackwolk.com/disk
[{"free": 20.09, "total": 24.06, "used": 2.74}]%

curl -k http://blackwolk.com/memory
[{"active": 326254592, "available": 455225344, "buffers": 47992832, "cached": 472260608, "free": 118136832, "inactive": 248201216, "percent": 47.0, "shared": 33239040, "slab": 125714432, "total": 858411008, "used": 220020736}]%

curl -k http://blackwolk.com/cpu-stats
[{"ctx_switches": 58668751, "interrupts": 32587530, "soft_interrupts": 28369329, "syscalls": 0}]%
```

The exmaple was created on an Ubuntu server setup with the following:
```
#!/bin/bash
sudo apt update
sudo apt install -y python3 python3-pip git
sudo pip3 install psutil flask waitress
cd /opt
git clone https://github.com/EarlWaud/intuit-a4a.git
cd intuit-a4a
sudo /usr/bin/python3 ./getresources.py &
```


## dockerfile
The repo includes a dockerfile that can be used to create an docker image of the app.


## metrics-api.yml
The repo also includes a swagger configuration file exported from the AWS REST API Gateway setup
