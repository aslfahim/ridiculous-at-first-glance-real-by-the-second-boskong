"""Ridiculous at First Glance, Real by the Second — @boskong entry.

Concept: AI APOLOGY SERVICE. Companies pay for a service that writes
warm, human-sounding apologies from their chatbots to furious customers,
because a bot that says sorry properly keeps the customer.

Writes exactly one sentence (<=200 chars) to /output/entry.txt.
Python standard library only.
"""

import os

SENTENCE = (
    "Our AI writes warm, human-sounding apologies for companies whose "
    "chatbots enraged their customers \u2014 brands pay per sorry, because "
    "a bot that apologises properly keeps the customer about to cancel."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
