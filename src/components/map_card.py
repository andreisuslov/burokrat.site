from fasthtml.common import *
from .dropdown import create_dropdown
import json


def create_map_card(locations=None):
    """
    Create an interactive map card with 2GIS integration and location dropdown.
    
    Args:
        locations: List of location dictionaries with 'title', 'address', 'lat', 'lon' keys
    """
    if locations is None:
        locations = [
            {
                'title': 'Офис (Строителей)',
                'address': 'Строителей проспект, 4, г. Барнаул',
                'lat': 53.3606,
                'lon': 83.7636
            },
            {
                'title': 'Магазин (Социалистический)',
                'address': 'Социалистический проспект, 109, г. Барнаул',
                'lat': 53.3482,
                'lon': 83.7765
            }
        ]
    
    # Create dropdown options
    dropdown_options = [
        {
            'value': str(i),
            'label': loc['title'],
            'data_lat': loc['lat'],
            'data_lon': loc['lon'],
            'data_address': loc['address']
        }
        for i, loc in enumerate(locations)
    ]
    
    return Div(
        # Header with dropdown
        Div(
            H3('Наши адреса', cls='text-xl font-semibold mb-4'),
            create_dropdown(
                options=dropdown_options,
                selected_value='0',
                dropdown_id='location-selector',
                label='Выберите локацию:',
                onchange='updateMap(this)',
                variant='bordered',
                size='medium',
                full_width=True
            ),
            cls='p-6 pb-0'
        ),
        
        # Map container
        Div(
            id='map-container',
            cls='w-full bg-gray-100',
            style='width: 100%; height: 400px; position: relative;'
        ),
        
        # Address display
        Div(
            Div(
                NotStr('''<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>'''),
                cls='w-5 h-5 text-indigo-600 flex-shrink-0'
            ),
            P(
                locations[0]['address'],
                id='current-address',
                cls='text-gray-700'
            ),
            cls='p-6 pt-4 flex items-start gap-3 border-t border-gray-200'
        ),
        
        # Yandex Maps Script and initialization
        Script(src='https://api-maps.yandex.ru/2.1/?apikey=&lang=ru_RU', type='text/javascript'),
        Script(NotStr(f'''
            (function() {{
                let map;
                let placemark;
                const locations = {json.dumps(locations)};
                
                console.log('Map script loaded, locations:', locations);
                
                // Check if ymaps is available
                if (typeof ymaps === 'undefined') {{
                    console.error('Yandex Maps API not loaded');
                    return;
                }}
                
                // Initialize Yandex Map when API is loaded
                ymaps.ready(function() {{
                    console.log('Yandex Maps API ready');
                    
                    try {{
                        // Initialize with first location
                        const firstLoc = locations[0];
                        console.log('Initializing map with location:', firstLoc);
                        
                        map = new ymaps.Map('map-container', {{
                            center: [firstLoc.lat, firstLoc.lon],
                            zoom: 16,
                            controls: ['zoomControl', 'fullscreenControl', 'geolocationControl', 'typeSelector']
                        }});
                        
                        console.log('Map created successfully');
                        
                        // Add placemark (marker) with balloon
                        placemark = new ymaps.Placemark([firstLoc.lat, firstLoc.lon], {{
                            balloonContentHeader: firstLoc.title,
                            balloonContentBody: firstLoc.address,
                            balloonContentFooter: '<a href="https://yandex.ru/maps/?pt=' + firstLoc.lon + ',' + firstLoc.lat + '&z=16&l=map" target="_blank" style="color: #4f46e5; text-decoration: underline;">Открыть в Яндекс.Картах</a>',
                            hintContent: firstLoc.title
                        }}, {{
                            preset: 'islands#redDotIcon'
                        }});
                        
                        map.geoObjects.add(placemark);
                        placemark.balloon.open();
                        
                        // Enable all interactions
                        map.behaviors.enable('scrollZoom');
                        map.behaviors.enable('drag');
                        map.behaviors.enable('dblClickZoom');
                        map.behaviors.enable('multiTouch');
                        
                        // Make map clickable - show coordinates on click
                        map.events.add('click', function(e) {{
                            const coords = e.get('coords');
                            console.log('Map clicked at:', coords);
                        }});
                        
                        console.log('Map initialization complete');
                    }} catch (error) {{
                        console.error('Error initializing map:', error);
                    }}
                }});
                
                // Function to update map when location changes
                window.updateMap = function(selectElement) {{
                    const index = parseInt(selectElement.value);
                    const location = locations[index];
                    
                    console.log('Updating map to location:', location);
                    
                    if (map && placemark) {{
                        // Update map center
                        map.setCenter([location.lat, location.lon], 16, {{
                            duration: 300
                        }});
                        
                        // Remove old placemark
                        map.geoObjects.remove(placemark);
                        
                        // Create new placemark
                        placemark = new ymaps.Placemark([location.lat, location.lon], {{
                            balloonContentHeader: location.title,
                            balloonContentBody: location.address,
                            balloonContentFooter: '<a href="https://yandex.ru/maps/?pt=' + location.lon + ',' + location.lat + '&z=16&l=map" target="_blank" style="color: #4f46e5; text-decoration: underline;">Открыть в Яндекс.Картах</a>',
                            hintContent: location.title
                        }}, {{
                            preset: 'islands#redDotIcon'
                        }});
                        
                        map.geoObjects.add(placemark);
                        placemark.balloon.open();
                        
                        // Update address display
                        document.getElementById('current-address').textContent = location.address;
                    }}
                }};
            }})();
        ''')),
        
        cls='contact-card overflow-hidden'
    )
