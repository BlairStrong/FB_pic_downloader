from playwright.sync_api import sync_playwright
import asyncio
import datetime
import time
import requests
from playwright.async_api import async_playwright
from time import sleep

import urllib.request
from lxml import etree, html
import csv
import urllib.parse
import keyboard
from bs4 import BeautifulSoup
import requests



async def get_urls(email, password,headless):
    url_list = []
    downloaded_counter = 0
    seen_counter = 0
    async with async_playwright() as p:
        page = await log_in(email, headless, p, password)
        downloaded_counter = await download(headless, email, page, url_list, downloaded_counter)
        await page.keyboard.press("ArrowRight")
        current_page_url = page.url
        await page.wait_for_load_state(state="networkidle")
        await page.goto("https://www.facebook.com/photo/?fbid=1501390463713235&set=pob.660980376")
        await page.wait_for_load_state(state="networkidle")
        await page.keyboard.press("ArrowRight")
        current_url = page.url
        while current_url != "https://www.facebook.com/photo/?fbid=1501390463713235&set=pob.660980376":
            url_list.append(page.url)
            await page.wait_for_load_state(state="networkidle")
            downloaded_counter = await download(headless, email, page, url_list, downloaded_counter)
            await page.keyboard.press("ArrowRight")
            seen_counter += 1
            print("Seen:", seen_counter, "\ndownloaded:",downloaded_counter)
    return url_list


async def download(headless, email, page, url_list, downloaded_counter):
    img_elements = await page.query_selector_all('img')
    for img in img_elements:
        src = await img.get_attribute('src')
        if len(src) > 50 and src[:5] == "https":
            if src not in url_list:
                await get_img(src, email, headless, downloaded_counter)
                url_list.append(src)
                downloaded_counter += 1
            print(src)
    return downloaded_counter


async def log_in(email, headless, p, password):
    print("Attempting log-in...")
    browser = await p.chromium.launch(headless=headless)
    page = await browser.new_page()
    await page.goto("http://www.facebook.com")
    await page.wait_for_load_state(state="networkidle")
    await page.click('button:has-text("Allow essential and optional cookies")')
    await page.wait_for_load_state(state="networkidle")
    await page.fill("input#email", email)
    await page.fill("input#pass", password)
    await page.get_by_test_id("royal_login_button").click()
    await page.get_by_text("Rachel Hannay").click()
    await page.wait_for_load_state(state="networkidle")
    await page.goto("https://www.facebook.com/photo/?fbid=1501390463713235&set=pob.660980376")
    await page.wait_for_load_state(state="networkidle")
    return page


async def get_img(src, email, headless, counter):
    async with async_playwright() as p:
        print("getting photo source")
        browser = await p.chromium.launch(headless=headless)
        page = await browser.new_page()
        await page.goto(src)
        await page.wait_for_load_state(state="networkidle")
        await page.get_by_role("img").screenshot(path=f"{email}Photos{counter}.png")
        print("Saved")
        await browser.close()



async def mright_click_Save(email, password,headless=True):
    url_list = []
    counter = 0
    async with async_playwright() as p:
        print("Attempting log-in...")
        browser = await p.chromium.launch(headless=headless)
        page = await browser.new_page()
        await page.goto("http://www.facebook.com")
        await page.wait_for_load_state(state="networkidle")
        await page.click('button:has-text("Allow essential and optional cookies")')
        await page.wait_for_load_state(state="networkidle")
        await page.fill("input#email", email)
        await page.fill("input#pass", password)
        await page.get_by_test_id("royal_login_button").click()
        await page.get_by_text("Rachel Hannay").click()
        await page.wait_for_load_state(state="networkidle")
        await page.goto("https://www.facebook.com/photo.php?fbid=1501390463713235&set=t.660980376&type=3")
        await page.get_by_label("Enter fullscreen").click()
        print("entering full screen")
        while True:
            await page.wait_for_load_state(state="networkidle")

            print(len(img_elements))
            await page.get_by_role("Div", name="Main").screenshot(path="screenshot.png")
            await page.mouse.click(600, 400, button="right")
            sleep(0.1)


            await page.keyboard.press("ArrowRight")
            print("pressed right arrowkey")
            print(f"Picture {counter} saved")
            counter += 1
            sleep(1000)

async def main():
    url_list = await get_urls("rachelhannay@hotmail.com", "miriam", headless=False)



if __name__ == "__main__":
    asyncio.run(main())