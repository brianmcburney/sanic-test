from sanic import Sanic
from sanic.response import json

from app.blueprint import bp

app = Sanic("test")
app.blueprint(bp)


@app.get("/")
def get_method(request):
    try:
        return json(request.app.ctx.content)
    except AttributeError:
        return json({})


@app.post("/")
def post_method(request):
    request.app.ctx.content = [request.json]
    return json(request.app.ctx.content)


@app.post("/post")
def post_method_works(request):
    request.app.ctx.content = [request.json]
    return json(request.app.ctx.content)


@app.put("/")
async def add(request):
    request.app.ctx.content.append(request.json)
    return json(request.app.ctx.content)


@app.delete("/")
async def remove(request):
    request.app.ctx.content.pop()
    return json(request.app.ctx.content)
