from pydantic import BaseModel, Field

class ImportCollaboratorSchema(BaseModel):
    client_id: int = Field(..., gt=1)
    file_path: str = Field(..., min_length=1)