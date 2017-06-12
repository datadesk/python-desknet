#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests DeskNet API wrapper.
"""
import os
import unittest
from desknet import DeskNet
from datetime import datetime


class DeskNetTest(unittest.TestCase):

    def setUp(self):
        self.desknet_user = os.environ['DESKNET_USER']
        self.desknet_secret = os.environ['DESKNET_SECRET']
        self.test_groups = [9229371]
        self.test_publications = [{
            'category': 9380971,
            'single': {
                'start': {
                    'date': datetime(2001, 1, 1).strftime('%Y-%m-%d'),
                    'time': datetime(2001, 1, 1).strftime('%H:%M:%S')
                }
            }
        }]
        self.client = DeskNet(self.desknet_user, self.desknet_secret, verbosity=3)

    def test_auth(self):
        self.assertTrue(self.client.access_token is None)
        self.client.auth()
        self.assertFalse(self.client.access_token is None)

    def test_create(self):
        obj = self.client.create(
            title="This is a only test",
            groups=self.test_groups,
            note="This is a test note",
            publications=self.test_publications,
        )
        self.assertEqual(obj['title'], "This is a only test")
        self.assertEqual(obj['groups'], self.test_groups)
        self.assertEqual(obj['note'], "This is a test note")
        self.assertEqual(obj['publications'][0]['category'], self.test_publications[0]['category'])
        self.assertTrue('id' in obj.keys())
        self.assertTrue('version' in obj.keys())
        self.assertTrue('modificationDate' in obj.keys())
