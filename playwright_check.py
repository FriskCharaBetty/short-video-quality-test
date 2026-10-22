from playwright.sync_api import sync_playwright
from pathlib import Path

html = Path('E:/VRproject/index.html').read_text(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.on('console', lambda msg: print('console:', msg.type, msg.text))
    page.on('pageerror', lambda err: print('pageerror:', err))
    page.set_content(html)
    print('page loaded')
    page.fill('#name-input', 'Test')
    page.fill('#age-input', '25')
    page.fill('#exp-input', '2')
    page.fill('#device-input', 'PC')
    page.click('#start-btn')
    page.wait_for_timeout(2000)
    print('start_page_display=', page.locator('#start-page').evaluate('el => getComputedStyle(el).display'))
    print('shorts_display=', page.locator('#shorts-container').evaluate('el => getComputedStyle(el).display'))
    print('shorts_html=', page.locator('#shorts-container').inner_html()[:200])
    browser.close()
