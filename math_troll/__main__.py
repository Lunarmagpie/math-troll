from quart import Quart, Response
import random

import os

app = Quart(__name__)

img_paths = [
    "math1.jpg",
    "math2.jpg",
]

imgs = []

for path in img_paths:
    with open(path, "rb") as f:
        imgs.append(f.read())


@app.route('/')
async def hello():
    return Response(
        """<head><meta property="og:image" content="/image" /> <img src="/image"/></head>""",
        mimetype="text/html",
    )

@app.route('/image')
async def hello_2():
    return Response(
        random.choice(imgs),
        mimetype="image",
    )

app.run(port=os.environ.get("PORT", 8080), host="0.0.0.0")
