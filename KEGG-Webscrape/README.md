# KEGG web scraping program.

The purpose of this program is to sift through the COMPOUND KEGG website and gather as much information as possible. The information
will be saved to an Excel sheet. I have estimated that there are about 25000 entries on KEGG to go through. Of these, only 18,000 are usable. 
Each webpage take about 1 min to scan. This not a technical limitation. This is because I fear getting my IP address blocked and do not want
to deal with that. Therefore I added a 45-75 second delay between each run. This number was selected as it was what Google could handle. 

## Instructions

Hit run. That all that is needed.

## Dependencies

You will need:
requests
re
bs4
random
pandas
time

bs4 is the engine that makes this work.


## Installation

Use conda and/or pip to install dependencies.

## Usage

Uses BeautifulSoup to search webpages and scrape the information.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
