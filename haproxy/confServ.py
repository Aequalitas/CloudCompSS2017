import subprocess as sp
from flask import Flask as f
from flask import request as req
app = f(__name__)

HAPATH = "/etc/haproxy/haproxy.cfg"

@app.route("/")
def hello():
    return "Hello %s" % req.remote_addr

@app.route("/update/<int:type>/<int:serverNR>")
def updateHAProxy(type, serverNR):
    ip = req.remote_addr
    name = "webserver%d" % serverNR

    if(type == 1):
        cmd = 'printf "    server %s %s check" >> %s' % (name, ip, HAPATH)
    else:
        pattern = "server %s %s check" % (name, ip)
        cmd = "sed -i '/%s/d' %s" % (pattern, HAPATH)

    sp.call(cmd, shell=True)
    sp.call("service haproxy reload", shell=True)
    return "OK"
