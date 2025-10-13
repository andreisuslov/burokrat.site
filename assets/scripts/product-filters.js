/**
 * Product Filters - Handles filtering, searching, and sorting of products
 */

(function() {
    'use strict';

    // State management
    const state = {
        selectedCategories: new Set(['all']),
        priceMin: 0,
        priceMax: 100,
        inStockOnly: false,
        searchQuery: '',
        sortBy: 'featured'
    };

    // DOM elements
    let productsGrid;
    let categoryCheckboxes;
    let priceMinSlider;
    let priceMaxSlider;
    let priceMinValue;
    let priceMaxValue;
    let sliderRange;
    let stockCheckbox;
    let clearFiltersBtn;
    let searchInput;
    let sortSelect;
    let resultsCount;
    let allProducts = [];

    // Initialize when DOM is ready
    function init() {
        // Get DOM elements
        productsGrid = document.getElementById('products-grid');
        categoryCheckboxes = document.querySelectorAll('.category-checkbox');
        priceMinSlider = document.getElementById('price-min');
        priceMaxSlider = document.getElementById('price-max');
        priceMinValue = document.getElementById('price-min-value');
        priceMaxValue = document.getElementById('price-max-value');
        sliderRange = document.getElementById('slider-range');
        stockCheckbox = document.querySelector('.stock-checkbox');
        clearFiltersBtn = document.querySelector('.btn-clear-filters');
        searchInput = document.getElementById('product-search');
        sortSelect = document.getElementById('product-sort');
        resultsCount = document.querySelector('.results-count');

        if (!productsGrid) return;

        // Store all products
        allProducts = Array.from(productsGrid.querySelectorAll('.product-card'));

        // Calculate actual price range from products
        calculatePriceRange();

        // Set up event listeners
        setupEventListeners();

        // Initial filter
        applyFilters();
    }

    // Calculate min/max prices from actual products
    function calculatePriceRange() {
        let minPrice = Infinity;
        let maxPrice = -Infinity;

        allProducts.forEach(card => {
            const priceText = card.querySelector('.product-price').textContent;
            const price = parseFloat(priceText.replace('$', ''));
            if (price < minPrice) minPrice = price;
            if (price > maxPrice) maxPrice = price;
        });

        // Round to nice numbers
        minPrice = Math.floor(minPrice);
        maxPrice = Math.ceil(maxPrice);

        // Update sliders
        if (priceMinSlider && priceMaxSlider) {
            priceMinSlider.min = minPrice;
            priceMinSlider.max = maxPrice;
            priceMinSlider.value = minPrice;
            
            priceMaxSlider.min = minPrice;
            priceMaxSlider.max = maxPrice;
            priceMaxSlider.value = maxPrice;

            state.priceMin = minPrice;
            state.priceMax = maxPrice;

            updatePriceDisplay();
        }
    }

    // Set up all event listeners
    function setupEventListeners() {
        // Category checkboxes
        categoryCheckboxes.forEach(checkbox => {
            checkbox.addEventListener('change', handleCategoryChange);
        });

        // Price sliders
        if (priceMinSlider) {
            priceMinSlider.addEventListener('input', handlePriceMinChange);
        }
        if (priceMaxSlider) {
            priceMaxSlider.addEventListener('input', handlePriceMaxChange);
        }

        // Stock checkbox
        if (stockCheckbox) {
            stockCheckbox.addEventListener('change', handleStockChange);
        }

        // Clear filters button
        if (clearFiltersBtn) {
            clearFiltersBtn.addEventListener('click', clearAllFilters);
        }

        // Search input
        if (searchInput) {
            searchInput.addEventListener('input', debounce(handleSearchChange, 300));
        }

        // Sort select
        if (sortSelect) {
            sortSelect.addEventListener('change', handleSortChange);
        }
    }

    // Handle category checkbox changes
    function handleCategoryChange(e) {
        const checkbox = e.target;
        const category = checkbox.value;

        if (category === 'all') {
            // If "All" is checked, uncheck others and select only "all"
            if (checkbox.checked) {
                state.selectedCategories.clear();
                state.selectedCategories.add('all');
                categoryCheckboxes.forEach(cb => {
                    if (cb.value !== 'all') {
                        cb.checked = false;
                    }
                });
            }
        } else {
            // If a specific category is checked, uncheck "all"
            const allCheckbox = Array.from(categoryCheckboxes).find(cb => cb.value === 'all');
            if (allCheckbox) {
                allCheckbox.checked = false;
            }
            state.selectedCategories.delete('all');

            // Add or remove the category
            if (checkbox.checked) {
                state.selectedCategories.add(category);
            } else {
                state.selectedCategories.delete(category);
            }

            // If no categories selected, select "all"
            if (state.selectedCategories.size === 0) {
                state.selectedCategories.add('all');
                if (allCheckbox) {
                    allCheckbox.checked = true;
                }
            }
        }

        applyFilters();
    }

    // Handle price min slider change
    function handlePriceMinChange(e) {
        const value = parseFloat(e.target.value);
        
        // Ensure min doesn't exceed max
        if (value > state.priceMax) {
            e.target.value = state.priceMax;
            state.priceMin = state.priceMax;
        } else {
            state.priceMin = value;
        }

        updatePriceDisplay();
        applyFilters();
    }

    // Handle price max slider change
    function handlePriceMaxChange(e) {
        const value = parseFloat(e.target.value);
        
        // Ensure max doesn't go below min
        if (value < state.priceMin) {
            e.target.value = state.priceMin;
            state.priceMax = state.priceMin;
        } else {
            state.priceMax = value;
        }

        updatePriceDisplay();
        applyFilters();
    }

    // Update price display values
    function updatePriceDisplay() {
        if (priceMinValue) {
            priceMinValue.textContent = `$${state.priceMin.toFixed(0)}`;
        }
        if (priceMaxValue) {
            priceMaxValue.textContent = `$${state.priceMax.toFixed(0)}`;
        }
        
        // Update slider range visual
        if (sliderRange && priceMinSlider && priceMaxSlider) {
            const min = parseFloat(priceMinSlider.min);
            const max = parseFloat(priceMinSlider.max);
            const range = max - min;
            
            const leftPercent = ((state.priceMin - min) / range) * 100;
            const rightPercent = ((state.priceMax - min) / range) * 100;
            
            sliderRange.style.left = `${leftPercent}%`;
            sliderRange.style.width = `${rightPercent - leftPercent}%`;
        }
    }

    // Handle stock checkbox change
    function handleStockChange(e) {
        state.inStockOnly = e.target.checked;
        applyFilters();
    }

    // Handle search input change
    function handleSearchChange(e) {
        state.searchQuery = e.target.value.toLowerCase().trim();
        applyFilters();
    }

    // Handle sort select change
    function handleSortChange(e) {
        state.sortBy = e.target.value;
        applyFilters();
    }

    // Clear all filters
    function clearAllFilters() {
        // Reset state
        state.selectedCategories.clear();
        state.selectedCategories.add('all');
        state.inStockOnly = false;
        state.searchQuery = '';
        state.sortBy = 'featured';

        // Reset UI
        categoryCheckboxes.forEach(checkbox => {
            checkbox.checked = checkbox.value === 'all';
        });

        if (stockCheckbox) {
            stockCheckbox.checked = false;
        }

        if (searchInput) {
            searchInput.value = '';
        }

        if (sortSelect) {
            sortSelect.value = 'featured';
        }

        // Reset price sliders to full range
        calculatePriceRange();

        applyFilters();
    }

    // Apply all filters
    function applyFilters() {
        let visibleProducts = allProducts.filter(card => {
            // Category filter
            const productCategory = card.dataset.category;
            const categoryMatch = state.selectedCategories.has('all') || 
                                 state.selectedCategories.has(productCategory);
            
            if (!categoryMatch) return false;

            // Price filter
            const priceText = card.querySelector('.product-price').textContent;
            const price = parseFloat(priceText.replace('$', ''));
            if (price < state.priceMin || price > state.priceMax) return false;

            // Stock filter (currently all products are in stock, but keeping for future)
            if (state.inStockOnly) {
                const inStock = card.dataset.inStock !== 'false';
                if (!inStock) return false;
            }

            // Search filter
            if (state.searchQuery) {
                const productName = card.querySelector('.product-name').textContent.toLowerCase();
                if (!productName.includes(state.searchQuery)) return false;
            }

            return true;
        });

        // Sort products
        visibleProducts = sortProducts(visibleProducts);

        // Update display
        updateProductsDisplay(visibleProducts);
        updateResultsCount(visibleProducts.length);
    }

    // Sort products based on selected sort option
    function sortProducts(products) {
        const sorted = [...products];

        switch (state.sortBy) {
            case 'price-asc':
                sorted.sort((a, b) => {
                    const priceA = parseFloat(a.querySelector('.product-price').textContent.replace('$', ''));
                    const priceB = parseFloat(b.querySelector('.product-price').textContent.replace('$', ''));
                    return priceA - priceB;
                });
                break;

            case 'price-desc':
                sorted.sort((a, b) => {
                    const priceA = parseFloat(a.querySelector('.product-price').textContent.replace('$', ''));
                    const priceB = parseFloat(b.querySelector('.product-price').textContent.replace('$', ''));
                    return priceB - priceA;
                });
                break;

            case 'rating':
                sorted.sort((a, b) => {
                    const ratingA = parseFloat(a.querySelector('.rating-value').textContent);
                    const ratingB = parseFloat(b.querySelector('.rating-value').textContent);
                    return ratingB - ratingA;
                });
                break;

            case 'featured':
            default:
                // Keep original order
                break;
        }

        return sorted;
    }

    // Update products display
    function updateProductsDisplay(visibleProducts) {
        // Hide all products first
        allProducts.forEach(card => {
            card.style.display = 'none';
        });

        // Show and reorder visible products
        visibleProducts.forEach(card => {
            card.style.display = '';
            productsGrid.appendChild(card);
        });

        // Show "no results" message if needed
        const existingMessage = productsGrid.querySelector('.no-results-message');
        if (existingMessage) {
            existingMessage.remove();
        }

        if (visibleProducts.length === 0) {
            const noResultsMessage = document.createElement('div');
            noResultsMessage.className = 'no-results-message';
            noResultsMessage.style.cssText = 'grid-column: 1 / -1; text-align: center; padding: 3rem; color: #6b7280;';
            noResultsMessage.innerHTML = '<p style="font-size: 1.125rem; margin-bottom: 0.5rem;">Товары не найдены</p><p style="font-size: 0.875rem;">Попробуйте изменить фильтры или поисковый запрос</p>';
            productsGrid.appendChild(noResultsMessage);
        }
    }

    // Update results count
    function updateResultsCount(count) {
        if (resultsCount) {
            const total = allProducts.length;
            const showingText = resultsCount.textContent.split(' ')[0]; // Get "Показано" text
            const ofText = resultsCount.textContent.split(' ')[2]; // Get "из" text
            const productsText = resultsCount.textContent.split(' ').slice(-1)[0]; // Get "товаров" text
            resultsCount.textContent = `${showingText} ${count} ${ofText} ${total} ${productsText}`;
        }
    }

    // Debounce utility function
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // Initialize on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
