# sensitive_data_simulation.py
"""
⚠️ This script is for EDR/DLP testing purposes only.
It contains simulated sensitive information (fake secrets, fake keys, etc.)
to trigger security tools. DO NOT use in production.
"""

# Simulated RSA Private Key (DO NOT USE IN PRODUCTION)
fake_rsa_key = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA7VJZHVw8KJFt7O3Qz9X2Bz3+4FakeKeyHerexEMmmkAGt+YZP
9EzJQ7KZZFakeBase64ThatLooksRealwLZqTb2KxF3YkURJz9R+cmidH3d9c7xT
ZxdxGZZO+ALfZB6WZn7efG2N9KD5N+XJFAKEKEYBADl3xD+e1FSXafR7YGB0fE7
-----END RSA PRIVATE KEY-----
"""

# Simulated API Keys
fake_aws_key = "AKIAIOSFODNN7EXAMPLE"
fake_aws_secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Simulated Passwords
db_password = "SuperSecret123!"
admin_password = "P@ssw0rd!"

# Simulated OAuth Token
fake_oauth_token = "ya29.A0ARrdaM-fake-token-string-1234567890"

# Simulated JWT
fake_jwt = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6Im1hbmFnZXIifQ."
    "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"
)

# Simulated DB connection string
fake_db_conn_string = "postgres://admin:SuperSecret123@localhost:5432/mydatabase"

# Simulated encryption key
encryption_key = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"

# Sample usage
def connect_to_fake_db():
    print(f"Connecting to database with: {fake_db_conn_string}")

def authenticate_with_token():
    print(f"Authenticating with OAuth token: {fake_oauth_token}")

def load_private_key():
    print("Loaded RSA Private Key.")

if __name__ == "__main__":a
    connect_to_fake_db()
    authenticate_with_token()
    load_private_key()
