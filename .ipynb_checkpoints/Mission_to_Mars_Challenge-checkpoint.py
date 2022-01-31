{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10c4ba83",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter and BeautifulSoup\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82d85643",
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4317201",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://redplanetscience.com/'\n",
    "browser.visit(url)\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "176a6910",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('div.list_text')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c02e3937",
   "metadata": {},
   "outputs": [],
   "source": [
    "slide_elem.find('div', class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10f5e027",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the parent element to find the first `a` tag and save it as `news_title`\n",
    "news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d4183304",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "59d10259",
   "metadata": {},
   "source": [
    "### Featured Images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d58e171",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bd1452f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7670b24e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bfc61614",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find the relative image url\n",
    "img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b205fab6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the base URL to create an absolute URL\n",
    "img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e83b2b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "df.columns=['description', 'Mars', 'Earth']\n",
    "df.set_index('description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e96c14d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76421ba2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Use browser to visit the URL \n",
    "url = 'https://marshemispheres.com/'\n",
    "\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1728be60",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "res_soup = soup(html, 'html.parser')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d03c5b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "hemisphere_image_urls = []\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "906e1bb6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6307ad18",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    "links = browser.find_by_css(\"a.product-item img\")\n",
    "for x in range (len(links)):\n",
    "    hemisphere = {}\n",
    "    browser.find_by_css(\"a.product-item img\")[x].click()\n",
    "    link_to_img = browser.find_by_css('h3')\n",
    "    link_to_img.click()\n",
    "    my_list = browser.links.find_by_text(\"Sample\").first\n",
    "    hemisphere[\"image_url\"] = my_list[\"href\"]\n",
    "    \n",
    "    hemisphere[\"title\"] = browser.find_by_css(\"h2.title\").text\n",
    "    \n",
    "    #sample_link = res_soup.find()\n",
    "    #img_url_par = res_soup.find('img', class_='wide-image')\n",
    "    #img_url = f'https://marshemispheres.com/{img_url_par}'\n",
    "    #title = res_soup.find('h2', class_='title').text\n",
    "    hemisphere_image_urls.append(hemisphere)\n",
    "   \n",
    "    browser.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bbce2008",
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "676ec462",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4. Print the list that holds the dictionary of each image url and title.\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb668eb1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8bf7eee3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
