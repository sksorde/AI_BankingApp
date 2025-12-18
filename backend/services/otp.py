
def verify_otp(code: str):
    if code == "123456":
        return {"status": "success", "message": "OTP verified successfully"}
    return {"status": "failed", "message": "Invalid OTP"}
