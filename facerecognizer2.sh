#!/bin/sh
SERVICE='facerecognizer2.py'
 
if ps ax | grep -v grep | grep $SERVICE > /dev/null
then
    echo "$SERVICE service running, everything is fine"
else
    echo "$SERVICE is not running and going to run now"
    cd /home/ubuntu/GitHub/face-recognition-python-opencv/
    python /home/ubuntu/GitHub/face-recognition-python-opencv/facerecognizer2.py /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/face/ /var/nodes/easyrtc/node_modules/easyrtc/server_example/uploads/ /var/nodes/easyrtc/node_modules/easyrtc/demos/latest/
fi
