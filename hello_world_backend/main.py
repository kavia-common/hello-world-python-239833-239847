"""
hello_world_backend FastAPI application.

This container exposes a minimal REST API with a single endpoint:
- GET /hello -> "Hello, World!"

Preview is expected to run on port 3001 (platform/orchestrator controlled).
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

openapi_tags = [
    {
        "name": "hello",
        "description": "Hello World endpoints.",
    }
]

app = FastAPI(
    title="Hello World Backend",
    description="A minimal FastAPI backend exposing a Hello World endpoint.",
    version="1.0.0",
    openapi_tags=openapi_tags,
)


@app.get(
    "/",
    response_class=PlainTextResponse,
    include_in_schema=False,
)
def root() -> str:
    """Redirect-less root response for quick health checks."""
    return "OK"


# PUBLIC_INTERFACE
@app.get(
    "/greet",
    response_class=PlainTextResponse,
    tags=["hello"],
    summary="Greet",
    description="Returns a plain-text greeting.",
    operation_id="greet",
)
def greet() -> str:
    """Return a plain-text greeting."""
    return "Hello"


# PUBLIC_INTERFACE
@app.get(
    "/bye",
    response_class=PlainTextResponse,
    tags=["hello"],
    summary="Bye",
    description="Returns a plain-text goodbye message.",
    operation_id="bye",
)
def bye() -> str:
    """Return a plain-text goodbye message."""
    return "Bye"


# PUBLIC_INTERFACE
@app.get(
    "/hello",
    response_class=PlainTextResponse,
    tags=["hello"],
    summary="Hello World",
    description="Returns a plain-text Hello World message.",
    operation_id="hello_world",
)
def hello() -> str:
    """Return the canonical Hello World message as plain text."""
    return "Hello, World!"
