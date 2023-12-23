# Simple Pentair Screenlogic Pool Status

Flask Web Application to show staus of Pentair Screenlogic System

With special thanks to the developers of [screenlogic.py](https://github.com/dieselrabbit/screenlogicpy/tree/master)


Building and Running
- docker build --tag pool-status .
- docker stop pool-status;docker rm pool-status;docker run -d -p 5005:5000 --name pool-status pool-status
