// Header navigation and responsive burger menu functionality
document.addEventListener('DOMContentLoaded', function() {
    const burgerBtn = document.getElementById('burgerBtn');
    const navContainer = document.getElementById('navContainer');
    const headerContent = document.querySelector('.header-content');
    const header = document.querySelector('header');
    
    if (!burgerBtn || !navContainer || !headerContent || !header) return;
    
    // Function to update dropdown position
    function updateDropdownPosition() {
        if (headerContent.classList.contains('mobile-mode')) {
            const headerHeight = header.offsetHeight;
            // Subtract 3px to overlap with header's bottom border
            navContainer.style.top = (headerHeight - 3) + 'px';
        }
    }
    
    // Function to check if nav menu should be burger
    function checkNavOverflow() {
        // Reset to horizontal layout temporarily to measure
        headerContent.classList.remove('mobile-mode');
        burgerBtn.classList.remove('active');
        navContainer.classList.remove('active');
        
        // Get dimensions
        const headerWidth = headerContent.offsetWidth;
        const headerPadding = parseInt(getComputedStyle(headerContent).paddingLeft) + 
                            parseInt(getComputedStyle(headerContent).paddingRight);
        const availableWidth = headerWidth - headerPadding;
        
        // Calculate total width needed (logo + gap + nav + buffer)
        const logo = headerContent.querySelector('h1');
        const logoWidth = logo ? logo.offsetWidth : 0;
        const navWidth = navContainer.offsetWidth;
        const gap = 140; // gap between logo and nav
        const buffer = 20; // safety buffer
        
        const totalNeeded = logoWidth + gap + navWidth + buffer;
        
        // Switch to mobile mode if content would overflow
        if (totalNeeded > availableWidth) {
            headerContent.classList.add('mobile-mode');
            updateDropdownPosition();
        }
    }
    
    // Burger button click handler
    burgerBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        burgerBtn.classList.toggle('active');
        navContainer.classList.toggle('active');
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!burgerBtn.contains(event.target) && !navContainer.contains(event.target)) {
            burgerBtn.classList.remove('active');
            navContainer.classList.remove('active');
        }
    });
    
    // Close menu when clicking a nav link
    const navLinks = navContainer.querySelectorAll('a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            burgerBtn.classList.remove('active');
            navContainer.classList.remove('active');
        });
    });
    
    // Check on load and resize (instant, no debounce)
    checkNavOverflow();
    window.addEventListener('resize', function() {
        checkNavOverflow();
        updateDropdownPosition();
    });
});
