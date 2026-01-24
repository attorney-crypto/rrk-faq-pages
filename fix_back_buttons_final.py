#!/usr/bin/env python3
import os

public_dir = "public"

# Map each FAQ page to its category page
category_mapping = {
    # Family Law
    'divorce-faq.html': 'family-law-topics.html',
    'child-custody-faq.html': 'family-law-topics.html',
    'child-support-faq.html': 'family-law-topics.html',
    'family-law-faq.html': 'family-law-topics.html',
    'family-law.html': 'family-law-topics.html',
    'divorce.html': 'family-law-topics.html',

    # Personal Injury
    'car-accident-faq.html': 'personal-injury-topics.html',
    'car-accident-lawyer.html': 'personal-injury-topics.html',
    'truck-accident-faq.html': 'personal-injury-topics.html',
    'truck-accident-lawyer.html': 'personal-injury-topics.html',
    'motorcycle-accident-faq.html': 'personal-injury-topics.html',
    'slip-and-fall-faq.html': 'personal-injury-topics.html',
    'dog-bite-faq.html': 'personal-injury-topics.html',
    'personal-injury.html': 'personal-injury-topics.html',

    # Criminal Defense
    'assault-faq.html': 'criminal-defense-topics.html',
    'dwi-faq.html': 'criminal-defense-topics.html',
    'drug-possession-faq.html': 'criminal-defense-topics.html',
    'criminal-defense.html': 'criminal-defense-topics.html',

    # Other
    'senate-bill-30-texas.html': 'index.html',
}

for filename, category_page in category_mapping.items():
    filepath = os.path.join(public_dir, filename)
    if not os.path.exists(filepath):
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace back button
    old_pattern = '<a href="/all-faqs.html" style="background-color: #BDBDBD; color: #1a1a1a; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; margin-right: 10px;">← All FAQ Topics</a><a href="/index.html" style="color: #BDBDBD; text-decoration: none; padding: 10px;">Home</a>'

    new_button = f'<a href="/{category_page}" style="background-color: #BDBDBD; color: #1a1a1a; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block;">← Back</a>'

    if old_pattern in content:
        content = content.replace(old_pattern, new_button)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Updated {filename} -> back to {category_page}")

print("Done fixing back buttons")
