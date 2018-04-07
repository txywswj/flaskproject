import functools

from flask import request, Response, make_response, jsonify
from flask_classy import FlaskView
from tigereye.helper.code import Code

class ApiView(FlaskView):
    @classmethod
    def make_proxy_method(cls, name):
        """Creates a proxy function that can be used by Flasks routing. The
        proxy instantiates the FlaskView subclass and calls the appropriate
        method.

        :param name: the name of the method to create a proxy for
        """

        i = cls()
        view = getattr(i, name)

        if cls.decorators:
            for decorator in cls.decorators:
                view = decorator(view)

        @functools.wraps(view)
        def proxy(**forgettable_view_args):
            # Always use the global request object's view_args, because they
            # can be modified by intervening function before an endpoint or
            # wrapper gets called. This matches Flask's behavior.
            del forgettable_view_args

            if hasattr(i, "before_request"):
                response = i.before_request(name, **request.view_args)
                if response is not None:
                    return response

            before_view_name = "before_" + name
            if hasattr(i, before_view_name):
                before_view = getattr(i, before_view_name)
                response = before_view(**request.view_args)
                if response is not None:
                    return response

            response = view(**request.view_args)


            #判断是否是一个Response对象
            if not isinstance(response,Response):
                # 如果不是，则先获取它的类型
                response_type = type(response)
                #如果是tuple类型
                if response_type == tuple and len(response)> 1:
                    rc,_data = response
                    return jsonify(rc = rc.value,msg = rc.name,data = _data)
                else:
                    return jsonify(rc=Code.succ.value,msg=Code.succ.name,data = response)

            # if not isinstance(response, Response):
            #     response = make_response(response)

            after_view_name = "after_" + name
            if hasattr(i, after_view_name):
                after_view = getattr(i, after_view_name)
                response = after_view(response)

            if hasattr(i, "after_request"):
                response = i.after_request(name, response)

            return response

        return proxy
