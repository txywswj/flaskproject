
from enum import Enum,unique

# Enum 类 可以用a.b.value 获得右边的值
#           a.b.name 获得左边的值
@unique   #各个字段的value 不能重复
class Code(Enum):
    succ = 0


    required_parameter_missing = 100

    unknow_error = 999

    cinema_does_not_exist = 200

    hall_does_not_exist = 201

    hall_seats_does_not_exist = 202

    """排期不存在"""
    play_does_not_exist = 300
    """购买价格小于排期设置的最小价格"""
    prcice_less_than_the_lowest_price = 301
    """座位不存在"""
    seat_does_not_exist = 400
    """座位已锁定"""
    seat_locked_already = 401
    """座位未锁定"""
    seat_not_locked = 402
    """座位已售出"""
    seat_sold_already = 403
    """锁座失败"""
    seat_lock_failed = 404
    """解锁座位失败"""
    seat_unlock_failed = 405
    """购买座位失败"""
    seat_buy_failed = 406

    """订单不存在"""
    order_does_not_exist = 500
    """订单状态异常"""
    order_status_error = 501
    """订单尚未支付"""
    order_not_paid_yet = 502
    """票不存在"""
    ticket_does_not_exist = 503
    """已取票"""
    ticket_printed_already = 504
    """取票验证码异常"""
    ticket_flag_error = 505
    """打票失败"""
    ticket_print_failed = 506
    """退票失败"""
    ticket_refund_failed = 507