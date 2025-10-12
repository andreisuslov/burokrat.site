import yaml
from pathlib import Path

_data = {}

def load_yaml_file(filename):
    """Load a YAML file from the data directory."""
    data_dir = Path(__file__).parent.parent.parent / 'data'
    file_path = data_dir / filename
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def load_page_data():
    """Load main page data from YAML file."""
    global _data
    _data['main'] = load_yaml_file('main_page.yaml')
    return _data

def load_about_data():
    """Load about page data from YAML file."""
    global _data
    if 'about' not in _data:
        _data['about'] = load_yaml_file('about.yaml')
    return _data['about']

def get_data():
    """Get main page data."""
    return _data.get('main', {})

def get_about_data():
    """Get about page data."""
    if 'about' not in _data:
        load_about_data()
    return _data['about']

def load_privacy_data():
    """Load privacy page data from YAML file."""
    global _data
    if 'privacy' not in _data:
        _data['privacy'] = load_yaml_file('privacy.yaml')
    return _data['privacy']

def get_privacy_data():
    """Get privacy page data."""
    if 'privacy' not in _data:
        load_privacy_data()
    return _data['privacy']

def load_contact_data():
    """Load contact page data from YAML file."""
    global _data
    if 'contact' not in _data:
        _data['contact'] = load_yaml_file('contact.yaml')
    return _data['contact']

def get_contact_data():
    """Get contact page data."""
    if 'contact' not in _data:
        load_contact_data()
    return _data['contact']

def load_seals_stamps_data():
    """Load seals and stamps page data from YAML file."""
    global _data
    if 'seals_stamps' not in _data:
        _data['seals_stamps'] = load_yaml_file('seals_stamps.yaml')
    return _data['seals_stamps']

def get_seals_stamps_data():
    """Get seals and stamps page data."""
    if 'seals_stamps' not in _data:
        load_seals_stamps_data()
    return _data['seals_stamps']

def load_self_inking_stamps_data():
    """Load self-inking stamps page data from YAML file."""
    global _data
    if 'self_inking_stamps' not in _data:
        _data['self_inking_stamps'] = load_yaml_file('self_inking_stamps.yaml')
    return _data['self_inking_stamps']

def get_self_inking_stamps_data():
    """Get self-inking stamps page data."""
    if 'self_inking_stamps' not in _data:
        load_self_inking_stamps_data()
    return _data['self_inking_stamps']

def load_stationery_data():
    """Load stationery page data from YAML file."""
    global _data
    if 'stationery' not in _data:
        _data['stationery'] = load_yaml_file('stationery.yaml')
    return _data['stationery']

def get_stationery_data():
    """Get stationery page data."""
    if 'stationery' not in _data:
        load_stationery_data()
    return _data['stationery']

def load_clients_data():
    """Load clients page data from YAML file."""
    global _data
    if 'clients' not in _data:
        _data['clients'] = load_yaml_file('clients.yaml')
    return _data['clients']

def get_clients_data():
    """Get clients page data."""
    if 'clients' not in _data:
        load_clients_data()
    return _data['clients']

def load_agreement_data():
    """Load agreement page data from YAML file."""
    global _data
    if 'agreement' not in _data:
        _data['agreement'] = load_yaml_file('agreement.yaml')
    return _data['agreement']

def get_agreement_data():
    """Get agreement page data."""
    if 'agreement' not in _data:
        load_agreement_data()
    return _data['agreement']
