"""Module contains all APIs' models and constants."""

ERROR_REQUEST_COUNT = "ERROR_REQUEST_COUNT"

class Issue:
    def __init__(self, index, code, text):
        self.index = index
        self.code = code
        self.text = text

    def __str__(self):
        return {
            'index': self.index,
            'code': self.code,
            'text': self.text
        }

    def __hash__(self):
        return self.code

    def __eq__(self, other):
        if isinstance(other, Issue):
            return self.index == other.index
        return False


class InMemomryCache:
    cacheDictionary: dict

    def __init__(self):
        self.cacheDictionary = {ERROR_REQUEST_COUNT: 0}

    def increase_error_request_count(self):
        """increase the count for error request"""
        self.cacheDictionary[ERROR_REQUEST_COUNT] = self.cacheDictionary[ERROR_REQUEST_COUNT] + 1

    def get_error_request_count(self) -> int:
        """get the count for error request"""
        return self.cacheDictionary.get(ERROR_REQUEST_COUNT)

    def increase_operator_request_count(self, operator_name):
        """increase the count of error request for a specific operator"""
        if operator_name:
            if operator_name in self.cacheDictionary:
                self.cacheDictionary[operator_name] = self.cacheDictionary[operator_name] + 1
            else:
                self.cacheDictionary[operator_name] = 1

    def get_operator_request_count(self, operator_name) -> int:
        """get the count of error request for a specific operator"""
        if operator_name in self.cacheDictionary:
            return self.cacheDictionary[operator_name]
        else:
            return 0

