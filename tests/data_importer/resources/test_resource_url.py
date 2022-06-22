from unittest import TestCase

from data_importer.resources.resource_url import ResourceURL


class TestResourceURL:
    class TestResourceURLWithURL(TestCase):
        def test_invalid_api_url_raises_exception(self):
            with self.assertRaises(Exception) as context:
                ResourceURL(url='http://test.com/envelopes')
            assert 'Invalid API URL' == context.exception.args[0]

        def test_valid_url_has_correct_complete_url(self):
            resource_url = ResourceURL(url='https://staging.credentialengineregistry.org/envelopes')
            assert 'https://staging.credentialengineregistry.org/envelopes' == resource_url.complete_url

        def test_valid_url_has_sub_path(self):
            resource_url = ResourceURL(url='https://staging.credentialengineregistry.org/envelopes')
            assert 'envelopes' == resource_url.sub_path

    class TestResourceURLWithoutParams(TestCase):
        def test_raises_exception(self):
            with self.assertRaises(Exception) as context:
                ResourceURL()
            assert 'Url or sub_path are mandatory parameters' == context.exception.args[0]

    class TestResourceURLWithOnlyUUID(TestCase):
        def test_sub_path_without_uuid_raises_exception(self):
            with self.assertRaises(Exception) as context:
                ResourceURL(uuid='2145-ab45-be33')
            assert 'Url or sub_path are mandatory parameters' == context.exception.args[0]

    class TestResourceURLWithOnlySubPath(TestCase):
        def test_has_correct_sub_path(self):
            resource_url = ResourceURL(sub_path='envelopes')
            assert 'envelopes' == resource_url.sub_path

        def test_resource_has_complete_url(self):
            resource_url = ResourceURL(sub_path='envelopes')
            assert 'https://staging.credentialengineregistry.org/envelopes' == resource_url.complete_url


    class TestResourceURLWithURLParamContainingResourceID(TestCase):
        def setUp(self):
            self.resource_url = ResourceURL(url='https://staging.credentialengineregistry.org/resources/2145-ab45-be33')

        def test_has_correct_sub_path(self):
            assert 'resources' == self.resource_url.sub_path

        def test_has_correct_uuid(self):
            assert '2145-ab45-be33' == self.resource_url.uuid

        def test_resource_has_correct_complete_url(self):
            assert 'https://staging.credentialengineregistry.org/resources/2145-ab45-be33' == self.resource_url.complete_url

    class TestResourceURLWithSubPathAndUUIDParams(TestCase):
        def setUp(self):
            self.resource_url = ResourceURL(sub_path='resources', uuid='2145-ab45-be44')

        def test_has_correct_sub_path(self):
            assert 'resources' == self.resource_url.sub_path

        def test_has_correct_uuid(self):
            assert '2145-ab45-be44' == self.resource_url.uuid

        def test_resource_has_correct_complete_url(self):
            assert 'https://staging.credentialengineregistry.org/resources/2145-ab45-be44' == self.resource_url.complete_url
