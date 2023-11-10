from sqlalchemy import select, Insert, Update
from sqlalchemy.ext.asyncio import AsyncSession

from salon.entities.models.tool import Tool
from salon.entities.schemas.tool import ToolCreateUpdate


async def get_tools(db: AsyncSession):
    query = select(Tool)
    result = await db.execute(query)
    return result.scalars().all()


async def get_tool_by_id(db: AsyncSession, tool_id: int):
    result = await db.get(Tool, tool_id)
    return result


async def get_tools_by_master(db: AsyncSession, master_id: int):
    query = select(Tool).where(master_id=master_id)
    result = await db.execute(query)
    return result.scalars().all()


async def delete_tool(db: AsyncSession, tool: Tool):
    await db.delete(tool)
    await db.commit()


async def add_tool(db: AsyncSession, tool: ToolCreateUpdate):
    query = Insert(Tool).values(**tool)
    await db.execute(query)


async def update_tool(db: AsyncSession, tool: ToolCreateUpdate):
    query = Update(Tool).values(**tool)
    await db.execute(query)
