#!/usr/bin/env python3
"""
clipboard_extract.py

A human-readable-regex (humre) rewrite of the original pyperclip script.
Provides:
 - a tiny `humre.compile` helper that compiles verbose/indented regex strings
 - named groups for phone/email parsing
 - clearer formatting and safer handling of optional groups
"""

import re
import pyperclip
from typing import Pattern


# -------------------------
# tiny "humre" helper
# -------------------------
def _dedent_and_strip(commented: str) -> str:
    """
    Remove common indentation and strip trailing spaces.
    Keep it compatible with re.VERBOSE style comments.
    """
    # remove leading/trailing blank lines
    lines = commented.strip("\n").splitlines()
    # determine minimal indentation of non-empty lines
    indents = [len(line) - len(line.lstrip()) for line in lines if line.strip()]
    min_indent = min(indents) if indents else 0
    cleaned = "\n".join(line[min_indent:] for line in lines)
    return cleaned


def humre_compile(spec: str, flags: int = re.VERBOSE) -> Pattern:
    """
    Compile a human-readable regex spec (multi-line, commented)
    into a compiled regex using re.VERBOSE by default.
    """
    pattern = _dedent_and_strip(spec)
    return re.compile(pattern, flags)


# -------------------------
# Patterns (human-readable)
# -------------------------
phone_spec = r"""
(
  # Full match (we'll use named groups inside too)
  (?P<full>
    # optional area code: 123 or (123)
    (?P<area>\d{3}|\(\d{3}\))?
    (?:\s|-|\.)?          # optional separator
    (?P<prefix>\d{3})     # first 3 digits
    (?:\s|-|\.)           # required separator between prefix and line
    (?P<line>\d{4})       # last 4 digits
    (?:                   # optional extension group
      \s*(?:ext|x|ext\.)\s*(?P<ext>\d{2,5})
    )?
  )
)
"""

email_spec = r"""
(
  # email username
  (?P<user>[a-zA-Z0-9._%+\-]+)
  @
  # domain (support subdomains)
  (?P<domain>[a-zA-Z0-9.\-]+\.[A-Za-z]{2,})
)
"""

phone_re = humre_compile(phone_spec)
email_re = humre_compile(email_spec, flags=re.IGNORECASE | re.VERBOSE)


# -------------------------
# Utilities
# -------------------------
def format_phone_from_match(m: re.Match) -> str:
    """
    Build normalized phone string from regex match.
    Output example: 123-456-7890 x123  (extension optional)
    If area code had parentheses, remove them for normalization.
    """
    if not m:
        return ""
    area = m.group("area") or ""
    prefix = m.group("prefix") or ""
    line = m.group("line") or ""
    ext = m.group("ext")

    # normalize area: remove parentheses
    area = area.replace("(", "").replace(")", "")
    pieces = []
    if area:
        pieces.append(area)
    # If no explicit area present, don't force an empty prefix
    pieces.extend([prefix, line])
    phone_num = "-".join(p for p in pieces if p)
    if ext:
        phone_num += f" x{ext}"
    return phone_num


# -------------------------
# Main extraction logic
# -------------------------
def extract_contacts_from_text(text: str) -> list:
    """
    Extract phone numbers and emails from a large text blob.
    Returns a list of normalized strings.
    """
    matches = []

    # Find phone matches (use finditer for Match objects)
    for m in phone_re.finditer(text):
        # format and append only if we actually have prefix+line
        if m.group("prefix") and m.group("line"):
            matches.append(format_phone_from_match(m))

    # Find email matches
    for m in email_re.finditer(text):
        email = m.group(1)  # full match (preserves case per original)
        matches.append(email)

    # Remove duplicates while preserving order
    seen = set()
    unique = []
    for item in matches:
        if item not in seen:
            seen.add(item)
            unique.append(item)

    return unique


def main():
    text = str(pyperclip.paste() or "")
    results = extract_contacts_from_text(text)

    if results:
        output = "\n".join(results)
        pyperclip.copy(output)
        print("Copied to clipboard:")
        print(output)
    else:
        print("No phone numbers or email addresses found.")


if __name__ == "__main__":
    main()
