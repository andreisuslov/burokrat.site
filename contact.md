# Contact Section Implementation Tasks

- [x] Create `data/contact.yaml` containing Russian text for:
  - Title: "Обратная связь"
  - Intro text
  - Field labels/placeholders for name, email, comment
  - Consent text with link to privacy at `/privacy`
  - Submit button label
  - Success messages
- [x] Add contact data loaders to `src/config/data_loader.py` and export in `src/config/__init__.py`.
- [x] Render contact form as a section on the home page:
  - Add section with id `contact-form` in `src/pages/home/view.py`.
  - Use YAML-driven labels/placeholders; submit via HTMX to `/contact/submit`.
  - Fields: name, email, comment; required consent checkbox with link to `/privacy`.
- [x] Update `src/routes/contact.py`:
  - Remove old modal GET route.
  - Implement `POST /contact/submit` that returns YAML-driven success snippet.
- [x] Add alias route `GET /privacy` in `src/routes/privacy.py` to the same privacy view.
- [x] Update `data/about.yaml` CTA button "Связаться с нами" link to `/#contact-form`.
- [ ] Manual test flow: navigate to `/#contact-form`, submit valid form, see success message; click privacy link to `/privacy`.
