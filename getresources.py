# import os
import psutil
import json
from flask import Flask
from flask import jsonify
from collections import namedtuple
from psutil._common import bytes2human

app = Flask(__name__)


def json_ntuple(x):
  nt = x._asdict()
  return("["+json.dumps(dict(nt), sort_keys=True)+"]")


@app.route('/')
def hello_world():
  return 'Hello, World!'


@app.route('/cpu-stats')
def get_cpu():
  cpu = psutil.cpu_stats()
  return(json_ntuple(cpu))


@app.route('/memory')
def get_memory():
  mem = psutil.virtual_memory()
  return(json_ntuple(mem))


def convert_disk_value_to_gb(ov):
  # convert to GB
  nv = float(ov) / 1024 / 1024 / 1024
  return( "{:.2f}".format(round(nv, 2)) )


@app.route('/disk')
def get_disk():
  disk = psutil.disk_usage('/')
  nt = disk._asdict()

  # remove the percent item
  del(nt['percent'])

  # convert scale on remaining items
  for item in nt.items():
    nt[item[0]] = convert_disk_value_to_gb(item[1])

  return("["+json.dumps(dict(nt), sort_keys=True)+"]")


if __name__ == '__main__':
  from waitress import serve
  serve(app, host="0.0.0.0", port=8080)
