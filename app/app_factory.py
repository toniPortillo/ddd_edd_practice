from typing import List
from fastapi import FastAPI


class AppFactory:
    @classmethod
    def create_app(
        cls, 
        container_subscriber: List, 
    ) -> FastAPI:
        pass
