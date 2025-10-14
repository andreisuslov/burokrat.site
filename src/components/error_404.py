from fasthtml.common import *

def create_404_page():
    """Create animated 404 error page with face animation and back button."""
    
    svg_content = '''
    <svg class="face" viewBox="0 0 320 380" width="320px" height="380px" aria-label="A 404 becomes a face, looks to the sides, and blinks. The 4s slide up, the 0 slides down, and then a mouth appears.">
        <g fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="25">
            <g class="face__eyes" transform="translate(0, 112.5)">
                <g transform="translate(15, 0)">
                    <polyline class="face__eye-lid" points="37,0 0,120 75,120" />
                    <polyline class="face__pupil" points="55,120 55,155" stroke-dasharray="35 35" />
                </g>
                <g transform="translate(230, 0)">
                    <polyline class="face__eye-lid" points="37,0 0,120 75,120" />
                    <polyline class="face__pupil" points="55,120 55,155" stroke-dasharray="35 35" />
                </g>
            </g>
            <rect class="face__nose" rx="4" ry="4" x="132.5" y="112.5" width="55" height="155" />
            <g stroke-dasharray="102 102" transform="translate(65, 334)">
                <path class="face__mouth-left" d="M 0 30 C 0 30 40 0 95 0" stroke-dashoffset="-102" />
                <path class="face__mouth-right" d="M 95 0 C 150 0 190 30 190 30" stroke-dashoffset="102" />
            </g>
        </g>
    </svg>
    '''
    
    return Div(
        NotStr(svg_content),
        H1('Страница не найдена', cls='error-404__title'),
        P('К сожалению, запрашиваемая страница не существует.', cls='error-404__message'),
        Button(
            '← Вернуться назад',
            cls='error-404__back-btn',
            onclick='if (document.referrer && document.referrer !== window.location.href) { window.history.back(); } else { window.location.href = "/"; }'
        ),
        cls='error-404__content'
    )
