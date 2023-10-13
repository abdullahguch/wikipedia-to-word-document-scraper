# Wikipedia Scraper

## Overview

This Python script allows you to scrape the content of a Wikipedia page and create a Word document with the scraped content. It uses the Wikipedia API to fetch the page content. Currently it can only scrape the text but NOT images. And it is only possible to scrape the English content.

## Prerequisites

- Python 3.x
- Required Python packages (install using `pip install wikipedia-api python-docx`)

## How to Use

1. Clone or download the script.

2. Open a terminal or command prompt.

3. Navigate to the script's directory.

4. Run the script using the command:

```bash
python script_name.py
```

5. Enter the Wikip  edia page title when prompted.

6. The script will fetch the Wikipedia page content and create a Word document.

## Customization

You can customize the script by modifying the `scrape_wikipedia` function to extract additional information from the Wikipedia page if needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [python-docx](https://python-docx.readthedocs.io/en/latest/)
- [wikipedia-api](https://github.com/Wikipedia-API/Wikipedia-API)
