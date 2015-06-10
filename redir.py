#!/usr/bin/env python3
#
# url redirection service
#

from argparse import ArgumentParser
from flask import Flask, redirect, request, abort

app = Flask(__name__)

@app.route('/')
def index():
    url = request.args.get('url')
    if url:
        return redirect(url, code=301)
    else:
        abort(404)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', default=False)
    parser.add_argument('-b', '--bind', default='127.0.0.1')
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()
    app.run(debug=args.debug, host=args.bind, port=args.port)

