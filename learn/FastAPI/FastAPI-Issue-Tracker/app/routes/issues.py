import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueOut, IssueUpdate, IssuesStatus
from app.storage import load_data, save_data


router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

# The reponse model, filters out the respone and the return value will only containt the values that the IssueOut schema has
@router.get("/", response_model=list[IssueOut])
async def get_issues():
    """Retrieve all issues"""
    issues = load_data()
    return issues

#Post request to create a single issue with the Issue out schema
@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED)
def create_issue(payload: IssueCreate):
    """Create a new issue"""
    issues = load_data()
    new_issue = {
        "id": str(uuid.uuid4()), #Generates a unique identifier for the new issue
        "title": payload.title,
        "description": payload.description,
        "priority": payload.priority,
        "status": IssuesStatus.open,
    }
    issues.append(new_issue)
    save_data(issues)
    return new_issue

#Request to return a single issue give an id, using the IssueOut schema as the response model
@router.get("/{issue_id}", response_model=IssueOut)
def get_issue(issue_id: str):
    """Retrieve a single issue by ID"""
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.put("/{issue_id}", response_model=IssueOut)
def update_issue(issue_id:str, payload: IssueUpdate):
    """Update an existing issue given an ID"""
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            updated_issue = {**issue, **payload.dict(exclude_unset=True)}
            issues[index] = updated_issue
            save_data(issues)
            return updated_issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def deleate_issue(issue_id: str):
    """Delete an issue given an ID"""
    issues = load_data()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            del issues[index]
            save_data(issues)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")