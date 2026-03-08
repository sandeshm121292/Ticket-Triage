from app.utils.parser import normalize_ticket

CATEGORIES = ["billing", "login", "bug", "feature_request", "other"]
URG = ["low", "medium", "high", "critical"]

def _rule_category(text: str) -> str:
    t = text.lower()
    if "charge" in t or "refund" in t or "invoice" in t:
        return "billing"
    if "password" in t or "login" in t or "sign in" in t:
        return "login"
    if "crash" in t or "error" in t or "stacktrace" in t:
        return "bug"
    if "feature" in t or "would be nice" in t:
        return "feature_request"
    return "other"

def _rule_urgency(text: str) -> str:
    t = text.lower()
    if "asap" in t or "urgent" in t or "immediately" in t:
        return "high"
    if "down" in t or "cannot" in t and "login" in t:
        return "critical"
    return "medium"

def classify_ticket(ticket):
    """
    Returns dict:
      { "ticket_id": ..., "category": ..., "urgency": ..., "confidence": float }
    """
    normalized = normalize_ticket(ticket)

    # normalized is always a dict with keys `id` and `text` (see parser.normalize_ticket)
    text = normalized.get("text", "")
    cat = _rule_category(text)
    urg = _rule_urgency(text)

    # Return a numeric confidence in [0.0, 1.0]. Use a simple heuristic.
    raw_conf = 0.9 if cat != "other" else 0.0
    confidence = float(raw_conf)
    # enforce bounds just in case rules change later
    confidence = max(0.0, min(1.0, confidence))

    result = {
        "ticket_id": str(normalized.get("id", "unknown")),
        "category": str(cat),
        "urgency": str(urg),
        "confidence": confidence,
    }

    # sanity check: return types should match expected schema
    assert isinstance(result["ticket_id"], str)
    assert isinstance(result["category"], str)
    assert isinstance(result["urgency"], str)
    assert isinstance(result["confidence"], float)
    assert 0.0 <= result["confidence"] <= 1.0

    return result
