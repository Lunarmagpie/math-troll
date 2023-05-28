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
            <!-- Primary Meta Tags -->
            <title>Meta Tags — Preview, Edit and Generate</title>
            <meta name="title" content="Meta Tags — Preview, Edit and Generate">
            <meta name="description" content="With Meta Tags you can edit and experiment with your content then preview how your webpage will look on Google, Facebook, Twitter and more!">

            <!-- Open Graph / Facebook -->
            <meta property="og:type" content="website">
            <meta property="og:url" content="/">
            <meta property="og:title" content="Meta Tags — Preview, Edit and Generate">
            <meta property="og:description" content="With Meta Tags you can edit and experiment with your content then preview how your webpage will look on Google, Facebook, Twitter and more!">
            <meta property="og:image" content="/image">

            <!-- Twitter -->
            <meta property="twitter:card" content="summary_large_image">
            <meta property="twitter:url" content="/">
            <meta property="twitter:title" content="Meta Tags — Preview, Edit and Generate">
            <meta property="twitter:description" content="With Meta Tags you can edit and experiment with your content then preview how your webpage will look on Google, Facebook, Twitter and more!">
            <meta property="twitter:image" content="/image">
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
