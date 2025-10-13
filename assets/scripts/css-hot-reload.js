// CSS Hot Reload - Instantly updates CSS without page refresh
(function() {
    const cssFiles = new Map();
    const CHECK_INTERVAL = 300; // Check every 300ms for changes
    
    // Find all CSS link elements
    function findCSSLinks() {
        document.querySelectorAll('link[rel="stylesheet"]').forEach(link => {
            const href = link.getAttribute('href');
            if (href && !href.startsWith('http') && !href.startsWith('//')) {
                cssFiles.set(href, {
                    link: link,
                    lastModified: null
                });
            }
        });
    }
    
    // Check if CSS file has been modified
    async function checkCSSFile(href, data) {
        try {
            const response = await fetch(href, {
                method: 'HEAD',
                cache: 'no-cache'
            });
            
            const lastModified = response.headers.get('Last-Modified') || 
                                 response.headers.get('ETag') || 
                                 Date.now().toString();
            
            if (data.lastModified && data.lastModified !== lastModified) {
                reloadCSS(href, data.link);
            }
            
            data.lastModified = lastModified;
        } catch (error) {
            // Silently fail - file might not be accessible
        }
    }
    
    // Reload CSS by updating the link href with cache-busting parameter
    function reloadCSS(href, linkElement) {
        const url = new URL(href, window.location.origin);
        url.searchParams.set('_reload', Date.now());
        
        // Create new link element
        const newLink = linkElement.cloneNode();
        newLink.href = url.toString();
        
        // Replace old link with new one
        newLink.onload = () => {
            linkElement.remove();
            console.log('🎨 CSS hot-reloaded:', href);
        };
        
        linkElement.parentNode.insertBefore(newLink, linkElement.nextSibling);
        
        // Update our reference
        cssFiles.get(href).link = newLink;
    }
    
    // Start monitoring CSS files
    function startMonitoring() {
        findCSSLinks();
        
        setInterval(() => {
            cssFiles.forEach((data, href) => {
                checkCSSFile(href, data);
            });
        }, CHECK_INTERVAL);
        
        console.log('🔥 CSS hot-reload enabled');
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', startMonitoring);
    } else {
        startMonitoring();
    }
})();
