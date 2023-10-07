import wikipediaapi
from docx import Document
import os

def scrape_wikipedia(page_title):
    # Set a custom user-agent
    user_agent = 'My Wikipedia Scraper/1.0 (your@email.com)'

    # Create a Wikipedia API client with custom headers
    wiki_wiki = wikipediaapi.Wikipedia('en', headers={'User-Agent': user_agent})

    # Get the Wikipedia page content
    page_py = wiki_wiki.page(page_title)

    # Return the content text
    return page_py.text

def create_word_document(content, output_directory='output'):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Create a Word document
    doc = Document()

    # Add the Wikipedia content to the document
    doc.add_paragraph(content)

    # Save the document with the Wikipedia page title as the filename
    output_filename = os.path.join(output_directory, f"{page_title}.docx")
    doc.save(output_filename)
    print(f"Word document '{output_filename}' created successfully.")

if __name__ == "__main__":
    # Input: Wikipedia page title
    page_title = input("Enter the Wikipedia page title: ")

    # Scrape Wikipedia content
    content = scrape_wikipedia(page_title)

    # Create a Word document with the scraped content
    create_word_document(content)
