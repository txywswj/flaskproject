# 正常的配置，configs里面有三个配置
# 灰度环境，就是和线上的环境基本上一模一样，只是用户比较少。
#   通过灰度环境，来逐渐逐渐上线，小规模上线。

from tigereye.configs.default import DefalutConfig


class ProductionConfig(DefalutConfig):
    DEBUG = False
    JSON_SORT_KEYS = False
    JSON_PRETTY_REGULAR = False
    SQLALCHEMY_ECHO = False
    # 以上 达到 上线基本配置
    # import sys
    #  print(sys.path)
    EMAIL_HOST = 'smtp.exmail.qq.com'
    EMAIL_PORT = 465

    # EMAIL_HOST_USER = SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'test1@iguye.com'
    EMAIL_HOST_USER = 'test1@iguye.com'
    EMAIL_HOST_PASSWORD = 'P67844QUssW3'
    EMAIL_USE_SSL = True
    ADMINS = ['839173890@qq.com']


    # 持续集成


    #flake8
    #jenkins



    #ab