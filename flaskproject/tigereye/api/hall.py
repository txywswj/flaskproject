from flask import jsonify, request
from flask_classy import FlaskView

from tigereye.models.cinerma import Cinema
from tigereye.models.hall import Hall
from tigereye.models.seat import Seat
from tigereye.helper.code import Code

from tigereye.api import ApiView
from tigereye.helper.code import Code

class HallView(ApiView):

    def seats(self):
        hid = request.args.get('hid')
        hall = Hall.get(hid)
        if not hall:
            return Code.hall_seats_does_not_exist,request.args

        hall.seats = Seat.query.filter_by(hid = hid).all()
        return hall

