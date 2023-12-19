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

@app.route('/', methods=['GET', 'POST'])
async def index():
    return render_template('index.html')


if __name__ == "app":
  gateway = ScreenLogicGateway()
  