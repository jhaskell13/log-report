from pathlib import Path
import json

def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_nonempty():
    """The report file is not empty."""
    assert Path("/app/report.json").stat().st_size > 0, "report.json is empty"

def test_report_has_valid_keys():
    """The report file uses the required format and keys."""
    with open('/app/report.json', 'r') as f:
      report = json.load(f)

    expected_keys = {"total_requests", "unique_ips", "top_path"}
    assert expected_keys.issubset(report.keys()), "report.json is missing required keys"
