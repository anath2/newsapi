
# import pytest
# import aiohttp
# from math import floor
# from random import random
# from news_api import __version__, constants, construct_headlines_request, fetch_all


# def test_version():
#     assert __version__ == '0.1.0'


# @pytest.fixture
# def countries():
#     picked = []
#     num_to_pick = 2
#     countries = constants.COUNTRIES.copy()
#     for p in range(num_to_pick):
#         # Select without replacement
#         idx = floor(random() * len(countries))
#         picked.append(countries[idx])
#         countries.pop(idx)
#     return picked

# @pytest.mark.asyncio
# async def test_fetch(countries):
#     urls = [construct_headlines_request(c) for c in countries]
#     async with aiohttp.ClientSession(raise_for_status=True) as sess:
#         result = await fetch_all(sess, urls)
#         assert result
#         print(result)