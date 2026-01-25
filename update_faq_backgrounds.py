#!/usr/bin/env python3
import os

public_dir = "public"

# Pages to keep building background (hub + category pages)
keep_building = [
    'index.html',
    'family-law-topics.html',
    'personal-injury-topics.html',
    'criminal-defense-topics.html',
    'all-faqs.html'
]

# Individual FAQ pages that need logo background
for filename in os.listdir(public_dir):
    if not filename.endswith('.html'):
        continue

    if filename in keep_building:
        continue

    filepath = os.path.join(public_dir, filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace building background with logo background
    if "url('rrk-law-building.png')" in content:
        content = content.replace(
            "url('rrk-law-building.png')",
            "url('rrk-logo-dark.jpg')"
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Updated {filename} to use logo background")

print("Done! Individual FAQ pages now use clean logo background")
