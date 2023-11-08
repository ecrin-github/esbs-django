from djangorestframework_camel_case.render import CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer


TYPES = [str, int, bool, float, None]


class CustomRenderer(CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        if type(data) not in TYPES:
            data.update({'statusCode': status_code})

        return super(CustomRenderer, self).render(data, accepted_media_type, renderer_context)