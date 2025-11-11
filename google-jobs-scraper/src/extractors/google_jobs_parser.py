thonimport requests
from bs4 import BeautifulSoup
import json

def parse_google_jobs(search_text, proxy=None, cookies=None):
    url = f"https://www.google.com/search?q={search_text}&tbs=qdr:d"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers, proxies=proxy, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    job_listings = []
    for job in soup.find_all('div', class_='BjJfJf'):
        job = {
            "title": job.find('div', class_='BjJfJf').text,
            "company": job.find('div', class_='Qk80Jf').text if job.find('div', class_='Qk80Jf') else "Unknown",
            "location": job.find('div', class_='Qk80Jf').text if job.find('div', class_='Qk80Jf') else "Unknown",
            "date_posted": job.find('div', class_='nL5hS').text if job.find('div', class_='nL5hS') else "Unknown",
            "job_url": job.find('a')['href']
        }
        job_listings.append(job)
    
    return job_listings