from flask import Flask
from flask import request
import socket
import os
import sys
import requests
import time


app = Flask(__name__)


@app.route('/service')
def service():
	app.logger.info(request.json)
	app.logger.info(request.headers)
	return "{\"code\": 50001, \"msg\": \"error\", \"data\":\"test\"}",200,{'Status-Code': 500001, 'content-type': 'application/json'}

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=int(os.environ['PORT']), debug=True)
