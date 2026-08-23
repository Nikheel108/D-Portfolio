import re

with open('gsites/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make hamburger visible globally and hide tabs globally
css = css.replace('.hamburger{display:none;}', '.hamburger{display:flex;}')
css = css.replace('.tabs{display:flex;', '.tabs{display:none !important;')
# Also in mobile query, maybe remove or keep it since it's already hidden.
# I will just replace .nav-row { ... } to hide it completely, because we don't need the empty row?
# Wait, if tabs are hidden, nav-row has 1px bottom border. Let's hide nav-row completely.
css = css.replace('.nav-row{border-bottom:1px solid var(--rule);}', '.nav-row{display:none;}')

# Add blur to toolbar
toolbar_old = '''
.toolbar{
  position:sticky;top:0;z-index:800;
  background:color-mix(in srgb, var(--bg-elev) 92%, transparent);
  border-bottom:1px solid var(--rule);
}
'''
toolbar_new = '''
.toolbar{
  position:sticky;top:0;z-index:800;
  background:color-mix(in srgb, var(--bg-elev) 70%, transparent);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom:1px solid var(--rule);
}
'''
css = css.replace(toolbar_old.strip(), toolbar_new.strip())

# Change fixed top value for mobile-panel since nav-row is gone
# Let's check mobile-panel CSS
mobile_panel_old = '.mobile-panel.open{display:block;border-bottom:1px solid var(--rule);background:var(--bg-elev);}'
mobile_panel_new = '.mobile-panel.open{display:block;border-bottom:1px solid var(--rule);background:color-mix(in srgb, var(--bg-elev) 90%, transparent); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); position:fixed; top:54px; width:100%; z-index:790;}'
# But wait, mobile-panel is probably already positioned. Let's see its current CSS first.
# I'll just write it back.
with open('gsites/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

