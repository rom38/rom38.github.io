from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles


routes = [
    Mount(
        '/', app=StaticFiles(directory='static', html = True),
         name="static"
         ),
]

app = Starlette(routes=routes)
