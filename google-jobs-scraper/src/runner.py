thonimport json
from extractors.google_jobs_parser import parse_google_jobs
from outputs.exporters import export_to_json
from config.settings import PROXY, COOKIES

def main():
    # Example search parameters
    search_text = "developer in seattle jobs in the last 3 days"
    job_data = parse_google_jobs(search_text, proxy=PROXY, cookies=COOKIES)

    # Export the data
    export_to_json(job_data, 'data/sample_output.json')

if __name__ == "__main__":
    main()