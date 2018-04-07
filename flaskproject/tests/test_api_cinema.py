from flask import json

from tigereye.helper.code import Code
from .helper import FlaskTestCase

class TestApiCinema(FlaskTestCase):


    def test_cinema_all(self):
        # response = self.app.get('/cinema/all/')
        # self.assertEquals(response.status_code,200)
        # self.assertEquals()
        # data = json.loads(response.data)
        # self.assertEquals(data['rc'],Code.succ.value)
        self.get_succ_json('/cinema/all/')

    def test_cinema_halls(self):
        self.assert_get('/cinema/all', 400)
        data = self.get_succ_json('/cinema/all', cid = 1)
        self.assertIsNone(data['data'])


