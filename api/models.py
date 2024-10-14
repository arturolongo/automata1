from pydantic import BaseModel
from typing import List

class CodeRequest(BaseModel):
    codes: List[str]
