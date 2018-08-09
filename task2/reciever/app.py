import asyncio
import aiohttp
import async_timeout
from flask import Flask, jsonify


RESPONSE_TIMEOUT = 2
SOURCES = ['http://source1', 'http://source222', 'http://source3']

app = Flask(__name__)
app.loop = asyncio.get_event_loop()


async def make_request(url):
    print(url)
    try:
        async with aiohttp.ClientSession() as session, async_timeout.timeout(RESPONSE_TIMEOUT):
            async with session.get(url) as response:
                return await response.json()
    except asyncio.TimeoutError:
        return None


@app.route('/', methods=['GET', 'POST'])
def index():

    responses = app.loop.run_until_complete(asyncio.gather(
        *(make_request(i) for i in SOURCES)
    ))
    result = []
    for i in responses:
        if i:
            result.extend(i)
    result.sort(key=lambda s: s['id'])

    return jsonify(result)


@app.before_request
def init_loop():
    try:
        app.loop = asyncio.get_event_loop()
    except RuntimeError:
        app.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(app.loop)


if __name__ == '__main__':
    app.run()
