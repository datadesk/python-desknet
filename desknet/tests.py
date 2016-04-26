import unittest
from desknet import DeskNet


class TestDeskNet(unittest.TestCase):

    def setUp(self):
        self.client = DeskNet()

    def test_init(self):
        self.assertTrue(True)
