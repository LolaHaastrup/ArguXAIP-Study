"""
storage.py
==========

Where participant responses go.

READ THIS BEFORE DEPLOYING
--------------------------
Streamlit Community Cloud runs the app in a container whose filesystem is
EPHEMERAL. The container is restarted on redeploy, on code changes, and after
periods of inactivity, and anything written to disk is lost at that point.
Writing participant responses to a local file on Streamlit Cloud will
silently lose data partway through a study.

LocalJSONLStore below therefore exists for development only, and says so
loudly on screen. For a live study, configure a durable backend.

The store the app uses is chosen by what is present in st.secrets, so no code
change is needed to switch between development and the live study.

DATA PROTECTION
---------------
The choice of backend is not only a technical decision. Where participant
data is stored, and in which jurisdiction, has to match what your approved
ethics application states. Streamlit Community Cloud is a third-party host
outside the University's control. If your approved application says data will
be held on University systems, then a Google Sheet on a personal account does
not satisfy it, and neither does the container's disk. Confirm the storage
location against the approved application before recruiting.

I am not able to advise on whether a given arrangement satisfies UK GDPR or
University policy. That is a question for your supervisor and the University
research data management team.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class ResponseStore:
    """Interface for a participant response store."""

    #: Human readable name shown on the researcher page.
    name = "abstract"

    #: True when the backend survives a container restart.
    durable = False

    def save(self, record: Dict[str, Any]) -> bool:
        raise NotImplementedError

    def load_all(self) -> List[Dict[str, Any]]:
        raise NotImplementedError


class LocalJSONLStore(ResponseStore):
    """Append responses to a local JSON Lines file.

    DEVELOPMENT ONLY. On Streamlit Community Cloud this file does not survive
    a container restart, so responses collected through it will be lost.
    """

    name = "Local file (development only, NOT durable)"
    durable = False

    def __init__(self, path: str = "responses.jsonl") -> None:
        self.path = path

    def save(self, record: Dict[str, Any]) -> bool:
        try:
            with open(self.path, "a", encoding="utf-8") as handle:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            return True
        except OSError:
            return False

    def load_all(self) -> List[Dict[str, Any]]:
        if not os.path.exists(self.path):
            return []
        rows = []
        with open(self.path, "r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if line:
                    try:
                        rows.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
        return rows


class GoogleSheetsStore(ResponseStore):
    """Append each response as a row in a Google Sheet, via a service account.

    Configure by adding the following to .streamlit/secrets.toml, or to the
    Secrets box in the Streamlit Cloud app settings:

        sheet_id = "the id from the sheet's URL"

        [gcp_service_account]
        type = "service_account"
        project_id = "..."
        private_key_id = "..."
        private_key = "-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n"
        client_email = "...@....iam.gserviceaccount.com"
        client_id = "..."
        token_uri = "https://oauth2.googleapis.com/token"

    The sheet must be shared with the service account's client_email address,
    with edit permission.

    VERIFY THE gspread CALLS BELOW against the current gspread documentation
    before you rely on them. The library's authentication helpers have changed
    across major versions, and I have not been able to exercise this path
    against a live sheet from here.
    """

    name = "Google Sheet"
    durable = True

    #: Column order. Keep stable, because rows are appended positionally.
    COLUMNS = [
        "timestamp",
        "participant_code",
        "consent_version",
        "retention_years",
        "verdict_shown",
        "cqs_available",
        "cqs_challenged",
        "premises_grounded",
        "explainee_moves",
        "closed_by_user",
        "seconds_on_dialogue",
        "questionnaire_json",
        "open_responses_json",
        "transcript_json",
    ]

    def __init__(self, service_account_info: Dict[str, Any], sheet_id: str) -> None:
        import gspread  # imported lazily so the app runs without it installed

        self._client = gspread.service_account_from_dict(service_account_info)
        self._sheet_id = sheet_id

    def _worksheet(self):
        return self._client.open_by_key(self._sheet_id).sheet1

    def save(self, record: Dict[str, Any]) -> bool:
        try:
            worksheet = self._worksheet()
            if not worksheet.get_all_values():
                worksheet.append_row(self.COLUMNS)
            worksheet.append_row(
                [str(record.get(column, "")) for column in self.COLUMNS]
            )
            return True
        except Exception:
            return False

    def load_all(self) -> List[Dict[str, Any]]:
        try:
            return self._worksheet().get_all_records()
        except Exception:
            return []


def get_store(secrets: Optional[Any] = None) -> ResponseStore:
    """Choose a store based on what is configured.

    Returns GoogleSheetsStore when both a service account and a sheet id are
    present in secrets, and LocalJSONLStore otherwise. The app displays which
    store is active and warns when the active store is not durable, so a study
    cannot be run accidentally against the development backend.
    """
    if secrets is None:
        return LocalJSONLStore()
    try:
        has_account = "gcp_service_account" in secrets
        has_sheet = "sheet_id" in secrets
    except Exception:
        return LocalJSONLStore()

    if has_account and has_sheet:
        try:
            return GoogleSheetsStore(
                dict(secrets["gcp_service_account"]), secrets["sheet_id"]
            )
        except Exception:
            # Fall back rather than crash mid-session, and let the app warn.
            return LocalJSONLStore()
    return LocalJSONLStore()


def build_record(
    participant_code: str,
    outcome: Dict[str, Any],
    transcript: List[Dict[str, Any]],
    questionnaire: Dict[str, Any],
    open_responses: Dict[str, str],
    retention_years: int,
    consent_version: str,
    seconds_on_dialogue: Optional[float] = None,
) -> Dict[str, Any]:
    """Assemble one participant's complete record.

    No field here identifies the participant. The participant code is
    randomly generated in the browser session and is not linked to any
    identity, which is what allows the study to describe the data as
    anonymous rather than pseudonymous.
    """
    return {
        "timestamp": _now(),
        "participant_code": participant_code,
        "consent_version": consent_version,
        "retention_years": retention_years,
        "verdict_shown": outcome.get("verdict"),
        "cqs_available": outcome.get("cqs_available"),
        "cqs_challenged": outcome.get("cqs_challenged"),
        "premises_grounded": outcome.get("premises_grounded"),
        "explainee_moves": outcome.get("explainee_moves"),
        "closed_by_user": outcome.get("closed_by_user"),
        "seconds_on_dialogue": (
            round(seconds_on_dialogue, 1) if seconds_on_dialogue else ""
        ),
        "questionnaire_json": json.dumps(questionnaire, ensure_ascii=False),
        "open_responses_json": json.dumps(open_responses, ensure_ascii=False),
        "transcript_json": json.dumps(transcript, ensure_ascii=False),
    }
