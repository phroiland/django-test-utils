from . import base
import pickle as pickle
from test_utils.testmaker.serializers import REQUEST_UNIQUE_STRING, RESPONSE_UNIQUE_STRING

class Serializer(base.Serializer):

    def __init__(self, name='pickle'):
        super(Serializer, self).__init__(name)

    def save_request(self, request):
        """Saves the Request to the serialization stream"""
        request_dict = self.process_request(request)
        self.ser.info(pickle.dumps(request_dict))
        self.ser.info(REQUEST_UNIQUE_STRING)

    def save_response(self, request, response):
        """Saves the Response-like objects information that might be tested"""
        response_dict = self.process_response(request.path, response)
        try:
            self.ser.info(pickle.dumps(response_dict))
            self.ser.info(RESPONSE_UNIQUE_STRING)
        except (TypeError, pickle.PicklingError):
            #Can't pickle wsgi.error objects
            pass
