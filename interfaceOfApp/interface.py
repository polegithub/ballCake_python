#-*- coding: UTF-8 -*-

__author__ = 'chengpoleness'

from  flask import flask

app = Flask(__name__)

@app.route('/movieInfo/', methods=['GET'])
def getMovieDetailInfo():
    movieId = request.form.get('movieId')

