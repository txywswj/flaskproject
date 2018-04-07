from flask import json

from tigereye.helper.code import Code
from .helper import FlaskTestCase

pid = 1
sid_list = [1,2]
sid = ','join([str(i) for i in sid_list])
price = 5000
orderno = 'test-%s-%s'  %(pid,sid)


class TestApiSeat(FlaskTestCase):
    def test_seat_num = len(sid_list)
    rv = self.get_succ_json('/seat/lock/',method='POST',
                            orderno = orderno,
                            pid = pid,
                            sid = sid,
                            price = price)
    self.assertEquals(rv['data']['locked_seats_num'], locked_seats_num)

    rv = self.get_succ_json('/play/seats',pid = pid)

    for seat in rv['data']:
        if seat['orderno'] == orderno:
            self.assertEquals(seat['status'],SeatStatus.locked.value)
            succ_count += 1
    self.assertEquals(succ_count, locked_seats_num)


    rv = self.get_json(
        '/seat/lock/',
        method='POST',
        orderno = orderno,
        pid = pid,
        sid = sid,
        price = price
    )
    self.assertEquals(rv['rc'],Code.seat_lock_failed.value)



    #测试驱动开发