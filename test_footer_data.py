#!/usr/bin/env python3
"""Test script to verify footer data includes locations from about.yaml"""

from src.config import load_page_data, get_footer_data, get_about_data

# Load data
load_page_data()

# Get footer data
footer_data = get_footer_data()
about_data = get_about_data()

print("=" * 60)
print("FOOTER DATA TEST")
print("=" * 60)

# Check if locations exist in footer data
if 'locations' in footer_data:
    print("✓ 'locations' key found in footer_data")
    
    locations = footer_data.get('locations', {})
    offices = locations.get('offices', [])
    
    print(f"✓ Number of offices: {len(offices)}")
    
    for i, office in enumerate(offices, 1):
        print(f"\n  Office {i}:")
        print(f"    - Icon: {office.get('icon', 'N/A')}")
        print(f"    - Name: {office.get('name', 'N/A')}")
        print(f"    - Address: {office.get('address', 'N/A')}")
        print(f"    - Weekday hours: {office.get('hours', {}).get('weekdays', 'N/A')}")
        print(f"    - Maps query: {office.get('maps_query', 'N/A')}")
else:
    print("✗ 'locations' key NOT found in footer_data")
    print(f"  Available keys: {list(footer_data.keys())}")

print("\n" + "=" * 60)
print("ABOUT DATA TEST")
print("=" * 60)

# Check if locations exist in about data
if 'locations' in about_data:
    print("✓ 'locations' key found in about_data")
    locations = about_data.get('locations', {})
    offices = locations.get('offices', [])
    print(f"✓ Number of offices in about data: {len(offices)}")
else:
    print("✗ 'locations' key NOT found in about_data")

print("\n" + "=" * 60)
print("COMPARISON")
print("=" * 60)

footer_offices = footer_data.get('locations', {}).get('offices', [])
about_offices = about_data.get('locations', {}).get('offices', [])

if footer_offices == about_offices:
    print("✓ Footer locations match about locations")
else:
    print("✗ Footer locations DO NOT match about locations")

print("\n" + "=" * 60)
print("TEST COMPLETE")
print("=" * 60)
