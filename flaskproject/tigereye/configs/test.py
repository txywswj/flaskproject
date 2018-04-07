from tigereye.configs.default import DefalutConfig

class Testconfig(DefalutConfig):
    TESTTING = True
    JSON_SORT_KEYS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'