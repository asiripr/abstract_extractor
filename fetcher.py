import requests

def fetch_abstract(doi: str) -> str:
    """Fetch abstract using Crossref API."""
    url = f"https://api.crossref.org/works/{doi}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        abstract = data["message"].get("abstract", None)

        if abstract:
            abstract = (
                abstract.replace("<jats:p>", "")
                        .replace("</jats:p>", "")
                        .strip()
            )
            return abstract
        else:
            return "N/A"

    except Exception as e:
        return f"Error: {str(e)}"
