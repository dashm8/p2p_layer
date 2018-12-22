import json

class Encoder(object):
    """
    encodes and decodes string
    """

    @staticmethod
    def json_encode(str_msg):
        """
        encode into json object from string
        """
        return json.loads(str_msg)

    @staticmethod
    def json_decode(object_msg):
        """
        decode into string from json object
        """
        return json.dumps(object_msg)

