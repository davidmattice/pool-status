import asyncio
import string
import json
import argparse
import sys
import pprint
import time
import os
from flask import Flask, render_template, request, url_for, flash, redirect
from screenlogicpy import ScreenLogicGateway, discovery

gateway = None

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def index():
  global gateway
  ip = None
  success = None

  msg = "No IP set"
  ip = os.getenv("IP_ADDR")
  if ip != None:

    hosts = [{"ip": ip, "port": "80"}]
#    hosts = await discovery.async_discover()
    msg = hosts

    success = await gateway.async_connect(**hosts[0])
    if success:
      msg = "Connected!"
      success = await gateway.async_update()  
      if success:
        msg = gateway.get_data()
        success = await gateway.async_disconnect()

  return render_template('index.html', msg=msg)


if __name__ == "app":
  gateway = ScreenLogicGateway()
  