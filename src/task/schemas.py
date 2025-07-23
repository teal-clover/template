from pydantic import BaseModel, ConfigDict, Field

class TaskSchema(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str = Field(max_length=255)

    model_config = ConfigDict(from_attributes=True)
