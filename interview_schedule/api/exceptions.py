from rest_framework.serializers import ValidationError
from rest_framework import status



class QueryParameterException(ValidationError):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'error'

    def __init__(self, detail):
        self.detail = detail