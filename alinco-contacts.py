import argparse
import csv

# Regions/countries mirrored from checkbox-selection code in https://www.radioid.net/generator/contacts_continents

REGION_EUROPE = 'eu'
REGION_NORTH_AMERICA = 'na'
REGION_SOUTH_AMERICA = 'sa'
REGION_AFRICA = 'af'
REGION_ASIA_PACIFIC = 'ap'
REGION_AUSTRALIA_OCEANIA = 'au'

EUROPE_COUNTRIES = {
    "Aaland Islands",
    "Albania",
    "Andorra",
    "Armenia",
    "Austria",
    "Belarus",
    "Belgium",
    "Bosnia and Hercegovina",
    "Bulgaria",
    "Corsica",
    "Croatia",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Faroe Islands",
    "Finland",
    "France",
    "Georgia",
    "Germany",
    "Gibraltar",
    "Greece",
    "Greenland",
    "Hungary",
    "Iceland",
    "Ireland",
    "Italy",
    "Kosovo",
    "Latvia",
    "Liechtenstein",
    "Lithuania",
    "Luxemburg",
    "Macedonia",
    "Malta",
    "Moldova",
    "Monaco",
    "Montenegro",
    "Netherlands",
    "Norway",
    "Poland",
    "Portugal",
    "Romania",
    "Russia",
    "San Marino",
    "Serbia",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "Switzerland",
    "Turkey",
    "Ukraine",
    "United Kingdom"
}

NORTH_AMERICA_COUNTRIES = [
    "Anguilla",
    "Antigua and Barbuda",
    "Aruba",
    "Bahamas",
    "Barbados",
    "Belize",
    "Bermuda",
    "British Virgin Islands",
    "Canada",
    "Cayman Islands",
    "Costa Rica",
    "Cuba",
    "Curacao",
    "Dominica",
    "Dominican Republic",
    "El Salvador",
    "Grenada",
    "Guadeloupe",
    "Guatemala",
    "Haiti",
    "Honduras",
    "Jamaica",
    "Martinique",
    "Mexico",
    "Montserrat",
    "Nicaragua",
    "Panama",
    "Puerto Rico",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "St. Pierre and Miquelon",
    "St. Vincent and Grenada",
    "Trinidad and Tobago",
    "U.S. Virgin Islands",
    "United States"
]

SOUTH_AMERICA_COUNTRIES = [
    "Argentina Republic",
    "Bolivia",
    "Brazil",
    "Chile",
    "Colombia",
    "Ecuador",
    "French Guiana",
    "Guyana",
    "Paraguay",
    "Peru",
    "Suriname",
    "Uruguay",
    "Venezuela"
]

AFRICA_COUNTRIES = [
    "Algeria",
    "Angola",
    "Ascension Island",
    "Benin",
    "Botswana",
    "Burkina Faso",
    "Burundi",
    "Cameroon",
    "Cape Verde",
    "Central African Republic",
    "Chad",
    "Comoros",
    "Democratic Republic of Congo",
    "Djibouti",
    "Egypt",
    "Equatorial Guinea",
    "Eritrea",
    "Ethiopia",
    "Gabon",
    "Gambia",
    "Ghana",
    "Guinea",
    "Guinea-Bissau",
    "Ivory Coast",
    "Kenya",
    "Lesotho",
    "Liberia",
    "Libya",
    "Madagascar",
    "Malawi",
    "Mali",
    "Mauretania",
    "Mauritius",
    "Morocco",
    "Mozambique",
    "Namibia",
    "Niger",
    "Nigeria",
    "Reunion",
    "Rwanda",
    "Sao Tome and Principe",
    "Senegal",
    "Seychelles",
    "Sierra Leone",
    "Somalia",
    "South Africa",
    "Sudan",
    "Swasiland",
    "Tanzania",
    "Togo",
    "Tunisia",
    "Uganda",
    "Zambia",
    "Zimbabwe"
]

