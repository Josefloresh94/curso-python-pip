import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/contact", response_class=HTMLResponse)
async def read_root():
    return """
    <h1>Hola soy una página</h1>
"""


def run():
    store.get_categories()


if __name__ == "__main__":
    run()
