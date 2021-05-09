from werkzeug import BaseRequest

class Request(BaseRequest):
    pass
    # поддержку заголовка accept

from werkzeug import BaseRequest, AcceptMixin

class Request(AcceptMixin, BaseRequest):
    pass
# создать объект запроса, поддерживающий заголовки accept, etags, 
# аутентификацию и поддержку агента пользователя:
from werkzeug import BaseRequest, AcceptMixin, ETagRequestMixin, UserAgentMixin, AuthenticationMixin

class Request(AcceptMixin, ETagRequestMixin, UserAgentMixin, AuthenticationMixin, BaseRequest):
    pass