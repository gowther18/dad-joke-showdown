"""Dad Joke Showdown.

Writes one dad joke to /output/entry.txt. The joke is a single sentence:
a dad buys memory-foam shoes, and the foam's "memory" turns literal --
he can no longer forget a single step he has taken. The setup is an
everyday purchase, the pun is the word "memory" doing double duty
(the foam remembers, so the wearer cannot forget), and the groan
lands on the last words, where "step" means both a footstep and a
misstep. Clean, self-contained, no profanity, one sentence.
"""

from pathlib import Path

TEXT = (
    "I bought memory-foam shoes, and now I can't forget "
    "a single step I've taken."
)


# The competition accepts a single text of 1 to 200 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
