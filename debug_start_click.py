from playwright.sync_api import sync_playwright
from pathlib import Path

html = Path('E:/VRproject/index.html').read_text(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 800})
    page.on('console', lambda msg: print('console:', msg.type, msg.text))
    page.on('pageerror', lambda err: print('pageerror:', err))
    page.set_content(html)
    print('page loaded')

    page.fill('#name-input', 'Test')
    page.fill('#age-input', '25')
    page.fill('#exp-input', '2')
    page.fill('#device-input', 'PC')

    print('before start display=', page.locator('#start-page').evaluate('el => getComputedStyle(el).display'))
    page.click('#start-btn')
    page.wait_for_timeout(2000)
    print('after start display=', page.locator('#start-page').evaluate('el => getComputedStyle(el).display'))
    print('shorts display=', page.locator('#shorts-container').evaluate('el => getComputedStyle(el).display'))
    html_after = page.locator('#shorts-container').inner_html()
    print('shorts html=', html_after[:500])
    browser.close()
