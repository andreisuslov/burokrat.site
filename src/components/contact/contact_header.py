from fasthtml.common import *


def create_contact_header(data=None):
    """Create contact page header with gradient background."""
    if data is None:
        data = {}
    
    badge_text = data.get('badge', 'Get In Touch')
    title = data.get('title', 'Contact Us')
    description = data.get('description', 
        "Have questions? We'd love to hear from you. Send us a message and we'll respond as soon as possible.")
    
    return Div(
        Div(
            Div(
                # Badge
                Div(
                    Span(
                        badge_text,
                        cls='px-4 py-2 bg-indigo-100 text-indigo-700 rounded-full'
                    ),
                    cls='inline-block mb-4'
                ),
                
                # Title
                H1(
                    title,
                    cls='text-5xl mb-4'
                ),
                
                # Description
                P(
                    description,
                    cls='text-xl text-gray-600 max-w-2xl mx-auto'
                ),
                
                cls='text-center'
            ),
            cls='max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16'
        ),
        cls='bg-gradient-to-br from-indigo-50 via-white to-purple-50'
    )
