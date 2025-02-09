from typing import List

from pydantic import BaseModel, Field


class Section(BaseModel):
    name: str = Field(
        description="Name for a particular section of the report.",
    )
    description: str = Field(
        description="Brief overview of the main topics and concepts to be covered in this section.",
    )
    research: bool = Field(
        description="Whether to perform web search for this section of the report."
    )
    content: str = Field(
        description="The content for this section."  # To be filed in by Section Write Agent
    )


class Sections(BaseModel):
    sections: List[Section] = Field(
        description="All the Sections of the overall report.",
    )
