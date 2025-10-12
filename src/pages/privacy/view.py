from fasthtml.common import *
from src.config import get_privacy_data
import re


def _render_privacy_paragraphs(paragraphs):
    """Render paragraphs with better semantics:
    - Lines like "**Subheading**" become H3.
    - Lines starting with "- " become bullet lists (UL/LI).
    - A line that is just an email (optionally wrapped in **) is inlined to the previous paragraph as a mailto link.
    """
    if not paragraphs:
        return []

    nodes = []
    buffer_text = None  # holds the last non-email paragraph text until flushed
    ul_items = []       # holds accumulated bullet list items across blocks
    email_re = re.compile(r'^\*{0,2}([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})\*{0,2}$')

    def flush_buffer():
        nonlocal buffer_text
        if buffer_text is not None:
            nodes.append(P(buffer_text))
            buffer_text = None

    def flush_ul():
        nonlocal ul_items
        if ul_items:
            nodes.append(Ul(*[Li(item) for item in ul_items]))
            ul_items = []

    def parse_heading_line(line: str):
        m = re.fullmatch(r'\*\*(.+)\*\*', line)
        if m and not email_re.fullmatch(m.group(1) or ''):
            return H3(m.group(1))
        return None

    def parse_block(block):
        nonlocal buffer_text
        s = str(block).strip()

        # Email-only block (possibly wrapped in **)
        m = email_re.fullmatch(s)
        if m:
            email = m.group(1)
            if buffer_text is not None:
                nodes.append(P(buffer_text, ' ', A(email, href=f"mailto:{email}", cls='contact-email')))
                buffer_text = None
            else:
                nodes.append(P(A(email, href=f"mailto:{email}", cls='contact-email')))
            return

        # Split block into lines and parse
        lines = [ln.rstrip() for ln in s.splitlines()]

        for raw in lines:
            line = raw.strip()
            if not line:
                continue

            # Subheading line like **1.2. Title**
            h = parse_heading_line(line)
            if h:
                flush_buffer()
                flush_ul()
                nodes.append(h)
                continue

            # Bullet item line starting with "- "
            if line.startswith('- '):
                flush_buffer()
                ul_items.append(line[2:].strip())
                continue

            # Regular text line -> accumulate into paragraph buffer
            flush_ul()
            if buffer_text:
                buffer_text += (' ' if not buffer_text.endswith((' ', '\n')) else '') + line
            else:
                buffer_text = line

        # do not flush UL here; allow accumulation across blocks

    for p in paragraphs:
        parse_block(p)

    flush_ul()
    flush_buffer()

    return nodes


def render():
    """Render main content for the Privacy page."""
    data = get_privacy_data()

    return (
        Section(
            Div(
                H1(data['title']),
                P(data.get('intro', '')),
                cls='page-intro privacy-intro'
            )
        ),
        Section(
            Div(
                *[Div(
                    H2(section.get('heading', '')),
                    *(_render_privacy_paragraphs(section.get('paragraphs', []))),
                    cls='privacy-section'
                ) for section in data.get('sections', [])],
            ),
            cls='privacy-content'
        ),
    )
