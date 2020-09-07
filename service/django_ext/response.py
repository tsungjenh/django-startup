import json
from datetime import datetime
from django.http import HttpResponse


class EnhencedEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat(' ')
        return super(EnhencedEncoder, self).default(o)


class JsonResponse(HttpResponse):

    def __init__(self,
                 content,
                 content_type='application/json; charset=utf-8',
                 **kwargs):
        super(JsonResponse, self).__init__(
            content=json.dumps(
                content, cls=EnhencedEncoder, ensure_ascii=False),
            content_type=content_type,
            **kwargs
        )
