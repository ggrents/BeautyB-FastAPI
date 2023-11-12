from fastapi import FastAPI

from administration.endpoints.areas_router import areas_router
from administration.endpoints.clients_router import client_router
from administration.endpoints.feedbacks_router import feedback_router
from administration.endpoints.masters_router import master_router
from administration.endpoints.records_router import record_router
from administration.endpoints.services_router import service_router
from administration.endpoints.spots_router import spot_router
from administration.endpoints.tools_router import tool_router

app = FastAPI()

app.include_router(areas_router)
app.include_router(service_router)
app.include_router(master_router)
app.include_router(client_router)
app.include_router(tool_router)
app.include_router(spot_router)
app.include_router(record_router)
app.include_router(feedback_router)