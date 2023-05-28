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
        """<html>
        <head>
            <meta name="viewport" content="width=device-width; height=device-height;">
            <meta property="og:type" content="website">
            <meta property="og:image" content="/image" />
            <meta name="twitter:card" content="summary_large_image">
        </head>
        
        <body><img src="/image"/></body>
        </html>
        """,
        mimetype="text/html",
    )

@app.route('/image')
async def hello_2():
    return Response(
        random.choice(imgs),
        mimetype="image",
    )

app.run(port=os.environ.get("PORT", 8080), host="0.0.0.0")
