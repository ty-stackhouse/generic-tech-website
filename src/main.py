from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_home():
    return """<html><head><title>TechConsult Group</title></head><body><h1>TechConsult Group</h1><p>Enterprise Solutions for Modern Challenges</p></body></html>"""

@app.get("/services", response_class=HTMLResponse)
async def read_services():
    return """<html><head><title>Services</title></head><body><h1>Our Services</h1><ul><li>Cloud Migration</li><li>Security Audit</li><li>DevOps Optimization</li></ul></body></html>"""

@app.get("/services/{service_slug}", response_class=HTMLResponse)
async def read_service_detail(service_slug: str):
    return f"""<html><head><title>{service_slug}</title></head><body><h1>{service_slug}</h1><p>Description and details about {service_slug}.</p></body></html>"""
