from fetcher import fetch_abstract
from utils import extract_doi, save_to_csv

def main():
    print("Enter DOI links (max 10). Enter an empty line to finish.\n")

    user_dois = []
    while len(user_dois) < 10:
        val = input(f"DOI {len(user_dois)+1}: ").strip()
        if val == "":
            break
        user_dois.append(val)

    if not user_dois:
        print("No DOIs entered.")
        return

    results = []

    for doi_link in user_dois:
        doi = extract_doi(doi_link)
        print(f"Fetching abstract for DOI: {doi}")
        abstract = fetch_abstract(doi)
        results.append([doi, abstract])

    save_to_csv("abstracts.csv", results)
    print("\nSaved: abstracts.csv")


if __name__ == "__main__":
    main()
