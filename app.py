from flask import Flask,request
import re
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/ddns")
@app.route("/ddns/<name>")
def ddns(name = ""):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    match_object = re.match("[a-zA-Z]+", name)
    host=request.args.get('host')
    ip=request.args.get('ip')
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    s="ddns"
    if (host): s=s+",dns host is :" + host
    if (ip): s=s+",ip:" + ip
    s = s+ formatted_now + " " + clean_name
    return s