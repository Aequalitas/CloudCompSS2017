# File: confServ.py 
# Author: Franz Weidmann
# Description: This file provides a small API
#   in form of a web server which enables a dynamic 
#   configuration of the HAProxy service at runtime
import subprocess as sp
from flask import Flask as f
from flask import request as req
app = f(__name__)

HAPATH = "/etc/haproxy/haproxy.cfg"

# debug route for status check
@app.route("/")
def hello():
    return "Hello %s" % req.remote_addr
# API for adding or deleting a web server from the HAProxy config file
# @param type 1 = add server, 2 = delete server
# @param serverNR a number to identify the web server
@app.route("/update/<int:type>/<int:serverNR>")
def updateHAProxy(type, serverNR):
    ip = req.remote_addr
    name = "webserver%d" % serverNR

    if(type == 1):
        # adding is done by simple calling the echo shell command
        cmd = 'printf "    server %s %s check" >> %s' % (name, ip, HAPATH)
    else:
        pattern = "server %s %s check" % (name, ip)
        # deleting is done by using the shell tool sed
        cmd = "sed -i '/%s/d' %s" % (pattern, HAPATH)

    sp.call(cmd, shell=True)
    # in order to change the configuration
    # the HAProxy service has to be reloaded
    sp.call("service haproxy reload", shell=True)
    return "OK"
