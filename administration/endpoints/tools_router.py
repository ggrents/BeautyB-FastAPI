from http.client import OK
from typing import Annotated

from fastapi import APIRouter, Depends, Path, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession

from administration.data_access import services, tools
from administration.database import get_async_session

tool_router = APIRouter(prefix="/tools", tags=["Tools"])


@tool_router.get("")
async def list_tools(db: AsyncSession = Depends(get_async_session)):
    return await tools.get_tools(db)


@tool_router.get("/{tool_id}")
async def get_tool_by_id(tool_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    tool = await tools.get_tool_by_id(db, tool_id)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")
    return tool


@tool_router.get("/master/{master_id}")
async def get_tool_by_master(master_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    tool = await tools.get_tools_by_master(db, master_id)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")
    return tool


@tool_router.delete("/{tool_id}")
async def delete_tool(tool_id: Annotated[int, Path()], db: AsyncSession = Depends(get_async_session)):
    tool = await tools.get_tool_by_id(db, tool_id)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")
    await tools.delete_tool(db, tool)
    return OK
