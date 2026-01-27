from flask_restful import Resource


class HomeResources(Resource):
    def get(self):
        return '{"versao":"2.0.0"}', 200
