from fastapi import FastAPI

from app.mock.mock_aws import MockAWSService


app = FastAPI(
    title="AI Cloud Cost Recovery Agent",
    version="0.1.0"
)

aws = MockAWSService()


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/mock-aws/account")
def get_account():
    return {
        "account_id": aws.get_account_id()
    }


@app.get("/mock-aws/cost")
def get_cost():
    return aws.get_cost()


@app.get("/mock-aws/services")
def get_services():
    return aws.get_services()


@app.get("/mock-aws/resources")
def get_resources():
    return aws.get_resources()