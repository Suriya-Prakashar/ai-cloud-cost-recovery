import json
from pathlib import Path


class MockAWSService:

    def __init__(self):
        data_path = Path(__file__).parent / "aws_data.json"

        with open(data_path, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    def get_cost(self):
        return self.data["daily_cost"]

    def get_services(self):
        return self.data["services"]

    def get_resources(self):
        return self.data["resources"]

    def get_account_id(self):
        return self.data["account_id"]