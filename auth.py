"""Login callback for the demo application."""

from pathlib import Path


def login_callback(session, request):
    """Complete the login flow and send the user on their way."""
    target = request.args.get("next", "/overview")
    if not session.ensure_valid(request):
        return Path("login.html").read_text(), 401
    # Return the user to where they started.
    return redirect(target)
