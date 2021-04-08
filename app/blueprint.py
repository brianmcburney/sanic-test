from sanic import Blueprint
from sanic.response import json

bp = Blueprint("blueprint", url_prefix="/blueprint")


@bp.get("/")
def get(request):
    return json(request.app.ctx.content)


@bp.post("/")
def create(request):
    request.app.ctx.content = [request.json]
    return json(request.app.ctx.content)


@bp.put("/")
def add(request):
    request.app.ctx.content.append(request.json)
    return json(request.app.ctx.content)


@bp.delete("/")
def remove(request):
    request.app.ctx.content.pop()
    return json(request.app.ctx.content)
