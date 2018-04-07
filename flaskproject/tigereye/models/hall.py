'''
    影厅 (hall)
    id  (hid)
    影院id  (cid)
    名称  (name)
    屏幕类型  (screen_type)
    音效  (auto_type)
    座位数量  (seats_num)
    状态  (status)
'''
from tigereye.models import db, Model
class Hall(db.Model,Model):
    hid = db.Column(db.Integer,primary_key=True)
    cid = db.Column(db.Integer)
    name = db.Column(db.String(64),nullable=False)
    screen_type = db.Column(db.String(32))
    audio_type = db.Column(db.String(32))
    seats_num = db.Column(db.Integer,default = 0,nullable = False)
    status = db.Column(db.Integer,nullable=False,index=True)