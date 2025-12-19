from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_home():
    return templates.TemplateResponse("home.html", {})

@app.get("/services", response_class=HTMLResponse)
async def read_services():
    return templates.TemplateResponse("services.html", {})

@app.get("/services/{service_slug}", response_class=HTMLResponse)
async def read_service_detail(service_slug: str):
    return templates.TemplateResponse("service_detail.html", {"service_slug": service_slug})
