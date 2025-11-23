import csv

def extract_doi(doi_link: str) -> str:
    """Extract raw DOI from a full DOI link or return the DOI."""
    doi_link = doi_link.strip()
    if doi_link.startswith("http"):
        return doi_link.split("doi.org/")[-1]
    return doi_link


def save_to_csv(filename: str, rows: list):
    """Save results to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["DOI", "Abstract"])
        writer.writerows(rows)
