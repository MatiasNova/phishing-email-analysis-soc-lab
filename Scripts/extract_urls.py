
from pathlib import Path
from email import policy
from email.parser import BytesParser
from html.parser import HTMLParser
import re

PROJECT = Path(
    r"C:\cyber projects\Phishing-Email-Analysis"
)

SAMPLES = PROJECT / "Samples" / "Working"

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ("href", "src") and value:
                self.links.append(value)

def defang(url):
    return (
        url.replace("https://", "hxxps://")
           .replace("http://", "hxxp://")
           .replace(".", "[.]")
    )

for path in SAMPLES.rglob("*.eml"):

    print(f"\nEMAIL: {path.name}")

    with path.open("rb") as file:
        message = BytesParser(
            policy=policy.default
        ).parse(file)

    for part in message.walk():

        if part.get_content_maintype() == "multipart":
            continue

        if part.get_content_disposition() == "attachment":
            continue

        if part.get_content_type() not in (
            "text/plain", "text/html"
        ):
            continue

        content = part.get_content()

        if not isinstance(content, str):
            continue

        urls = re.findall(
            r'https?://[^\s<>"\']+',
            content
        )

        if part.get_content_type() == "text/html":
            parser = LinkExtractor()
            parser.feed(content)
            urls.extend(parser.links)

        for url in dict.fromkeys(urls):
            print(defang(url))
