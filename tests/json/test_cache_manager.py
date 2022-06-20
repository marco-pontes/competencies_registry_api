import os.path

from data_importer.json.cache_manager import CacheManager


class TestCacheManager:
    def test_read_returns_correct_stored_json(self, tmpdir):
        sub = tmpdir.mkdir("sub")
        sub.join("testfile.json").write('{"prop1": "test", "prop2": "test2"}')
        result = CacheManager().read(os.path.join(sub, 'testfile.json'))
        expected = {'prop1': 'test', 'prop2': 'test2'}
        assert result == expected

    def test_write_correct_json_file(self, tmpdir):
        sub = tmpdir.mkdir("sub")
        sub.join("testfile.json").write('{"prop1": "test", "prop2": "test2"}')
        json_data = {'prop1': 'test', 'prop2': 'test2'}
        cache_file_path = os.path.join(sub, 'testfile.json')
        CacheManager().write(cache_file_path, json_data)
        result = CacheManager().read(cache_file_path)
        assert result == json_data


    def test_cache_exists_with_file_present_returns_true(self, tmpdir):
        sub = tmpdir.mkdir("sub")
        sub.join("testfile.json").write('{"prop1": "test", "prop2": "test2"}')
        cache_file_path = os.path.join(sub, 'testfile.json')
        result = CacheManager().cache_exists(cache_file_path)
        assert result == True


    def test_cache_exists_without_cache_file_returns_false(self, tmpdir):
        sub = tmpdir.mkdir("sub")
        cache_file_path = os.path.join(sub, 'testfile.json')
        result = CacheManager().cache_exists(cache_file_path)
        assert result == False



