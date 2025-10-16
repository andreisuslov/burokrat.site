# 404 Error Page - Usage Guide

## Overview
The 404 error page features an animated SVG face that provides a friendly, engaging experience when users encounter a page that doesn't exist.

## Features
- **Animated SVG Face**: The face animates with blinking eyes, looking around, and a smile appearing
- **Responsive Design**: Adapts to different screen sizes
- **Smooth Animations**: CSS keyframe animations for natural movement
- **Clear Call-to-Action**: "Go Back Home" button to help users navigate back

## File Structure

### Component
- **Location**: `src/components/error_404.py`
- **Function**: `create_404_page()`
- **Returns**: FastHTML Main element with animated SVG and error message

### Route
- **Location**: `src/routes/error_404.py`
- **Function**: `register_404_handler(rt)`
- **URL**: `/404`

### Styles
- **Location**: `assets/styles/main.css`
- **Section**: Lines 3623-3808
- **Classes**:
  - `.error-404` - Main container
  - `.error-404__title` - Page title
  - `.error-404__message` - Error message
  - `.error-404__link` - Home button
  - `.face` - SVG face container
  - `.face__*` - Face animation elements

## Animation Details

### Face Animations
1. **Eyes Animation** (1s): Eyes slide up from bottom to top
2. **Pupil Animation** (4s loop): Eyes look left and right, blink
3. **Eye Lid Animation** (4s loop): Blinking effect
4. **Mouth Animation** (1s): Mouth appears with smile
5. **Nose Animation** (1s): Nose slides down

### Timing
- Initial animation: 0.3s delay
- Loop animations: 1.3s delay, infinite repeat
- Smooth cubic-bezier easing functions

## Usage

### Accessing the Page
Navigate to any non-existent URL or directly to `/404`:
```
http://localhost:8080/404
```

### Integration
The 404 page is automatically registered with the application through:
1. Component export in `src/components/__init__.py`
2. Route registration in `src/routes/__init__.py`
3. Called in `register_all_routes()` function

## Customization

### Changing Colors
The page uses CSS variables from the main theme:
```css
--primary-color: #080aa6;  /* Title and button color */
--text-color: #1a1a1a;     /* Message text color */
--hover-blue: #0a0cc7;     /* Button hover color */
```

### Modifying Text
Edit the component in `src/components/error_404.py`:
```python
H1('Page Not Found', cls='error-404__title'),
P('The page you are looking for does not exist.', cls='error-404__message'),
A('Go Back Home', href='/', cls='error-404__link'),
```

### Adjusting Animation Speed
Modify animation durations in `assets/styles/main.css`:
```css
.face__eyes {
    animation: eyes 1s 0.3s cubic-bezier(0.65, 0, 0.35, 1) forwards;
}
```

### Changing Face Size
Update the `.face` class:
```css
.face {
    width: 12em;  /* Adjust this value */
}
```

## Responsive Behavior

### Desktop (> 768px)
- Face size: 12em
- Title: 2rem
- Message: 1.125rem
- Padding: 3rem 1.5rem

### Mobile (≤ 768px)
- Face size: 10em
- Title: 1.5rem
- Message: 1rem
- Padding: 2rem 1rem

## Browser Compatibility
- Modern browsers with CSS animations support
- SVG support required
- CSS Grid support required

## Testing
To test the 404 page:
1. Start the development server
2. Navigate to `http://localhost:8080/404`
3. Or visit any non-existent URL (when error handler is configured)

## Future Enhancements
Consider adding:
- Sound effects on animation
- Additional face expressions
- Random animation variations
- Search functionality
- Popular page suggestions
- Breadcrumb navigation
