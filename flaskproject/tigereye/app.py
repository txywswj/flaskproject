from logging.handlers import SMTPHandler

from flask import Flask
import logging

from flask_classy import FlaskView

from tigereye.models import db, JSONEncoder
from logging import FileHandler, Formatter
import os

# def create_app(debug=True):
def create_app(config = None):
    app = Flask(__name__)
    # app.debug = debug
    app.config.from_object('tigereye.configs.default.DefalutConfig')
    app.config.from_object(config)
    app.json_encoder = JSONEncoder


    if not app.debug:
        app.logger.setLevel(logging.INFO)

        mail_handler = SMTPHandler(
            app.config['EMAIL_HOST'],
            app.config['SERVER_EMAIL'],
            # app.config['EMAIL_PORT'],
            app.config['ADMINS'],
            'TIGEREYE ALERT',
            credentials = (
                app.config['EMAIL_HOST_USER'],
                app.config['EMAIL_HOST_PASSWORD']
            )
        )
        mail_handler.setLevel(logging.ERROR)
        mail_handler.setFormatter(Formatter('''
        Message Type: %(levelname)s
        Location:     %(pathname)s: %(lineno)d
        Module:       %(module)s
        Function:     %(funcName)s
        Time:         %(asctime)s
        
        Message:
        
        
        %(message)s
        '''))
        app.logger.addHandler(mail_handler)


        file_handler = FileHandler(os.path.join(app.config['LOG_DIR'],'app.log'))
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(Formatter(
            '%(asctime)s %(levelname)s : %(message)s'
        ))
        app.logger.addHandler(file_handler)

    db.init_app(app)


    configure_views(app)
    app.logger.info('create_app_text')
    return app



def configure_views(app):
    from tigereye.api.movie import MovieView
    from tigereye.api.cinema import CinemaView
    from tigereye.api.misc import MiscView
    from tigereye.api.hall import HallView
    from tigereye.api.play import PlayView
    from tigereye.api.seat import SeatView
    from tigereye.api.order import OrderView


    for view in locals().values():
        print(type(view))
        print(type)
        print(type(app))

        if type(view) == type and issubclass(view, FlaskView):
            view.register(app)
    # MiscView.register(app)
    # CinemaView.register(app)
    # MovieView.register(app)

#
# @app.route('/check/')
# def hello_world():
#     return 'Hello World!'


# if __name__ == '__main__':
#     app.run()
