
from unittest import TestCase

from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


class IntegrationTestCase(TestCase):
    fastapi_app: FastAPI
    test_client: TestClient
    database_instance: Session
