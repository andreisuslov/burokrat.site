# Contact Page Navigation Reference

This document provides a quick reference for navigating the contact page structure using class names and IDs.

## Page Structure Overview

The contact page (`/contact`) is organized into the following major sections:

### 1. Contact Page Container
- **ID**: `contact-page`
- **Class**: `contact-page-container`
- **Description**: Main wrapper for the entire contact page

---

### 2. Contact Header Section
- **ID**: `contact-header-section`
- **Class**: `contact-page-header`
- **Description**: Top banner with gradient background, badge, title, and description
- **Component**: `create_contact_header()`

---

### 3. Contact Info Grid Section
- **ID**: `contact-info-grid-section`
- **Class**: `contact-info-cards`
- **Description**: Grid of contact information cards (address, phone, hours, email)
- **Component**: `create_contact_info_grid()`

---

### 4. Main Content Section
- **ID**: `contact-main-content`
- **Class**: `contact-content-wrapper`
- **Description**: Container for the 2-column layout (form + sidebar)

#### 4.1 Contact Main Grid
- **Class**: `contact-main-grid`
- **Description**: Grid layout container for form and sidebar

#### 4.2 Contact Form Column (Left)
- **ID**: `contact-form-section`
- **Class**: `contact-form-column`
- **Component**: `create_contact_form()`
- **Contains**:
  - Form fields (name, email, phone, subject, message)
  - Submit button: `#contact-submit-btn`
  - Status message: `#contact-status`

#### 4.3 Store Info Sidebar (Right)
- **ID**: `store-sidebar`
- **Class**: `store-info-sidebar`
- **Component**: `create_store_info_sidebar()`

##### 4.3.1 Visit Store Card
- **ID**: `visit-store-section`
- **Class**: `visit-store-card`
- **Contains**:
  - **Image Container**: `.store-image-container`
  - **Store Image**: `.store-image`
  - **Store Info Content**: `.store-info-content`
    - **Title**: `.store-title`
    - **Description**: `.store-description`
    - **Directions Link**: `.store-directions-link`

##### 4.3.2 Map Card
- **Component**: `create_map_card()`
- **Description**: Interactive map showing store locations

---

### 5. FAQ Section
- **ID**: `contact-faq-section`
- **Class**: `contact-faq-wrapper`
- **Component**: `create_faq_section()`
- **Description**: Frequently asked questions section

---

## Quick Navigation Selectors

### By ID
```javascript
// Main page
document.getElementById('contact-page')

// Header
document.getElementById('contact-header-section')

// Info grid
document.getElementById('contact-info-grid-section')

// Main content
document.getElementById('contact-main-content')

// Form
document.getElementById('contact-form-section')

// Store sidebar
document.getElementById('store-sidebar')

// Visit store card
document.getElementById('visit-store-section')

// FAQ
document.getElementById('contact-faq-section')
```

### By Class
```javascript
// Page container
document.querySelector('.contact-page-container')

// Header
document.querySelector('.contact-page-header')

// Info cards
document.querySelector('.contact-info-cards')

// Form column
document.querySelector('.contact-form-column')

// Sidebar
document.querySelector('.store-info-sidebar')

// Store elements
document.querySelector('.visit-store-card')
document.querySelector('.store-image')
document.querySelector('.store-title')
document.querySelector('.store-description')
document.querySelector('.store-directions-link')
```

---

## Component Files

- **Main View**: `/src/pages/contact/view.py`
- **Contact Header**: `/src/components/contact_header.py`
- **Contact Info Grid**: `/src/components/contact_info_grid.py`
- **Contact Form**: `/src/components/contact_form.py`
- **FAQ Section**: `/src/components/faq_section.py`
- **Map Card**: `/src/components/map_card.py`
- **Route Handler**: `/src/routes/contact.py`

---

## CSS Styling

All contact page styles are defined in `/assets/styles/main.css`. Look for:
- `.contact-card`
- `.contact-form-modern`
- `.form-input`
- `.form-textarea`
- `.btn-submit`
- `.contact-status`

---

## Form Elements

### Form Fields
- **Name**: `#contact-name`
- **Email**: `#contact-email`
- **Phone**: `#contact-phone`
- **Subject**: `#contact-subject`
- **Message**: `#contact-message`
- **Consent**: `#contact-consent`

### Form Actions
- **Submit Button**: `#contact-submit-btn`
- **Status Message**: `#contact-status`
- **Form Container**: `.contact-form-modern`

---

## Data Configuration

Contact page data is loaded from `/data/contact.yaml` via the `get_contact_data()` function in `/src/config/data_loader.py`.
