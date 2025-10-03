from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User
from database import get_db
from security import get_vendor_user
from pydantic import BaseModel

router = APIRouter()


# --- Pydantic schema for vendor profile update ---
class VendorProfileUpdate(BaseModel):
    email: str
    bio: str | None = None
    company_name: str | None = None


# --- Route: Vendor updates their own profile ---
@router.put("/vendor/profile")
def update_vendor_profile(
    profile_data: VendorProfileUpdate,
    token_data: dict = Depends(get_vendor_user),
    db: Session = Depends(get_db)
):
    user_id = int(token_data["sub"])
    
    vendor = db.query(User).filter(User.id == user_id).first()

    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    # Optional: double-check role
    if vendor.role != "vendor":
        raise HTTPException(status_code=403, detail="Unauthorized access")

    # Update fields
    vendor.email = profile_data.email
    vendor.bio = profile_data.bio
    vendor.company_name = profile_data.company_name

    db.commit()
    db.refresh(vendor)

    return {"message": "Profile updated successfully", "vendor": {
        "id": vendor.id,
        "email": vendor.email,
        "bio": vendor.bio,
        "company_name": vendor.company_name
    }}





from fastapi import APIRouter, Depends
from security import get_current_user, get_admin_user, get_vendor_user

router = APIRouter()

@router.get("/me")
def read_profile(user: dict = Depends(get_current_user)):
    return {"user_id": user["sub"], "role": user["role"]}

@router.get("/admin")
def admin_panel(user: dict = Depends(get_admin_user)):
    return {"message": f"Welcome admin {user['sub']}"}

@router.get("/vendor")
def vendor_panel(user: dict = Depends(get_vendor_user)):
    return {"message": f"Welcome vendor {user['sub']}"}
