from fasthtml.common import *
from src.config import get_agreement_data
import re


def _inline_email_nodes(text: str):
    """Return a list of strings/nodes where any email in text becomes a mailto link.
    Links use the 'contact-email' class to match normalized paragraph link styling.
    """
    if text is None:
        return []
    s = str(text)
    email_re = re.compile(r'([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})')
    parts = []
    last = 0
    for m in email_re.finditer(s):
        if m.start() > last:
            parts.append(s[last:m.start()])
        email = m.group(1)
        parts.append(A(email, href=f"mailto:{email}", cls='contact-email'))
        last = m.end()
    if last < len(s):
        parts.append(s[last:])
    return parts or [s]


def _render_clause(clause: dict):
    nodes = []
    text = clause.get('text')
    if text:
        nodes.append(P(*_inline_email_nodes(text)))

    items = clause.get('items', [])
    if items:
        nodes.append(Ul(*[Li(*_inline_email_nodes(item)) for item in items]))

    conclusion = clause.get('conclusion')
    if conclusion:
        nodes.append(P(*_inline_email_nodes(conclusion)))

    return Div(*nodes, cls='agreement-clause')


def _render_requisites(data: dict):
    if not data:
        return None

    req = data.get('requisites', {})
    pub_date = data.get('publication_date')

    lines = []
    if req.get('company_name'):
        lines.append(P(Strong(req.get('company_name'))))
    if req.get('inn'):
        lines.append(P(req.get('inn')))
    if req.get('kpp'):
        lines.append(P(req.get('kpp')))
    if req.get('ogrn'):
        lines.append(P(req.get('ogrn')))
    if req.get('address'):
        lines.append(P(req.get('address')))
    if req.get('email'):
        # May contain a label and email; convert only the email part to a link
        lines.append(P(*_inline_email_nodes(req.get('email'))))

    if pub_date:
        lines.append(Br())  # Add line break before publication date
        lines.append(P(pub_date, cls='agreement-publication-date'))

    if not lines:
        return None

    return Div(
        H2('Реквизиты'),
        *lines,
        cls='agreement-requisites'
    )


def render():
    """Render main content for the Agreement page (Пользовательское соглашение)."""
    data = get_agreement_data()

    return (
        Section(
            Div(
                H1(data.get('title', 'Пользовательское соглашение')),
                P(data.get('preamble', '')),
                cls='page-intro agreement-intro'
            )
        ),
        Section(
            Div(
                *[
                    Div(
                        H2(section.get('heading', '')),
                        *[_render_clause(cl) for cl in section.get('clauses', [])],
                        cls='agreement-section'
                    )
                    for section in data.get('sections', [])
                ],
            ),
            cls='agreement-content'
        ),
        Section(
            _render_requisites(data.get('footer', {})),
            cls='agreement-footer'
        ),
    )
