import os
import re
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.freezpak.com"
ASSETS_PREFIX = "https://cdn.prod.website-files.com/660eb6abe8cde3bea6a9c111/"
ASSETS_LOCAL = "/static/assets/660eb6abe8cde3bea6a9c111/"

# pages to skip
SKIP = {"/", "/about"}

session = requests.Session()
resp = session.get(BASE_URL)
resp.raise_for_status()
html = resp.text
soup = BeautifulSoup(html, "html.parser")
urls = set()
for tag in soup.find_all("a", href=True):
    href = tag['href']
    if href.startswith('/') and not href.startswith('//'):
        urls.add(href.split('#')[0])

# also parse about page for extra links
resp = session.get(BASE_URL + "/about")
resp.raise_for_status()
html = resp.text
soup = BeautifulSoup(html, "html.parser")
for tag in soup.find_all("a", href=True):
    href = tag['href']
    if href.startswith('/') and not href.startswith('//'):
        urls.add(href.split('#')[0])

urls -= SKIP

os.makedirs('templates', exist_ok=True)

for path in sorted(urls):
    url = BASE_URL + path
    r = session.get(url)
    if r.status_code != 200:
        print('Failed to fetch', url, r.status_code)
        continue
    data = r.text
    # replace asset domain
    data = data.replace(ASSETS_PREFIX, ASSETS_LOCAL)
    # replace full URL links
    data = re.sub(r'https?://www\.freezpak\.com', '', data)
    # parse html attrs, head, body
    doc = BeautifulSoup(data, 'html.parser')
    html_tag = doc.find('html')
    html_attrs = ' '.join(f'{k}="{v}"' for k, v in html_tag.attrs.items())
    head = html_tag.find('head')
    body = html_tag.find('body')
    content = ''.join(str(c) for c in body.contents)
    head_html = head.decode_contents()

    # build template
    template = f"""{{% extends 'base.html' %}}

{{% block html_attrs %}}
    {html_attrs}
{{% endblock %}}

{{% block head %}}
{head_html}
{{% endblock %}}

{{% block content %}}
    {{% include 'components/header.html' %}}
{content}
    {{% include 'components/footer.html' %}}
{{% endblock %}}
"""
    # compute filename
    if path.endswith('/'):
        name = path.strip('/').replace('/', '_') or 'index'
    else:
        name = path.strip('/').replace('/', '_')
    file_path = os.path.join('templates', f"{name}.html")
    with open(file_path, 'w') as f:
        f.write(template)
    print('Saved', file_path)
