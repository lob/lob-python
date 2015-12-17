import unittest
import lob
# Setting the API key
lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

class StateFunctions(unittest.TestCase):
    def setUp(self):
        lob.api_key = 'test_fc26575412e92e22a926bc96c857f375f8b'

    def test_states(self):
        states = lob.State.list()
        self.assertTrue(isinstance(states.data, list))
