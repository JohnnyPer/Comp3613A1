from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import status

from app.dependencies.session import SessionDep
from app.dependencies.auth import AdminDep, IsUserLoggedIn, get_current_user, is_admin
from app.repositories.tenant_directory import TenantDirectoryRepository
from app.services.tenant_directory_service import TenantDirectoryService
from . import router, templates


@router.get("/admin", response_class=HTMLResponse)
async def admin_home_view(
    request: Request,
    user: AdminDep,
    db: SessionDep,
    search: str = ""
):
    repository = TenantDirectoryRepository(db)
    service = TenantDirectoryService(repository)

    directory = service.get_directory(search)

    return templates.TemplateResponse(
        request=request,
        name="admin.html",
        context={
            "user": user,
            "rows": directory["rows"],
            "total_count": directory["total_count"],
            "active_count": directory["active_count"],
            "search": search,
        }
    )