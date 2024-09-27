import time
from datetime import datetime, timedelta, timezone

data = {
    "youtube": {
        "Watch YouTube Video #1": "070624",
        "Major Games #1": "070624",
        "Watch YouTube Shorts #3": "070624",
        "Watch YouTube Shorts #4": "159390"
    },
    "answer": {
        "choice_1": 13,
        "choice_2": 14,
        "choice_3": 11,
        "choice_4": 12
    },
    # Expires in 24 hours from now, in UTC
    "expires": int((datetime.now(timezone.utc) + timedelta(days=1)).timestamp())
}

def get_data():
    return data
