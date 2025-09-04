from flask import Flask

app = Flask(__name__)

# WARNING: Dummy secrets below are for EDR detection testing ONLY.
# Slack Bot Token (fake): xoxb-230766090094-242689517446-9BtpusikseNNIuay0vvB9yY1
# Google API Key (fake): AIzaNEnZzqXqnpszhPAMwr6ukbTObF8vw1qn2Ao

DUMMY_PASSWORD = "P@ssw0rd!123"  # hardcoded password (testing signature)
GITHUB_TOKEN = "ghp_PVpInAvCLHKhD6Ms0DLG8yP0uOZ7rIYdmtSp"    # GitHub classic PAT (fake)

@app.route("/")
def index():
    # Stripe key (fake): sk_live_Q8zucfN5lCi8c5tok5ej4esH
    return "Hello from a deliberately leaky app (for testing EDR secret detection)."

if __name__ == "__main__":
    app.run(port=8080)
