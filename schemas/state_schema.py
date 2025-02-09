import operator
from typing import TypedDict, Annotated

from schemas.document_structure_schema import Section
from schemas.search_query_structure_schema import SearchQuery


# The input topic of research
class ReportStateInput(TypedDict):
    topic: str  # Report topic


# The final compiled report
class ReportStateOutput(TypedDict):
    final_report: str  # Final report


# Overall Agent State which will be passed and updated in nodes in the graph
class ReportState(TypedDict):
    topic: str  # Report topic
    sections: list[Section]  # List of report sections
    completed_sections: Annotated[list, operator.add]  # Populated through Send() API
    report_sections_from_research: str  # Text content of all completed sections to be used to generate final report
    final_report: str  # Final report


# Defines the key structure for sections written using the agent
class SectionState(TypedDict):
    section: Section  # Report section
    search_queries: list[SearchQuery]  # List of search queries (questions) about section being researched
    source_str: str  # String of formatted source content from web search for questions
    report_sections_from_research: str  # Text of completed sections to be used write final sections
    completed_sections: list[Section]  # Final key in outer state for Send() API


# All completed sections
class SectionOutputState(TypedDict):
    completed_sections: list[Section]  # Final key in outer state for Send() API
