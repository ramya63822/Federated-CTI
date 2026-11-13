import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from flask import Flask, request
from flask_cors import CORS

from utils.database import init_db, save_visitor
from services.ml_service import load_model
from routes.auth import auth_bp
from routes.monitor import monitor_bp
from routes.ledger import ledger_bp
from routes.upload import upload_bp
from routes.reports import reports_bp
from routes.settings import settings_bp
from routes.blocked_ips import blocked_bp

app = Flask(
    __name__,
    template_folder=PROJECT_ROOT / "templates",
    static_folder=PROJECT_ROOT / "static",
)
CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(monitor_bp)
app.register_blueprint(ledger_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(reports_bp)
app.register_blueprint(settings_bp)
app.register_blueprint(blocked_bp)

SKIP_PREFIXES = ("/static", "/api/monitor/visitors", "/favicon.ico")


def get_client_ip():
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.remote_addr


@app.before_request
def track_visitor():
    if request.method == "OPTIONS":
        return
    if request.path.startswith(SKIP_PREFIXES) or request.path.startswith("/api/"):
        return
    try:
        save_visitor(
            get_client_ip(),
            request.method,
            request.path,
            request.headers.get("User-Agent", "")[:200],
        )
    except Exception:
        pass


if __name__ == "__main__":
    init_db()
    load_model()
    app.run(host="0.0.0.0", port=5000, debug=True)
