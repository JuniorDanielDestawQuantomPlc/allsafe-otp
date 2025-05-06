# Allsafe OTP

Allsafe OTP is a simple Python library for generating secure, time-based (TOTP) and counter-based (HOTP) one-time passwords (OTPs) for multi-factor authentication (MFA) systems. The library is designed for easy integration into Python-based applications, including Django apps.

## Features:
- **TOTP (Time-based One-Time Password)**: Generate OTPs that expire after a set time interval.
- **HOTP (Counter-based One-Time Password)**: Generate OTPs based on a moving counter.
- **Secure**: Uses HMAC-SHA1 for OTP generation.
- **Flexible**: Can be used in any Python application.
- **Easy Integration**: Compatible with Django and other Python frameworks.

## Installation:
```bash
pip install allsafe-otp
