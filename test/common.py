import os
import random
import string

from oss.compat import to_bytes


OSS_ID = os.getenv("OSS_TEST_ACCESS_KEY_ID")
OSS_SECRET = os.getenv("OSS_TEST_ACCESS_KEY_SECRET")
OSS_ENDPOINT = os.getenv("OSS_TEST_ENDPOINT")
OSS_BUCKET = os.getenv("OSS_TEST_BUCKET")


def random_string(n):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(n))


def random_bytes(n):
    return to_bytes(random_string(n))