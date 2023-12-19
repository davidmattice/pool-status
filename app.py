import asyncio
import string
import json
import argparse
import sys
import pprint
import time
import os
from flask import Flask, render_template, request, url_for, flash, redirect
from screenlogicpy.gateway import ScreenLogicGateway

gateway = None

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def index():
  global gateway
  ip = "192.168.1.156"
  hosts = [{"ip": ip, "port": "80"}]
  success = None
  msg = "Not connected!"

  success = await gateway.async_connect(**hosts[0])
  if success:
    msg = "Connected!"
    success = await gateway.async_update()  
    msg = gateway.get_data("controller", "sensor", "air_temperature", "value")
    success = await gateway.async_disconnect()

  return render_template('index.html', msg=msg)


if __name__ == "app":
  gateway = ScreenLogicGateway()
  