# UI Tests

This folder contains UI tests for the Burokrat.site application.

## Setup

Install test dependencies:
```bash
pip3 install -r test/requirements-test.txt
```

The test uses Selenium with automatic ChromeDriver management (no manual driver installation needed).

## Running Tests

### Error Width Test

Tests that error messages match the width of form inputs (specifically the email input).

**Prerequisites:** Make sure the dev server is running on `http://localhost:8080`

```bash
# Start the dev server in one terminal
./run.sh

# Run the test in another terminal
python3 test/test_error_widths.py
```

The test will:
- Automatically download and setup ChromeDriver (first run only)
- Run Chrome in headless mode
- Navigate to the local site
- Trigger form validation
- Measure and compare error message widths
- Report results in the terminal

### Nav Menu Layering Test

Tests that the navigation menu dropdown doesn't cover the header when opened in mobile mode.

**Prerequisites:** Make sure the dev server is running on `http://localhost:8080`

```bash
# Start the dev server in one terminal
./run.sh

# Run the test in another terminal
python3 test/test_nav_menu_layering.py
```

The test will:
- Run Chrome in headless mode at mobile width (800x600)
- Verify burger menu activates in mobile mode
- Click the burger button to open nav menu
- Check z-index values: header > nav-menu
- Verify burger button is clickable (highest z-index)
- Confirm nav menu doesn't overlap with logo
- Report results in the terminal

## Test Structure

- `test_error_widths.py` - UI test for error message widths
- `test_multiple_submissions.py` - UI test for duplicate error prevention
- `test_nav_menu_layering.py` - UI test for nav menu z-index layering
- `requirements-test.txt` - Test dependencies (Selenium + WebDriver Manager)

## All Tests

Run all tests:
```bash
python3 test/test_error_widths.py && python3 test/test_multiple_submissions.py && python3 test/test_nav_menu_layering.py
```
