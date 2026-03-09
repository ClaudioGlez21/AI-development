"""
we can use schemas to leverage the use of pydantic to mapout data for issues of any resources in various cases
For example if we do a POST request, there is a certain schema for a body that we expect, when using an schema 
we can check for the integrity of that body and its fields
Another examples is creating enums for the declaration and use of several statuses of a certian issue, like OPEN, CLOSED, etc
"""

from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class IssuesStatus (str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

#Schema fro creating an issue
# Field allows us to add validation constrains
class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=5, max_length=1000)
    priority: IssuePriority = IssuePriority.medium #Use of our enum, using the medium priority by default

# when updating an issue, we may only want to change the content of an specific field, not the entire body, that is why we use optional
class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=1000)
    priority: Optional[IssuePriority] = None
    status: Optional[IssuesStatus] = None

class IssueOut(BaseModel):
    id: str
    title: str
    description: str
    priority: IssuePriority
    status: IssuesStatus