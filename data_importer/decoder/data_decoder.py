import jwt


class DataDecoder:
    def decode(self, json_object):
        resource = json_object['resource']
        decoded_resource = jwt.decode(resource, options={"verify_signature": False})
        json_object['resource'] = decoded_resource
        return json_object
