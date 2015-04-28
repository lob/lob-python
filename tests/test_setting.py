import unittest
import lob
# Setting the API key

class SettingFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_0dc8d51e0acffcb1880e0f19c79b2f5b0cc'

    def test_settings(self):
        settings = lob.Setting.list()
        self.assertEqual(settings.object, 'list')


    def test_find_setting(self):
        setting = lob.Setting.retrieve(id=200)
        self.assertEqual(setting.id, '200')

    def test_find_setting_fail(self):
        self.assertRaises(lob.error.InvalidRequestError, lob.Setting.retrieve, id='test')


