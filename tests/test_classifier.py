import pytest
from app.services.classifier import classify_ticket

def test_empty_ticket_should_not_crash_and_return_unknown():
    out = classify_ticket({"id": "t1", "text": ""})
    # category should fall back to other and ticket_id preserved
    assert out["category"] == "other"
    assert out["ticket_id"] == "t1"
    # urgency may be the default medium but must be one of the valid levels
    assert out["urgency"] in {"low","medium","high","critical"}
    # confidence is a float in the unit interval
    assert isinstance(out["confidence"], float)
    assert 0.0 <= out["confidence"] <= 1.0

def test_none_ticket_should_not_crash_and_return_unknown():
    out = classify_ticket(None)
    # missing ticket should be handled gracefully
    assert out["category"] == "other"
    assert out["ticket_id"] == "unknown"
    assert isinstance(out["confidence"], float)
    assert 0.0 <= out["confidence"] <= 1.0

def test_confidence_is_float():
    out = classify_ticket({"id": "t2", "text": "refund asap"})
    assert isinstance(out["confidence"], float)

def test_urgency_critical_for_login_down():
    out = classify_ticket({"id": "t3", "text": "Cannot login, service is down"})
    assert out["urgency"] == "critical"


def test_urgency_critical_for_login_down_variations():
    # same message with different capitalization and punctuation
    out = classify_ticket({"id": "t4", "text": "cannot LOGIN service is down!"})
    assert out["urgency"] == "critical"


def test_output_schema_is_consistent():
    # use a variety of inputs to exercise defaulting logic
    samples = [
        {"id": "a", "text": "hello"},
        {"id": "b", "text": "fix bug"},
        {"id": "c", "text": ""},
        None,
    ]
    for ticket in samples:
        out = classify_ticket(ticket)
        assert set(out.keys()) == {"ticket_id", "category", "urgency", "confidence"}
        assert isinstance(out["ticket_id"], str)
        assert isinstance(out["category"], str)
        assert isinstance(out["urgency"], str)
        assert isinstance(out["confidence"], float)
        assert 0.0 <= out["confidence"] <= 1.0
