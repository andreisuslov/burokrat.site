"""
UI Test: Verify that multiple form submissions don't create duplicate error messages
Tests that submitting an empty form multiple times only shows one error per field
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


def test_multiple_submissions():
    """Test that multiple submissions don't create duplicate errors"""
    
    driver = None
    try:
        print("🧪 Running Multiple Submission Test...\n")
        print("📡 Setting up Chrome driver...")
        
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--window-size=1280,720')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        
        # Initialize WebDriver
        try:
            driver_path = ChromeDriverManager().install()
            import os
            import glob
            driver_dir = os.path.dirname(driver_path)
            actual_driver = glob.glob(os.path.join(driver_dir, '**/chromedriver'), recursive=True)
            if actual_driver:
                driver_path = actual_driver[0]
            service = Service(driver_path)
            driver = webdriver.Chrome(service=service, options=chrome_options)
        except:
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
        
        # Find submit button
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        
        # Test results
        passed = 0
        failed = 0
        num_submissions = 3
        
        print(f"🔄 Submitting empty form {num_submissions} times...\n")
        
        for i in range(num_submissions):
            print(f"Submission #{i + 1}:")
            
            # Click submit button
            submit_button.click()
            
            # Wait for errors to appear
            time.sleep(0.6)  # Wait for animations
            
            # Count all error messages
            all_errors = driver.find_elements(By.CSS_SELECTOR, '.error-message')
            print(f"  Total error messages on page: {len(all_errors)}")
            
            # Count errors per field
            form_groups = driver.find_elements(By.CSS_SELECTOR, '.form-group')
            field_errors = {}
            
            for group in form_groups:
                field = group.find_element(By.CSS_SELECTOR, 'input, textarea')
                field_name = field.get_attribute('name')
                errors_in_group = group.find_elements(By.CSS_SELECTOR, '.error-message')
                error_count = len(errors_in_group)
                
                if error_count > 0:
                    field_errors[field_name] = error_count
                    
                    if error_count == 1:
                        print(f"  ✅ {field_name}: 1 error (correct)")
                        passed += 1
                    else:
                        print(f"  ❌ {field_name}: {error_count} errors (should be 1)")
                        failed += 1
            
            print()
        
        # Final summary
        print("=" * 50)
        print(f"FINAL RESULTS AFTER {num_submissions} SUBMISSIONS:")
        print(f"SUMMARY: {passed} passed, {failed} failed")
        
        # Get final state
        final_errors = driver.find_elements(By.CSS_SELECTOR, '.error-message')
        expected_errors = 4  # name, email, comment, consent
        
        print(f"\nFinal error count: {len(final_errors)}")
        print(f"Expected error count: {expected_errors}")
        
        if len(final_errors) == expected_errors:
            print("✅ Correct number of errors displayed")
        else:
            print(f"❌ Wrong number of errors (expected {expected_errors}, got {len(final_errors)})")
            failed += 1
        
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
        success = test_multiple_submissions()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Test execution failed: {e}")
        sys.exit(1)
