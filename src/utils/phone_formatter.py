import re

def format_phone_number(phone_str):
    """
    Format a phone number string for display.
    Handles phone numbers with optional notes in parentheses at the end.
    
    Args:
        phone_str: Phone number string, possibly with note in parentheses
        
    Returns:
        tuple: (formatted_display_text, clean_tel_link, note_or_none)
    """
    # Extract note if present (text in parentheses at the end)
    note_match = re.search(r'\s*\(([^)]+)\)\s*$', phone_str)
    note = note_match.group(1) if note_match else None
    
    # Remove the note from the phone number
    phone_clean = re.sub(r'\s*\([^)]+\)\s*$', '', phone_str).strip()
    
    # Extract digits only for tel: link
    tel_link = re.sub(r'\D', '', phone_clean)
    
    # Format the display text
    # Keep the original formatting but ensure it's clean
    display_text = phone_clean
    
    return display_text, tel_link, note
