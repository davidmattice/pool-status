import asyncio
import os
from flask import Flask, render_template

from screenlogicpy import ScreenLogicGateway, discovery
from screenlogicpy.discovery import async_discover
from screenlogicpy.const.common import (ScreenLogicException)

gateway = None

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def index():
  global gateway
  ip = None
  hosts = None
  msg = "No IP set"

  ip = os.getenv("IP_ADDR")
  if ip != None:

    hosts = [{"ip": ip, "port": "80"}]
#    hosts = await async_discover()       # Can't get this to work
    msg = hosts

    if len(hosts) > 0:
      try:
        await gateway.async_connect(**hosts[0])
        await gateway.async_update()  
        await gateway.async_disconnect()
        msg = gateway.get_data()

      except ScreenLogicException as err:
        msg = err

  return render_template('index.html', msg=msg)


  

if __name__ == "app":
  gateway = ScreenLogicGateway()
  