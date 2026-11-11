"""Login callback for the demo application."""

from pathlib import Path
from urllib.parse import urlparse


def login_callback(session, request):
    """Complete the login flow and send the user on their way."""
    target = request.args.get("next", "/overview")
    if not session.ensure_valid(request):
        return Path("login.html").read_text(), 401
    # A redirect target is only trusted when it stays on the application.
    if urlparse(target).netloc or not target.startswith("/"):
        target = "/overview"
    return redirect(target)
