from app.repositories.tenant_directory import TenantDirectoryRepository


class TenantDirectoryService:
    def __init__(self, repository: TenantDirectoryRepository):
        self.repository = repository

    def get_directory(self, search: str) -> dict[str, object]:
        rows = self.repository.search_directory(search)
        total_count = self.repository.count_all()
        active_count = self.repository.count_active()

        return {
            "rows": rows,
            "total_count": total_count,
            "active_count": active_count,
        }
