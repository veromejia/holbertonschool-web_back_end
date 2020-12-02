#!/usr/bin/env python3
"""Redis exercises module"""
import redis
import uuid
from typing import Union, Callable, Optional, List
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts how many times methods of the Cache class
    have been called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs for a particular
    function"""
    in_keys = method.__qualname__ + ":inputs"
    out_keys = method.__qualname__ + ":outputs"

    @wraps(method)
    def set_history(self, *args, **kwargs):
        """ Set list keys to wrapped function """
        self._redis.rpush(in_keys, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(out_keys, str(res))
        return res
    return set_history


def replay(method: Callable) -> None:
    """ Ouput log of actions taken on method """
    counter_key = method.__qualname__
    input_list_key = method.__qualname__ + ':inputs'
    output_list_key = method.__qualname__ + ':outputs'
    this = method.__self__

    counter = this.get_str(counter_key)
    history = list(zip(this.get_list(input_list_key),
                       this.get_list(output_list_key)))
    print("{} was called {} times:".format(counter_key, counter))
    for call in history:
        value = this.get_str(call[0])
        key = this.get_str(call[1])
        print("{}(*{}) -> {}".format(counter_key, value, key))


class Cache:
    """Cache classs"""

    def __init__(self):
        self._redis = redis.Redis(host="localhost", port=6379)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key and Stores the input data in
        Redis using a random key"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Gets the value of a string and returns it converted to
        the right type"""
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, b_string: bytes) -> str:
        """ Convert bytes to str """
        return b_string.decode('utf-8')

    def get_int(self, b_int: bytes) -> int:
        """ Convert bytes to int """
        result = 0
        result = result * 256 + int(b_int)
        return result

    def get_list(self, k: str) -> List:
        """ Convert bytes from store to list """
        return self._redis.lrange(k, 0, -1)
