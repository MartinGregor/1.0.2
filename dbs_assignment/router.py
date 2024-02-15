from fastapi import APIRouter

from dbs_assignment.endpoints import status
from dbs_assignment.endpoints import hello

router = APIRouter()
router.include_router(hello.router, tags=["hello"])
router.include_router(status.router, tags=["status"])
