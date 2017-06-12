#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
import requests
logger = logging.getLogger(__name__)


class DeskNet(object):
    """
    Wrapper to DeskNet API.
    """
    def __init__(
        self,
        desknet_user=None,
        desknet_secret=None,
        auth_url="https://desk-net.com/api/token",
        api_url="https://desk-net.com/api/v1_0_1/elements/",
        verbosity=1
    ):
        """
        Create and return a new DeskNet client object.
        """
        self.desknet_user = desknet_user
        self.desknet_secret = desknet_secret
        self.auth_headers = {
            "client_id": desknet_user,
            "client_secret": desknet_secret,
            "grant_type": "client_credentials"
        }
        self.verbosity = verbosity
        self.auth_url = auth_url
        self.api_url = api_url
        self.access_token = None
        self.access_headers = None

    def auth(self):
        """
        Authenticate the user name and secret with the API.
        """
        logger.debug("Authorizing credentials")
        resp = requests.post(self.auth_url, params=self.auth_headers)
        self.access_token = resp.json()['access_token']
        self.access_headers = {
            "Authorization": "bearer {}".format(self.access_token),
            "Content-Type": "application/json;charset=UTF-8",
        }

    def post(self, payload):
        """
        Make and return a POST request to the DeskNet API.
        """
        logger.debug("POSTing to the DeskNet API")
        response = requests.post(self.api_url, headers=self.access_headers, data=json.dumps(payload))
        return response.json()

    def create(self, **kwargs):
        """
        Creates and returns a new DeskNet item as a dict
        """
        logger.debug("Creating new element")

        # Auth if we need to...
        if not self.access_token:
            self.auth()

        # Make the request to DeskNet API
        return self.post(kwargs)
