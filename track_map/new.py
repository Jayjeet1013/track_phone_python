

import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Replace with your OpenCage API Key
OpenCage_API_KEY = "your api key"

# Replace with the phone number you want to track
phone_number = "your number with country code"

# Parse the phone number
parsed_number = phonenumbers.parse(phone_number, None)

# Check if the phone number is valid
if not phonenumbers.is_valid_number(parsed_number):
    print("Invalid phone number")
else:
    # Get the location information for the phone number
    location_info = geocoder.description_for_number(parsed_number, "en")
    print("Location:", location_info)

    # Get the carrier/service provider information for the phone number
    service_provider = carrier.name_for_number(parsed_number, "en")
    print("Service Provider:", service_provider)

    # Initialize the OpenCageGeocode API
    geocoder = OpenCageGeocode(OpenCage_API_KEY)

    # Use the location information to query for latitude and longitude
    results = geocoder.geocode(location_info)

    if results and len(results):
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        print("Latitude:", lat)
        print("Longitude:", lng)

        # Create a map and add a marker
        map_location = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location_info).add_to(map_location)

        # Save the map as an HTML file
        map_location.save("mylocation.html")
    else:
        print("Location not found")
