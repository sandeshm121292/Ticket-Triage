from app.services.summarizer import summarize_ticket

def test_none_ticket_safe_defaults():
    out = summarize_ticket(None)
    assert out["ticket_id"] == "unknown"
    assert out["summary"] == ""
    assert out["keywords"] == []


def test_summary_truncates_at_80_chars():
    text = "x" * 200
    out = summarize_ticket({"id": "t11", "text": text})
    assert len(out["summary"]) == 80
    assert out["summary"] == "x" * 80

def test_keywords_is_list_and_summary_length():
    out = summarize_ticket({"id": "t9", "text": "Refund requested ASAP!! Charged twice."})
    assert isinstance(out["keywords"], list)
    assert len(out["summary"]) <= 80

def test_missing_text_safe():
    out = summarize_ticket({"id": "t10"})
    assert out["ticket_id"] == "t10"
    assert out["summary"] == ""
    assert out["keywords"] == []