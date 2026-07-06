from fastapi import APIRouter

from backend.app.services.system_service import get_system_info

router = APIRouter()


@router.get("/system/info")
def system_info():
    return get_system_info()