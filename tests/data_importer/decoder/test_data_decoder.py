import jwt

from data_importer.decoder.data_decoder import DataDecoder


class TestDataDecoder:
    def test_decode_should_return_decoded_value(self):
        decoded = {'resource': {'encoded_property1': 'test'}, 'prop2': 'test2'}
        encoded = {'prop2': 'test2'}
        encoded_prop = jwt.encode({'encoded_property1': 'test'}, '123456')
        encoded['resource'] = encoded_prop
        result = DataDecoder().decode(encoded)
        assert result == decoded


