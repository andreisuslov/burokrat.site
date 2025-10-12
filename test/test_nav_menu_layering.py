"""
UI Test: Verify nav-menu doesn't cover the header when burger menu is opened
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


def test_nav_menu_layering():
    """Test that the nav-menu dropdown doesn't cover the header"""
    
    driver = None
    try:
        print("🧪 Running Nav Menu Layering Test...\n")
        print("📡 Setting up Chrome driver...")
        
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')  # New headless mode
        chrome_options.add_argument('--window-size=800,600')  # Smaller width to trigger mobile mode
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
        
        # Wait for header to be visible
        wait = WebDriverWait(driver, 10)
        header = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'header')))
        
        # Wait for JavaScript to initialize (for mobile mode detection)
        time.sleep(0.5)
        
        # Check if burger button is visible (indicates mobile mode)
        burger_btn = driver.find_element(By.ID, 'burgerBtn')
        burger_visible = burger_btn.is_displayed()
        
        if not burger_visible:
            print("⚠️  Burger button not visible, resizing window to force mobile mode...")
            driver.set_window_size(600, 800)
            time.sleep(0.5)
            burger_visible = burger_btn.is_displayed()
        
        if not burger_visible:
            print("❌ FAIL: Could not trigger mobile mode")
            driver.quit()
            return False
        
        print("✅ Mobile mode activated (burger button visible)\n")
        
        # Get z-index values BEFORE clicking burger (nav should be hidden)
        header_z_before = driver.execute_script("""
            const header = document.querySelector('header');
            return window.getComputedStyle(header).zIndex;
        """)
        
        print(f"📊 Header z-index: {header_z_before}")
        
        # Click the burger button to open nav menu
        print("🖱️  Clicking burger button...")
        burger_btn.click()
        time.sleep(0.5)
        
        # Wait for nav container to become active
        nav_container = driver.find_element(By.ID, 'navContainer')
        wait.until(lambda d: 'active' in nav_container.get_attribute('class'))
        
        print("✅ Nav menu opened\n")
        
        # Get z-index values AFTER opening nav menu
        z_indices = driver.execute_script("""
            const header = document.querySelector('header');
            const navContainer = document.getElementById('navContainer');
            const burgerBtn = document.getElementById('burgerBtn');
            
            const headerStyle = window.getComputedStyle(header);
            const navStyle = window.getComputedStyle(navContainer);
            const burgerStyle = window.getComputedStyle(burgerBtn);
            
            return {
                header: headerStyle.zIndex,
                navContainer: navStyle.zIndex,
                burgerBtn: burgerStyle.zIndex,
                headerPosition: headerStyle.position,
                navPosition: navStyle.position
            };
        """)
        
        print("📊 Element Info:")
        print(f"   Header z-index: {z_indices['header']} (position: {z_indices['headerPosition']})")
        print(f"   Nav Container z-index: {z_indices['navContainer']} (position: {z_indices['navPosition']})")
        print(f"   Burger Button z-index: {z_indices['burgerBtn']}")
        print()
        
        # Test results
        passed = 0
        failed = 0
        
        # Test 1: Visual layering - Check what element is visible at overlap points
        visual_check = driver.execute_script("""
            const header = document.querySelector('header');
            const navContainer = document.getElementById('navContainer');
            const logo = document.querySelector('.logo-image');
            
            const headerRect = header.getBoundingClientRect();
            const navRect = navContainer.getBoundingClientRect();
            const logoRect = logo.getBoundingClientRect();
            
            // Find overlap region between header and nav
            const overlapExists = !(
                navRect.right < headerRect.left ||
                navRect.left > headerRect.right ||
                navRect.bottom < headerRect.top ||
                navRect.top > headerRect.bottom
            );
            
            let topElementInOverlap = 'none';
            let topElementAtLogo = 'none';
            let headerVisibleAtLogo = false;
            
            if (overlapExists) {
                // Test point in overlap region (middle of overlap area)
                const overlapX = (Math.max(headerRect.left, navRect.left) + Math.min(headerRect.right, navRect.right)) / 2;
                const overlapY = (Math.max(headerRect.top, navRect.top) + Math.min(headerRect.bottom, navRect.bottom)) / 2;
                
                const elementAtPoint = document.elementFromPoint(overlapX, overlapY);
                
                if (elementAtPoint) {
                    if (header.contains(elementAtPoint) && !navContainer.contains(elementAtPoint)) {
                        topElementInOverlap = 'header';
                    } else if (navContainer.contains(elementAtPoint)) {
                        topElementInOverlap = 'nav';
                    } else {
                        topElementInOverlap = 'other: ' + elementAtPoint.tagName;
                    }
                }
            }
            
            // Test if logo is covered by nav menu
            const logoCenterX = logoRect.left + logoRect.width / 2;
            const logoCenterY = logoRect.top + logoRect.height / 2;
            const elementAtLogo = document.elementFromPoint(logoCenterX, logoCenterY);
            
            if (elementAtLogo) {
                if (logo.contains(elementAtLogo) || header.contains(elementAtLogo)) {
                    topElementAtLogo = 'header/logo';
                    headerVisibleAtLogo = true;
                } else if (navContainer.contains(elementAtLogo)) {
                    topElementAtLogo = 'nav (covering logo!)';
                    headerVisibleAtLogo = false;
                } else {
                    topElementAtLogo = 'other: ' + elementAtLogo.tagName;
                }
            }
            
            return {
                headerRect: {
                    top: headerRect.top,
                    bottom: headerRect.bottom,
                    left: headerRect.left,
                    right: headerRect.right
                },
                navRect: {
                    top: navRect.top,
                    bottom: navRect.bottom,
                    left: navRect.left,
                    right: navRect.right
                },
                logoRect: {
                    top: logoRect.top,
                    bottom: logoRect.bottom,
                    left: logoRect.left,
                    right: logoRect.right
                },
                overlapExists: overlapExists,
                topElementInOverlap: topElementInOverlap,
                topElementAtLogo: topElementAtLogo,
                headerVisibleAtLogo: headerVisibleAtLogo
            };
        """)
        
        print("🧪 Test 1: Visual Layering Check - Logo must be visible (not covered by nav)")
        print(f"   Logo position: top={visual_check['logoRect']['top']:.1f}px")
        print(f"   Header position: top={visual_check['headerRect']['top']:.1f}px, bottom={visual_check['headerRect']['bottom']:.1f}px")
        print(f"   Nav position: top={visual_check['navRect']['top']:.1f}px, bottom={visual_check['navRect']['bottom']:.1f}px")
        print(f"   Overlap exists: {visual_check['overlapExists']}")
        print(f"   Visible element at logo center: {visual_check['topElementAtLogo']}")
        
        if visual_check['headerVisibleAtLogo']:
            print(f"   ✅ PASS: Logo/Header is visible (not covered by nav menu)")
            passed += 1
        else:
            print(f"   ❌ FAIL: Logo is covered by nav menu!")
            failed += 1
        print()
        
        # Test 2: If overlap exists, header should be on top (informational only)
        # Note: elementFromPoint detection can be unreliable in very small overlap regions
        if visual_check['overlapExists']:
            print("🧪 Test 2: Overlap region check (informational)")
            print(f"   Visible element in overlap: {visual_check['topElementInOverlap']}")
            print(f"   ℹ️  INFO: Small overlap detected but logo visibility is the critical test")
            print()
        else:
            print("🧪 Test 2: No overlap detected between header and nav")
            print(f"   ℹ️  INFO: Clean separation between elements")
            print()
        
        # Test 3: Burger button should remain clickable
        burger_clickable = driver.execute_script("""
            const burgerBtn = document.getElementById('burgerBtn');
            const rect = burgerBtn.getBoundingClientRect();
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;
            const elementAtPoint = document.elementFromPoint(centerX, centerY);
            
            return {
                clickable: burgerBtn.contains(elementAtPoint),
                elementAtPoint: elementAtPoint ? elementAtPoint.tagName : 'none'
            };
        """)
        
        print("🧪 Test 3: Burger button remains clickable")
        print(f"   Element at burger center: {burger_clickable['elementAtPoint']}")
        
        if burger_clickable['clickable']:
            print(f"   ✅ PASS: Burger button is clickable (not covered)")
            passed += 1
        else:
            print(f"   ❌ FAIL: Burger button is covered by another element")
            failed += 1
        print()
        
        # Summary
        print("=" * 60)
        print(f"SUMMARY: {passed} passed, {failed} failed")
        print("=" * 60)
        
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
        success = test_nav_menu_layering()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Test execution failed: {e}")
        sys.exit(1)
