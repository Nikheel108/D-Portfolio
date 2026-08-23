import re

with open('gsites/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update CGPA in kernel bot
js = js.replace('first-semester CGPA 8.9', 'first-semester CGPA 8.63')
# Add new achievements in kernel bot
js = js.replace('plus a district-level cultural performance', 'plus a district-level cultural performance, and 2nd Runner Up in both TECHSPRINT & NIRMAN 4.0 by GDG')

with open('gsites/app.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated app.js")
