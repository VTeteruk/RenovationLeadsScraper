import logging
from os import path

# Base urls setting
BASE_GOOGLE_MAPS_URL = "https://www.google.com/maps/search/"
BASE_GOV_URL = "https://find-and-update.company-information.service.gov.uk/"

# Searching settings
DEFAULT_COMPANIES_FIELD = "Renovation"
DEFAULT_CITY = "London"
DIRECT_URL = "https://www.google.com/maps/search/renovation/@54.5739916,-1.2589921,11z?entry=ttu"

# File names setting
FILE_PATH_FOR_CSV = path.join("results", "renovation_leads.csv")
FILE_PATH_FOR_XLSX = path.join("results", "renovation_leads.xlsx")

# Driver settings
HEADLESS = True
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

# Starter settings
INPUT_MODE = True
PYTHON_LISTS_IN_RESULTS = False
TRIES_FOR_WEBSITE = 3


# Logging settings
def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s - %(message)s"
    )
