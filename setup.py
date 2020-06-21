

import time
from flask import Flask, render_template, redirect, url_for, request, session, make_response, flash
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error_pages/404.html'), 404


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("detailscopy.html")


if __name__ == '__main__':
    app.run(debug=True)