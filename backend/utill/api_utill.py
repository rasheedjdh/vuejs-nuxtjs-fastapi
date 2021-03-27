"""Module contains all the helper and utility functions for all APIs"""
from typing import Any, Dict
from model.api_models import Issue
from collections import Counter
import random
import logging

ERROR_CODES = [error_code for error_code in range(50)]
LOGGER = logging.getLogger("utill")
RESOLVED = "resolved"
UNRESOLVED = "unresolved"
BACKLOG = "backlog"


def generate_lists() -> Dict[str, Any]:
    """Generate resolved, unresolved and backlog lists."""
    return {
        RESOLVED: [Issue(error_idx, random.choice(ERROR_CODES), f'Error ABC occured, that is `{RESOLVED}`')
                   for error_idx in range(50)],
        UNRESOLVED: [Issue(error_idx, random.choice(ERROR_CODES), f'Error DEF occured, that is `{UNRESOLVED}`')
                     for error_idx in range(50, 100)],
        BACKLOG: [Issue(error_idx, random.choice(ERROR_CODES), f'Error XYZ occured, that is in the `{BACKLOG}`')
                  for error_idx in range(100, 150)]
    }


def get_issues_intersection_counts(lists: Dict[str, Any]) -> Dict:
    """Return intersection count between resolved, unresolved and backlog lists."""
    return {
        f'{RESOLVED}_{UNRESOLVED}': len(extract_issues_intersection_between(lists[RESOLVED], lists[UNRESOLVED])),
        f'{RESOLVED},{BACKLOG}': len(extract_issues_intersection_between(lists[RESOLVED], lists[BACKLOG])),
        f'{UNRESOLVED}_{BACKLOG}': len(extract_issues_intersection_between(lists[UNRESOLVED], lists[BACKLOG]))
    }


def extract_issues_intersection_between(first_list: [], second_list: []) -> []:
    """Generate intersection count between two type of errors."""
    return [(first_iterator_item, second_iterator_item)
            for first_iterator_item in first_list for second_iterator_item in second_list
            if first_iterator_item.code == second_iterator_item.code]


def aggregate_resolved_issues(resolved_issues: [int]):
    """Return aggregated object that counts how many times a certain error.code was resolved"""
    return Counter(resolved_issues)


def resolved_issues_mapper(request_body: dict) -> [int]:
    """map resolved issues into array of integers 'codes' """
    issues = []
    for resolved_issue in request_body['resolved']:
        issues.append(resolved_issue['code'])
    return issues
