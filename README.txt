Learn scrapy from examples!

---------------SETUP---------------
python3 -m venv scrapy-env
source scrapy-env/bin/activate
pip3 install Scrapy

scrapy startproject tutorial
cd tutorial
scrapy crawl quotes

scrapy crawl quotes -o quotes.json
