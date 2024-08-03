from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from schemas import Item
from utils import find_favs
from constans import points

temmplates = Jinja2Templates(directory="templates")
app = FastAPI()

@app.get("/")
async def home(request: Request):
    return temmplates.TemplateResponse("index.html", {"request": request})


@app.post("/show-results")
async def show_results(request: Request):
    item = Item(**dict(await request.form()))
    dts = list(item.dict().items())
    data = dict(filter(lambda x: x[1] is not None, dts))
    data.update(find_favs(data))
    mood = points.get(data.get("fav_color", "").lower(), 0) + points.get(data.get("fav_animal", "").lower(), 0)
    return temmplates.TemplateResponse("results.html", {"request": request, "mood": mood, **data})