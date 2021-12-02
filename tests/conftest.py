"""
Testing configurations
"""

import pytest
import random
import server as s
from datetime import datetime



@pytest.fixture(scope='session')
def country_data():
    return [
        {
            "id": idx,
            "iso": c,
            "num_stories": round(random.random() * 10) + 1,
            "last_updated_on": datetime.utcnow()
        }
        for idx, c in enumerate(s.constants.COUNTRIES)
    ]


@pytest.fixture(scope='session')
def country_detail():
    num_stories = 10
    return [
        {
            "id": idx,
            "headline": "Headline",
            "sentiment": round(random(), 2),
            "url": "http://url.com"

        }
        for idx in range(num_stories)
    ]


@pytest.fixture(scope='session')
def article_detail():
    return {
        "headline": "Headline",
        "description": "Description",
        "ml_summary": "ML Summary",
        "url": "http://url.com"
    }
