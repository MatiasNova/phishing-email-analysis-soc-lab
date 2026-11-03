
from pathlib import Path
from email import policy
from email.parser import BytesParser

PROJECT = Path(
    r"C:\cyber projects\Phishing-Email-Analysis"
)

SAMPLES = PROJECT / "Samples" / "Working"
OUTPUT = PROJECT / "Headers"

OUTPUT.mkdir(parents=True, exist_ok=True)

email_files = list(SAMPLES.rglob("*.eml"))

if not email_files:
    print("No EML files found.")
    raise SystemExit

for index, email_path in enumerate(email_files, start=1):

    print(f"\nAnalyzing: {email_path.name}")

    with email_path.open("rb") as file:
        message = BytesParser(
            policy=policy.default
        ).parse(file, headersonly=True)

    headers = [
        "From",
        "To",
        "Subject",
        "Date",
        "Reply-To",
        "Return-Path",
        "Message-ID",
        "Received",
        "Authentication-Results",
        "Received-SPF",
        "DKIM-Signature"
    ]

    report = []

    for header in headers:

        values = message.get_all(header, [])

        if not values:
            report.append(f"{header}: Not present")

        for value in values:
            report.append(f"{header}: {value}")

    output_file = OUTPUT / f"email_{index}_headers.txt"

    output_file.write_text(
        "\n".join(report),
        encoding="utf-8"
    )

    print(f"Saved: {output_file.name}")

print("\nHeader extraction completed.")
