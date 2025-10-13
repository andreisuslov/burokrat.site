from fasthtml.common import *


def create_faq_item(faq, index):
    """Create a single FAQ accordion item."""
    question = faq.get('question', '')
    answer = faq.get('answer', '')
    item_id = f"faq-item-{index}"
    
    return Div(
        # Accordion trigger (question)
        Button(
            Span(question, cls='pr-4'),
            Span(
                NotStr('''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="accordion-icon"><polyline points="6 9 12 15 18 9"/></svg>'''),
                cls='accordion-icon-wrapper'
            ),
            type='button',
            cls='accordion-trigger',
            data_target=item_id,
            onclick=f"toggleAccordion('{item_id}')"
        ),
        
        # Accordion content (answer)
        Div(
            Div(
                answer,
                cls='accordion-content-inner'
            ),
            id=item_id,
            cls='accordion-content',
            style='max-height: 0; overflow: hidden;'
        ),
        
        cls='accordion-item border rounded-lg px-6 bg-gray-50'
    )


def create_faq_section(data=None):
    """
    Create FAQ section with accordion.
    
    Args:
        data: Dictionary with FAQ configuration:
            - title: Section title
            - subtitle: Section subtitle
            - items: List of FAQ items with 'question' and 'answer'
    """
    if data is None:
        data = {}
    
    title = data.get('title', 'Frequently Asked Questions')
    subtitle = data.get('subtitle', 'Find quick answers to common questions')
    items = data.get('items', [
        {
            'question': 'What kind of printing services do you offer?',
            'answer': 'We provide a variety of polygraphic services, including standard document printing and copying...'
        }
    ])
    
    return Div(
        Div(
            # Section header
            Div(
                H2(title, cls='text-4xl mb-4'),
                P(subtitle, cls='text-xl text-gray-600'),
                cls='text-center mb-12'
            ),
            
            # Accordion container
            Div(
                *[create_faq_item(faq, idx) for idx, faq in enumerate(items)],
                cls='faq-accordion space-y-4'
            ),
            
            cls='max-w-4xl mx-auto px-4 sm:px-6 lg:px-8'
        ),
        
        # Accordion JavaScript
        Script("""
function toggleAccordion(itemId) {
    const content = document.getElementById(itemId);
    const trigger = document.querySelector(`[data-target="${itemId}"]`);
    const allContents = document.querySelectorAll('.accordion-content');
    const allTriggers = document.querySelectorAll('.accordion-trigger');
    
    // Close all other accordions
    allContents.forEach(item => {
        if (item.id !== itemId) {
            item.style.maxHeight = '0';
            item.classList.remove('active');
        }
    });
    
    allTriggers.forEach(btn => {
        if (btn.getAttribute('data-target') !== itemId) {
            btn.classList.remove('active');
        }
    });
    
    // Toggle current accordion
    if (content.classList.contains('active')) {
        content.style.maxHeight = '0';
        content.classList.remove('active');
        trigger.classList.remove('active');
    } else {
        content.style.maxHeight = content.scrollHeight + 'px';
        content.classList.add('active');
        trigger.classList.add('active');
    }
}

// Optional: Close accordion when clicking outside
document.addEventListener('click', function(event) {
    const accordionContainer = document.querySelector('.faq-accordion');
    if (accordionContainer && !accordionContainer.contains(event.target)) {
        const allContents = document.querySelectorAll('.accordion-content');
        const allTriggers = document.querySelectorAll('.accordion-trigger');
        
        allContents.forEach(item => {
            item.style.maxHeight = '0';
            item.classList.remove('active');
        });
        
        allTriggers.forEach(btn => {
            btn.classList.remove('active');
        });
    }
});
        """),
        
        cls='faq-section bg-white py-16'
    )
