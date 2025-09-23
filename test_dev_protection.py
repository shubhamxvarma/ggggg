# test_dev_protection.py
# ⚠️ This file contains FAKE credentials for security testing only.
# Use it to test Check Point EDR Developer Protection.
# Fake RSA Private Key
RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgQC3EXAMPLEKEYDATA1234567890ABCDEFGH
ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ABCDEFGH
-----END RSA PRIVATE KEY-----"""
# Fake AWS Access Keys
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
# Fake GitHub Personal Access Token
GITHUB_TOKEN = "ghp_1234567890abcdef1234567890abcdef1234"
# Fake Google API Key
GOOGLE_API_KEY = "AIzaSyD-FAKEKEY1234567890abcdefghijklmnop"
# Fake Database Password
DB_PASSWORD = "SuperSecretP@ssw0rd!"
# Dummy usage in code
def connect_to_service():
   print("Connecting with AWS key:", AWS_ACCESS_KEY_ID)
   print("Using secret:", AWS_SECRET_ACCESS_KEY)
   print("GitHub Token:", GITHUB_TOKEN)
   print("Google API Key:", GOOGLE_API_KEY)
   print("Database Password:", DB_PASSWORD)
if __name__ == "__main__":
   connect_to_service()