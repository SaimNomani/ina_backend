from pydantic import BaseModel, EmailStr

class TenantCreate(BaseModel):
    email: EmailStr
    password: str
    client_policy_api_endpoint: str | None = None

class TenantOut(BaseModel):
    id: int
    email: EmailStr
    client_policy_api_endpoint: str | None

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
    tenant_id: int
