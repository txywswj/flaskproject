from flask import jsonify, request
from flask_classy import FlaskView

from tigereye.models.cinerma import Cinema
from tigereye.models.hall import Hall
from tigereye.api import ApiView
from tigereye.helper.code import Code
from tigereye.extensions.validator import Validator
from tigereye.models.movie import Movie
from tigereye.models.play import Play


class CinemaView(ApiView):

    def all(self):
        cinemas = Cinema.query.all()

        return cinemas

    @Validator(cid=int)
    def get(self):
        cid = request.args['cid']
        cinema = Cinema.query.get_or_404(cid)
        if not cinema:

            return Code.cinema_does_not_exist,request.args
        return cinema

    @Validator(cid=int)
    def halls(self):
        cid = request.params['cid']
        cinema = Cinema.get(cid)
        if not cinema:
            return Code.cinema_does_not_exist,request.args
        cinema.halls = Hall.query.filter_by(cid = cid).all()
        return cinema


    @Validator(cid=int)
    def plays(self):
        cid = request.params['cid']
        cinema = Cinema.get(cid)
        if not cinema:
            return Code.cinema_does_not_exist, request.args

        cinema.plays = Play.query.filter_by(cid=cid).all()
        for  play in cinema.plays:
            play.movie = Movie.get(play.mid)
        return cinema.plays





