"""Module to setup fastapi API to expose API to the outside world."""
from typing import Any, Dict, Optional
from fastapi import FastAPI
from utill.api_utill import generate_lists, get_issues_intersection_counts, aggregate_resolved_issues, resolved_issues_mapper
from model.api_models import InMemomryCache
import logging
import uvicorn

LOGGER = logging.getLogger("API")
app = FastAPI()
inMemomryCache = InMemomryCache()


@app.get("/get_lists")
def get_lists(operator_name: Optional[str] = None) -> Dict[str, Any]:
    """
    record how many request for this api receievd for a specific operator
    # logs how many request in total for this api
    Return resolved, unresolved and backlog lists
    """
    inMemomryCache.increase_operator_request_count(operator_name)
    LOGGER.info(inMemomryCache.get_error_request_count())
    return generate_lists()


@app.get("/get_list_intersection_counts")
def get_list_intersection_counts() -> Dict[str, int]:
    """Return intersection count between resolved, unresolved and backlog lists."""
    return get_issues_intersection_counts(generate_lists())


@app.get("/get_error_request_count")
def get_error_request_count() -> int:
    """Return & logs how many requests for errors are received"""
    LOGGER.info(inMemomryCache.get_error_request_count())
    return inMemomryCache.get_error_request_count()


@app.get("/get_operator_request_count")
def get_operator_request_count(operator_name: Optional[str] = None) -> int:
    """Return & logs how many requests for errors are received from a specific operator"""
    LOGGER.info(inMemomryCache.get_operator_request_count(operator_name))
    return inMemomryCache.get_operator_request_count(operator_name)


@app.post("/get_aggregated_resolved_issues")
def get_aggregated_resolved_issues(resolved_issues: dict):
    """
    The operator can send all errors that are currently marked as resolved to this api,
    the api prints out how many times a certain error.code was resolved
    """
    return aggregate_resolved_issues(resolved_issues_mapper(resolved_issues))


def run(host: str, port: int) -> None:
    """Run the code challenge API."""
    uvicorn.run(app, host=host, port=port)
