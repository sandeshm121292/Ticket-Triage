def normalize_ticket(ticket):
    """
    Normalize input ticket.
    Expected input:
      - dict with keys: id, text (text can be None)
    """
    # Be tolerant of None or non-dict input and provide safe defaults.
    if not isinstance(ticket, dict):
        return {"id": "unknown", "text": ""}

    ticket_id = ticket.get("id") or "unknown"
    text = ticket.get("text") or ""
    return {"id": ticket_id, "text": text.strip()}
