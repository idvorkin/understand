#!python3

import sys
import typer
import html2text
from bs4 import BeautifulSoup

app = typer.Typer(
    help="Extracts page title and article content from HTML and converts it to Markdown."
)


@app.command()
def convert(
    file: typer.FileText = typer.Option(
        None,
        "--file",
        "-f",
        help="Path to the HTML file to process. Reads from stdin if not specified.",
    ),
):
    """
    Extracts the page title and article text content from an HTML file and converts it to Markdown.
    """

    # Read HTML content from file or stdin
    html_content = file.read() if file else sys.stdin.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract the page title
    page_title = (
        soup.title.get_text(strip=True).replace("(Interconnected)", "").strip()
        if soup.title
        else "No Title Found"
    )

    # Extract the article content
    article_html = "\n".join(str(p) for p in soup.select("article#post p"))

    # Convert HTML to Markdown-like text
    markdown_text = html2text.html2text(article_html)

    # Output title and content to stdout
    print(f"# {page_title}\n\n{markdown_text}")


if __name__ == "__main__":
    app()
