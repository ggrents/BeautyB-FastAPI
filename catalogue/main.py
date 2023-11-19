from fastapi import FastAPI

from catalogue.endpoints.file_router import file_router

app = FastAPI(title="Catalogue", description=""" 
Microservice, which is a set of endpoints for easy integration of the file database into the application.
Using this API, you can easily get the entire catalog of services provided in any necessaryвиде.
""")
app.include_router(file_router)