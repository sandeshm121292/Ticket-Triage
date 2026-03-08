import json

def summarize_ticket(ticket: dict) -> dict:
    """
    Input: {"id": str, "text": str}
    Output: {"ticket_id": str, "summary": str, "keywords": list[str]}
    """
  
    if not isinstance(ticket, dict):
        ticket = {}

    ticket_id = str(ticket.get("id", "unknown"))
    text = (ticket.get("text") or "").strip()

    words = [w.strip(".,!? ").lower() for w in text.split() if w]
    keywords = sorted(set(words))[:5]

    summary = text[:80]
    return {"ticket_id": ticket_id, "summary": summary, "keywords": keywords}
