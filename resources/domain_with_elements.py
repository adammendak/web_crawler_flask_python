from flask_restful import Resource, reqparse
from model.domain import Domain


class DomainWithElements(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('domain',
                        type=str,
                        required=True,
                        help="there must be domain name to rock this code")

    def post(self):
        data = DomainWithElements.parser.parse_args()
        domain_to_save = Domain(data['domain'])
        return domain_to_save.json()
