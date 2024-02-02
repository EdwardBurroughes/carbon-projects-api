from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class ProjectsResult(BaseModel):
    id: UUID
    url: str
    status: str
    country: Optional[str]
