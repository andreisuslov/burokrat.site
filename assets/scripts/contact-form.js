// Contact form validation with Russian error messages
// This file is currently unused
/**
 * Contact Form Validation
 * Handles client-side validation for the contact form
 * 
 * NOTE: This file is for reference only. The actual form validation
 * is embedded inline in src/pages/home/view.py which loads error 
 * messages dynamically from data/contact.yaml
 */

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.contact-form');
    if (!form) return;

    // Error messages - in production these are loaded from YAML via Python
    // See src/pages/home/view.py for the actual implementation
    const errorMessages = {
        name: "Пожалуйста, заполните поле имени.",
        email: "Пожалуйста, введите корректный email адрес.",
        comment: "Пожалуйста, опишите ваш вопрос или запрос.",
        consent: "Чтобы отправить форму, подтвердите согласие с политикой конфиденциальности."
    };

    // Remove existing error messages with gentle fade-out
    function clearErrors() {
        const inputs = form.querySelectorAll('input, textarea');
        inputs.forEach(input => {
            input.classList.remove('error');
            input.setCustomValidity('');
            // Remove any existing error message elements immediately to prevent duplicates
            const errorMsg = input.parentNode.querySelector('.error-message');
            if (errorMsg) {
                errorMsg.remove();
            }
        });
    }

    // Show error message for a field
    function showError(field, message) {
        // Check if error already exists for this field
        const existingError = field.parentNode.querySelector('.error-message');
        const isNewError = !existingError;
        
        field.classList.add('error');
        field.setCustomValidity(message);
        
        // Only create new error message if one doesn't exist
        if (isNewError) {
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.textContent = message;
            errorDiv.style.color = '#e74c3c';
            errorDiv.style.fontSize = '14px';
            errorDiv.style.marginTop = '5px';
            
            // Insert after the field
            field.parentNode.appendChild(errorDiv);
        }
    }

    // Validate individual field
    function validateField(field) {
        const name = field.name;
        const value = field.value.trim();
        
        if (field.hasAttribute('required') && !value) {
            showError(field, errorMessages[name] || 'Это поле обязательно для заполнения.');
            return false;
        }
        
        if (name === 'email' && value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                showError(field, errorMessages.email);
                return false;
            }
        }
        
        if (name === 'consent' && field.type === 'checkbox' && !field.checked) {
            showError(field, errorMessages.consent);
            return false;
        }
        
        // Field is valid - remove error if it exists
        field.classList.remove('error');
        field.setCustomValidity('');
        const errorMsg = field.parentNode.querySelector('.error-message');
        if (errorMsg) {
            errorMsg.remove();
        }
        
        return true;
    }

    // Validate entire form
    function validateForm() {
        const fields = form.querySelectorAll('input[required]:not([type="checkbox"]), textarea[required]');
        let isValid = true;
        
        fields.forEach(field => {
            if (!validateField(field)) {
                isValid = false;
            }
        });
        
        // Check consent checkbox separately
        const consentField = form.querySelector('#contact-consent');
        if (consentField && !validateField(consentField)) {
            isValid = false;
        }
        
        return isValid;
    }

    // Add real-time validation
    const inputs = form.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value.trim() || this.hasAttribute('data-touched')) {
                this.setAttribute('data-touched', 'true');
                validateField(this);
            }
        });
        
        input.addEventListener('input', function() {
            if (this.hasAttribute('data-touched')) {
                validateField(this);
            }
        });
    });

    // Handle form submission
    form.addEventListener('submit', function(e) {
        if (!validateForm()) {
            e.preventDefault();
            e.stopPropagation();
            
            // Focus on first error field
            const firstError = form.querySelector('.error');
            if (firstError) {
                firstError.focus();
            }
        }
    });

    // Handle HTMX before request
    form.addEventListener('htmx:beforeRequest', function(e) {
        if (!validateForm()) {
            e.preventDefault();
            const firstError = form.querySelector('.error');
            if (firstError) {
                firstError.focus();
            }
        }
    });

    // Auto-dismiss contact status after 4 seconds
    const contactStatus = document.getElementById('contact-status');
    if (contactStatus) {
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (contactStatus.textContent.trim() !== '') {
                    // Wait 4 seconds then fade out
                    setTimeout(function() {
                        contactStatus.style.transition = 'opacity 0.5s ease-out';
                        contactStatus.style.opacity = '0';
                        setTimeout(function() {
                            contactStatus.innerHTML = '';
                            contactStatus.style.opacity = '1';
                        }, 500);
                    }, 4000);
                }
            });
        });
        observer.observe(contactStatus, { childList: true, subtree: true });
    }
});
