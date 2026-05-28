"""Modal entrypoints for the automation runtime.

This file is intentionally import-safe without Modal installed so unit tests can run
in a zero-dependency environment. Install the `modal` optional dependency before
running `modal deploy modal_app.py`.
"""
from __future__ import annotations

try:
    import modal
except ImportError:  # pragma: no cover - local tests do not require Modal
    modal = None

if modal is not None:
    app = modal.App("sa-sme-automation-runtime")

    image = modal.Image.debian_slim(python_version="3.11").pip_install(
        "google-api-python-client>=2.0.0",
        "google-auth>=2.0.0",
    )

    @app.function(image=image, schedule=modal.Cron("30 6 * * 1-5"), secrets=[])
    def invoiceflow_daily_batch() -> dict[str, int]:
        """Production wiring placeholder.

        Wire concrete Google/Email adapters here once client credentials are added
        as Modal Secrets. The pure workflow logic is tested in
        `automation_platform.workflows.invoiceflow`.
        """

        return {"processed": 0, "exceptions": 0, "documents_seen": 0}

    @app.function(image=image)
    @modal.fastapi_endpoint(method="POST", docs=True)
    def healthcheck(payload: dict | None = None) -> dict[str, str]:
        return {"status": "ok", "runtime": "modal-automation-runtime"}
else:
    app = None
