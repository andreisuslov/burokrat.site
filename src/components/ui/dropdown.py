from fasthtml.common import *


def create_dropdown(
    options,
    selected_value=None,
    dropdown_id=None,
    name=None,
    label=None,
    placeholder=None,
    onchange=None,
    required=False,
    disabled=False,
    variant='default',
    size='medium',
    width=None,
    full_width=False,
    custom_class=None
):
    """
    Create a stylish, reusable dropdown component.
    
    Args:
        options: List of option dictionaries with 'value', 'label', and optional 'data_*' attributes
                 OR list of tuples (value, label)
                 OR list of strings (used as both value and label)
        selected_value: Value of the option to be selected by default
        dropdown_id: ID attribute for the select element
        name: Name attribute for the select element
        label: Optional label text to display above the dropdown
        placeholder: Optional placeholder option (disabled, selected by default if no selected_value)
        onchange: JavaScript function to call on change event
        required: Whether the field is required
        disabled: Whether the dropdown is disabled
        variant: Style variant - 'default', 'primary', 'minimal', 'bordered'
        size: Size variant - 'small', 'medium', 'large'
        width: Width variant - 'short', 'medium', 'long' (optional, overrides full_width)
        full_width: Whether the dropdown should take full width
        custom_class: Additional CSS classes to apply
    
    Returns:
        Div containing the dropdown with optional label
    """
    
    # Normalize options to dictionaries
    normalized_options = []
    for opt in options:
        if isinstance(opt, dict):
            normalized_options.append(opt)
        elif isinstance(opt, (tuple, list)) and len(opt) >= 2:
            normalized_options.append({'value': opt[0], 'label': opt[1]})
        else:
            # String or single value
            normalized_options.append({'value': str(opt), 'label': str(opt)})
    
    # Build CSS classes for select element (no width classes)
    select_classes = ' '.join(filter(None, [
        'dropdown-select',
        f'dropdown-{variant}',
        f'dropdown-{size}',
        custom_class
    ]))
    
    # Build width class for wrapper
    if width:
        wrapper_width_class = f'dropdown-width-{width}'
    elif full_width:
        wrapper_width_class = 'dropdown-full-width'
    else:
        wrapper_width_class = ''
    
    # Create option elements
    option_elements = []
    
    # Add placeholder if provided
    if placeholder:
        option_elements.append(
            Option(
                placeholder,
                value='',
                disabled=True,
                selected=(selected_value is None)
            )
        )
    
    # Add regular options
    for opt in normalized_options:
        opt_value = opt.get('value', '')
        opt_label = opt.get('label', opt_value)
        is_selected = (str(opt_value) == str(selected_value)) if selected_value is not None else False
        
        # Extract data attributes
        data_attrs = {k: v for k, v in opt.items() if k.startswith('data_')}
        
        option_elements.append(
            Option(
                opt_label,
                value=opt_value,
                selected=is_selected,
                **data_attrs
            )
        )
    
    # Create select element
    select_attrs = {}
    if dropdown_id:
        select_attrs['id'] = dropdown_id
    if name:
        select_attrs['name'] = name
    if onchange:
        select_attrs['onchange'] = onchange
    if required:
        select_attrs['required'] = True
    if disabled:
        select_attrs['disabled'] = True
    
    select_element = Select(
        *option_elements,
        cls=select_classes,
        **select_attrs
    )
    
    # Create dropdown icon (chevron)
    dropdown_icon = Div(
        NotStr('''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>'''),
        cls='dropdown-icon'
    )
    
    # Wrap select with icon and apply width class to wrapper
    wrapper_classes = ' '.join(filter(None, ['dropdown-wrapper', wrapper_width_class]))
    select_wrapper = Div(
        select_element,
        dropdown_icon,
        cls=wrapper_classes
    )
    
    # If label is provided, wrap in a field container
    if label:
        label_element = Label(
            label,
            ' *' if required else '',
            fr=dropdown_id,
            cls='dropdown-label'
        )
        
        return Div(
            label_element,
            select_wrapper,
            cls='dropdown-field'
        )
    
    return select_wrapper


def create_icon_svg(icon_type):
    """Create inline SVG icons for dropdown decorations."""
    icons = {
        'chevron-down': '''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>''',
        'check': '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>''',
    }
    return NotStr(icons.get(icon_type, icons['chevron-down']))
