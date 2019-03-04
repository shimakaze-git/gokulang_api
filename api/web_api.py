import json
import falcon
from falcon import uri

from gokulang.gokulang import GokuLang


def validate(req, resp, resource, params):
    try:
        data = json.loads(req.stream.read().decode('utf-8'))
        if 'text' in data:
            req.params['text'] = data['text']
        else:
            raise ValueError
    except ValueError:
        raise falcon.HTTPBadRequest(
            'Invalid request params'
        )


class GokuLangResource:

    @falcon.before(validate)
    def on_post(self, req, resp):

        text = req.params['text']

        goku = GokuLang()
        goku_text = goku.translate(text)
        msg = {
            "normal_text": text,
            "goku_text": goku_text
        }
        resp.body = json.dumps(msg)

app = falcon.API()
app.add_route("/", GokuLangResource())


if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()
