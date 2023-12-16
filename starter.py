from google_maps_parser import GoogleMapsParser
from owners_parser import OwnersParser

if __name__ == "__main__":
    google_maps_parser = GoogleMapsParser()
    data = google_maps_parser.main(
        "https://www.google.com/maps/search/"
        "renovation/@52.583251,-0.2907134,12.05z?entry=ttu"
    )
    owners_parser = OwnersParser()
    owners_parser.find_owners(data)

    google_maps_parser.save_data_to_excel(data, "renovation_leads")
    google_maps_parser.save_data_to_csv(data, "renovation_leads")
    google_maps_parser.destroy()
