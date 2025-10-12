"""
UI Test: Verify error message widths match form input widths
Uses Selenium for browser automation and testing
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import sys
import time


def test_error_message_widths():
    """Test that all error messages match the width of the email input"""
    
    driver = None
    try:
        print("🧪 Running Error Width Tests...\n")
        print("📡 Setting up Chrome driver...")
        
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')  # New headless mode
        chrome_options.add_argument('--window-size=1280,720')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        
        # Initialize WebDriver with automatic driver management
        try:
            # Try with webdriver-manager first
            driver_path = ChromeDriverManager().install()
            # Fix for webdriver-manager bug: find actual chromedriver binary
            import os
            import glob
            driver_dir = os.path.dirname(driver_path)
            actual_driver = glob.glob(os.path.join(driver_dir, '**/chromedriver'), recursive=True)
            if actual_driver:
                driver_path = actual_driver[0]
            service = Service(driver_path)
            driver = webdriver.Chrome(service=service, options=chrome_options)
        except:
            # Fallback: try system chromedriver
            driver = webdriver.Chrome(options=chrome_options)
        
        driver.set_page_load_timeout(10)
        
        print("✅ Driver initialized\n")
        print("📡 Connecting to http://localhost:8080...")
        
        # Navigate to the local site
        driver.get('http://localhost:8080')
        
        print("✅ Page loaded successfully\n")
        
        # Wait for form to be visible
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.contact-form')))
        
        # Get the email input width as reference
        email_input = driver.find_element(By.ID, 'contact-email')
        email_width = email_input.size['width']
        print(f"📏 Reference width (email input): {email_width}px\n")
        
        # Trigger form validation by trying to submit without filling fields
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()
        
        # Wait for error messages to appear
        time.sleep(0.5)
        
        # Get all error messages
        error_messages = driver.find_elements(By.CSS_SELECTOR, '.error-message')
        
        if not error_messages:
            print("❌ FAIL: No error messages were generated!")
            driver.quit()
            return False
        
        print(f"✅ Generated {len(error_messages)} error messages\n")
        
        # Test results tracking
        passed = 0
        failed = 0
        tolerance = 2  # Allow 2px difference for rounding
        
        # Check each error message width
        for error_msg in error_messages:
            # Get parent form-group to identify the field
            parent_data = driver.execute_script("""
                const element = arguments[0];
                const formGroup = element.closest('.form-group');
                const field = formGroup.querySelector('input, textarea');
                return {
                    name: field?.name || 'unknown',
                    type: field?.type || 'unknown'
                };
            """, error_msg)
            
            error_width = error_msg.size['width']
            diff = abs(error_width - email_width)
            
            field_name = parent_data['name']
            field_type = parent_data['type']
            
            if diff <= tolerance:
                print(f"✅ PASS: {field_name} ({field_type})")
                print(f"   Width: {error_width}px (diff: {diff}px)")
                passed += 1
            else:
                print(f"❌ FAIL: {field_name} ({field_type})")
                print(f"   Width: {error_width}px (expected: {email_width}px, diff: {diff}px)")
                failed += 1
            print()
        
        # Summary
        print("=" * 50)
        print(f"SUMMARY: {passed} passed, {failed} failed")
        print("=" * 50)
        
        # Clean up
        driver.quit()
        
        return failed == 0
        
    except Exception as e:
        print(f"\n❌ Error during test: {e}")
        import traceback
        traceback.print_exc()
        if driver:
            driver.quit()
        return False


if __name__ == '__main__':
    try:
        success = test_error_message_widths()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Test execution failed: {e}")
        sys.exit(1)
