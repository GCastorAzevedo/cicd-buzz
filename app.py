"""CI/CD Buzz Generator App"""

import os
import signal
from flask import Flask
from buzz import generator

APP = Flask(__name__)

#pylint: disable=protected-access
signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@APP.route("/")
def generate_buzz():
    """
    wrapper for generate_buzz to display the phrases!
    """
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
