from fastapi import APIRouter, Depends, HTTPException, Path
from ..auth import get_current_tenant

router = APIRouter()

@router.get("/{tenant_id}/{context_id}")
async def get_policy(
    tenant_id: int = Path(...),
    context_id: str = Path(...),
    tenant=Depends(get_current_tenant)
):
    # Optional: enforce tenant ID matches token
    if tenant.id != tenant_id:
        raise HTTPException(status_code=403, detail="Tenant mismatch")

    # Mocked policy response
    return {
        "mam": 42000.00,
        "asking_price": 50000.00,
        "strategy": "concede_slow",
        "rules_source": "mock-v1",
        "context_id": context_id
    }
