#!/usr/bin/env python3
import os
import re

public_dir = "public"

# Replace old back button with new one that goes to all-faqs.html
old_back_button = '<a href="/index.html" style="background-color: #BDBDBD; color: #1a1a1a; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block;">← Back to Hub</a>'

new_back_button = '<a href="/all-faqs.html" style="background-color: #BDBDBD; color: #1a1a1a; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; margin-right: 10px;">← All FAQ Topics</a><a href="/index.html" style="color: #BDBDBD; text-decoration: none; padding: 10px;">Home</a>'

for filename in os.listdir(public_dir):
    if filename.endswith('.html') and filename not in ['index.html', 'all-faqs.html']:
        filepath = os.path.join(public_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_back_button in content:
            content = content.replace(old_back_button, new_back_button)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"Updated back button in {filename}")

print("Done updating back buttons to link to all-faqs.html")
