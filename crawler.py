import requests
from bs4 import BeautifulSoup


def crawl_page(url):
    """
    Crawl an educational webpage and extract:
    - Page title
    - Page description/content
    - URL
    """

    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/140.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=20,
            verify=True
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Get page title
        if soup.title and soup.title.string:
            title = soup.title.string.strip()
        else:
            title = "Unknown Title"

        # Remove unnecessary HTML elements
        for element in soup(
            ["script", "style", "noscript", "header", "footer"]
        ):
            element.decompose()

        # Extract visible text
        text = soup.get_text(" ", strip=True)

        # Keep useful amount of content
        description = text[:2000]

        return {
            "success": True,
            "title": title,
            "description": description,
            "url": url,
            "error": ""
        }

    except requests.exceptions.SSLError as error:

        return {
            "success": False,
            "title": "",
            "description": "",
            "url": url,
            "error": (
                "Secure HTTPS connection failed. "
                "Please try another educational URL."
            )
        }

    except requests.exceptions.Timeout:

        return {
            "success": False,
            "title": "",
            "description": "",
            "url": url,
            "error": (
                "The website took too long to respond. "
                "Please try another URL."
            )
        }

    except requests.exceptions.ConnectionError:

        return {
            "success": False,
            "title": "",
            "description": "",
            "url": url,
            "error": (
                "Could not connect to the website. "
                "Please check the URL or internet connection."
            )
        }

    except requests.exceptions.RequestException as error:

        return {
            "success": False,
            "title": "",
            "description": "",
            "url": url,
            "error": f"Website request failed: {error}"
        }

    except Exception as error:

        return {
            "success": False,
            "title": "",
            "description": "",
            "url": url,
            "error": f"Unexpected error: {error}"
        }