#!/usr/bin/env python3

"""
we will implement a get_page function
(prototype: def get_page(url: str)
"""

import requests
import redis
from typing import Callable
from functools import wraps


# Connect to Redis
cache = redis.Redis()


def cache_page(expiration: int = 10):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            url = args[0]
            cached_content = cache.get(url)
            if cached_content:
                return cached_content.decode('utf-8')

            response = func(*args, **kwargs)
            cache.setex(url, expiration, response)
            return response
        return wrapper
    return decorator


@cache_page()
def get_page(url: str) -> str:
    """
    Obtain the HTML content of a URL and return it.
    Track how many times the URL was accessed
    and cache the result for 10 seconds.
    """
    cache.incr(f"count:{url}")
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    # Example usage
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(f"URL accessed {cache.get(f'count:{url}').decode('utf-8')} times")
