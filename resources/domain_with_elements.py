from flask_restful import Resource, reqparse
from model.domain import Domain
from helpers.text_extractor import TextExtractor


class DomainWithElements(Resource):
    """
    resource do przekazania do frontu
    """
    parser = reqparse.RequestParser()
    parser.add_argument('domain',
                        type=str,
                        required=True,
                        help="there must be domain name to rock this code")

    @staticmethod
    def post():
        data = DomainWithElements.parser.parse_args()

        domain = Domain.find_by_name(data['domain'])
        if domain:
            domain.update()
        else:
            domain = Domain(data['domain'])

        TextExtractor.extract(data['domain'], domain)
        Domain.save_domain(domain)

        return domain.json()
