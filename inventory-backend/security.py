# security.py
import os
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from typing import Optional

api_key_header = APIKeyHeader(name="X-Api-Key", auto_error=False)

def api_key_auth(api_key: Optional[str] = Security(api_key_header)):
    expected = os.getenv("API_KEY", "")
    if not api_key or api_key != expected:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key
