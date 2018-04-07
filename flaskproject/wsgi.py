from tigereye import create_app
# 对外隐藏了实现
from tigereye.configs.production import ProductionConfig

application = create_app(config=ProductionConfig)
#


