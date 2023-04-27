
from unittest import TestCase

from fastapi import FastAPI
from fastapi.testclient import TestClient


class IntegrationTestCase(TestCase):
    fastapi_app: FastAPI
    test_client: TestClient
