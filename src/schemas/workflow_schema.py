from pydantic import BaseModel

class WorkflowCreate(BaseModel):
    name: str

class WorkflowOut(BaseModel):
    id: int
    name: str
