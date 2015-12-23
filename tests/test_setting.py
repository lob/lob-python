import unittest
import lob

class SettingFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

    def test_settings(self):
        settings = lob.Setting.list()
        self.assertEqual(settings.object, 'list')


    def test_find_setting(self):
        setting = lob.Setting.retrieve(id=200)
        self.assertEqual(setting.id, '200')

    def test_find_setting_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Setting.retrieve, id='test')