ASIA_PACIFIC_COUNTRIES = [
    "Afghanistan",
    "Azerbaijan",
    "Bahrain",
    "Bangladesh",
    "Bhutan",
    "Brunei Darussalam",
    "Burma",
    "Cambodia",
    "China",
    "Guam",
    "Hong Kong",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Israel",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Korea Republic of",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Lebanon",
    "Macao",
    "Malaysia",
    "Maldives",
    "Micronesia",
    "Mongolia",
    "Nepal",
    "Oman",
    "Pakistan",
    "Philippines",
    "Qatar",
    "Saudi Arabia",
    "Singapore",
    "Sri Lanka",
    "Syrian Arab Republic",
    "Taiwan",
    "Tajikistan",
    "Thailand",
    "Timor-Leste",
    "Turkmenistan",
    "United Arab Emirates",
    "Uzbekistan",
    "Viet Nam",
    "Yemen"
]

AUSTRALIA_OCEANIA_COUNTRIES = [
    "American Samoa",
    "Australia",
    "Cook Islands",
    "Fiji",
    "French Polynesia",
    "Kiribati",
    "New Caledonia",
    "New Zealand",
    "Palau",
    "Papua New Guinea",
    "Samoa",
    "Solomon Islands",
    "Tonga",
    "Vanuatu"
]

COUNTRIES_FOR_REGION = {
    REGION_EUROPE: EUROPE_COUNTRIES,
    REGION_NORTH_AMERICA: NORTH_AMERICA_COUNTRIES,
    REGION_SOUTH_AMERICA: SOUTH_AMERICA_COUNTRIES,
    REGION_AFRICA: AFRICA_COUNTRIES,
    REGION_ASIA_PACIFIC: ASIA_PACIFIC_COUNTRIES,
    REGION_AUSTRALIA_OCEANIA: AUSTRALIA_OCEANIA_COUNTRIES
}

ALL_REGIONS = [REGION_EUROPE,
               REGION_NORTH_AMERICA,
               REGION_SOUTH_AMERICA,
               REGION_AFRICA,
               REGION_ASIA_PACIFIC,
               REGION_AUSTRALIA_OCEANIA]


def parse_cmd_args():
    parser = argparse.ArgumentParser(description='Convert RadioID.net CSV files to Alinco DJ-MD5 CSV contact files.')
    parser.add_argument('infile', help='input CSV file from RadioID.net (no stdin)')
    parser.add_argument('outfile', help='output CSV file for Alinco DJ-MD5 (no stdout)')
    parser.add_argument('--regions', help='set of countries to include', choices=ALL_REGIONS, nargs='*')
    parsed_args = parser.parse_args()
    selected_regions = parsed_args.regions or []
    selected_countries = {c for region in selected_regions for c in COUNTRIES_FOR_REGION[region]}
    return parsed_args.infile, parsed_args.outfile, selected_countries


# RadioID.net CSV format:
# RADIO_ID,CALLSIGN,FIRST_NAME,LAST_NAME,CITY,STATE,COUNTRY
# 1023001,VE3THW,Wayne,Edward,Toronto,Ontario,Canada

# DJ-MD5 contact CSV format:
# "No.","Radio ID","Callsign","Name","City","State","Country","Remarks","Call Type","Call Alert"
# "3","1023001","VE3THW","Wayne","Toronto","Ontario","Canada","","Private Call","None"
RADIOID_FIELDS = ['RADIO_ID', 'CALLSIGN', 'FIRST_NAME', 'LAST_NAME', 'CITY', 'STATE', 'COUNTRY']
ALINCO_FIELDS = ['No.', 'Radio ID', 'Callsign', 'Name', 'City', 'State', 'Country', 'Remarks', 'Call Type',
                 'Call Alert']

in_file, out_file, countries = parse_cmd_args()
with open(in_file, 'r', encoding='UTF-8', newline='') as in_file:
    with open(out_file, 'w', encoding='UTF-8', newline='') as out_file:
        reader = csv.DictReader(in_file, RADIOID_FIELDS)
        writer = csv.DictWriter(out_file, ALINCO_FIELDS, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        output_row_idx = 0
        for contact in reader:
            if countries and contact['COUNTRY'] not in countries:
                continue
            output_row_idx += 1
            out_dict = {'No.': output_row_idx,
                        'Radio ID': contact['RADIO_ID'],
                        'Callsign': contact['CALLSIGN'],
                        'Name': f'{contact["FIRST_NAME"]} {contact["LAST_NAME"]}',
                        'City': contact['CITY'],
                        'State': contact['STATE'],
                        'Country': contact['COUNTRY'],
                        'Remarks': '',
                        'Call Type': 'Private Call',
                        'Call Alert': 'None'
                        }
            writer.writerow(out_dict)
