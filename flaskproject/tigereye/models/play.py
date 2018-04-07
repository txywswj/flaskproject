from tigereye.models import db,Model
from sqlalchemy import text
from sqlalchemy.sql import func
'''
排期
    id  (pid)
    电影id  (mid)
    影院id  (cid)
    影厅id  (hid)
    价格类型  (price_type)
    原价  (price)
    售价  (market_price)
    最低价  (lowest_price)
    开始时间  (start_time)
    时常  (duration)
    创建时间  (create_time)
    最后更新时间  (update_time)
    状态  （status）
'''

class Play(db.Model,Model):


    pid = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer)
    hid = db.Column(db.Integer)
    mid = db.Column(db.Integer)

    start_time = db.Column(db.DateTime,nullable=False)
    duration = db.Column(db.Integer,default=0,nullable=False)

    price_type = db.Column(db.Integer)
    price = db.Column(db.Integer)
    market_price = db.Column(db.Integer)
    lowest_price = db.Column(db.Integer)

    created_time = db.Column(db.DateTime,server_default=text('CURRENT_TIMESTAMP'))
    updated_time = db.Column(db.DateTime,onupdate=func.now())
    status = db.Column(db.Integer,default=0,nullable=False,index=True)
