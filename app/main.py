import argparse
from app.services.classifier import classify_ticket

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--text", required=True)
    args = p.parse_args()
    print(classify_ticket({"id": "cli", "text": args.text}))

if __name__ == "__main__":
    main()
