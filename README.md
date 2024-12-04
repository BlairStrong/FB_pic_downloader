# 📷 Facebook Photo Scraper  

This project uses **Playwright** to automate the process of logging into Facebook and downloading photos from a specific profile or photo album. The script interacts with the Facebook UI to navigate, capture, and save images, while minimizing redundant downloads.  

---

## 📜 Project Description  

### Key Features:  
- **Automated Login**: Logs into Facebook using the provided credentials.  
- **Photo Scraping**: Iterates through photos in a specified album or profile and downloads unique images.  
- **Efficient Processing**: Avoids duplicate downloads by checking and appending new image URLs.  
- **Headless Mode Support**: Runs in both headless (background) and non-headless (visible browser) modes.  

---

## 🛠️ Technologies Used  

- **Python**  
- **Playwright** (Async API)  
- **BeautifulSoup** for parsing web data (minor usage)  
- **Lxml** for additional HTML parsing  
- **Other Libraries**: `asyncio`, `datetime`, `time`, `keyboard`, `requests`  

---

## 🚀 How to Install and Run  

### Prerequisites  
1. Install Python 3.7+  
2. Install Playwright:  
   ```bash
   pip install playwright
   playwright install
