from allsafe_otp import generate_otp, generate_qr_code

secret = "JBSWY3DPEHPK3PXP"
otp = generate_otp(secret)
print("OTP from package:", otp)

uri = f"otpauth://totp/MyApp:daniel@allsafe.com?secret={secret}&issuer=MyApp"
generate_qr_code(uri)
