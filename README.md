# ImpactDB Experimental Data Upload Demo
This repository contains code that demonstrates how experimental data can be uploaded to ImpactDB's firestore.

The user needs to send a POST request to https://us-central1-impact-db.cloudfunctions.net/uploadExperimentalData.

The request body needs to have three keys:
species: Examples include 'yarrowia', 'rhodosporidium', 'saccharomyces', 'lipomyces', 'pichia', or 'clostridium'
slug: The last part of the ImpactDB url for the paper to update. For example: 'hydrogen-production-by-immobilized-cells-of-clostridium-intestinale-strain-urnw-using-alginate-beads'
experimentalData: A string representation of JSON experimental data. The format of this string must be based on test_experimental_data.json.

### A brief example of the code:
```
url = 'https://us-central1-impact-db.cloudfunctions.net/uploadExperimentalData'

data = {
    'species': 'clostridium',
    'slug': 'hydrogen-production-by-immobilized-cells-of-clostridium-intestinale-strain-urnw-using-alginate-beads',
    'experimentalData': experimental_data,
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(data), headers=headers)
```

### Notes on the experimental_data object:
The type of experimental_data is required to be a python list of dictionaries. Each dictionary must contain the following keys: 
```
species	strain	engineeredStrain	parentStrain	product	titer	averageRate	maximumRate	yield	volume	vessel	substrate1	substrateConc1	substrate2	substrateConc2	media	time	oxygenLevel	nitrogenLevel	pH	temperature	geneIds	geneNames	knockedOutGenes	overexpressedGenes	heterologousGenes	promoters	integrationSites	originSpecies	optimizedCodons	directedEvolution	sourceEmail	geneticNotes	bioprocessNotes
```

Each experimental result is required to have a non-blank value for the following fields: 
```
parentStrain	product	titer vessel	substrate1	substrateConc1 time	oxygenLevel	nitrogenLevel
```

experimental_data can be defined in an excel file, a json file, or manually in python code. See the demo notebook for examples of all three methods.

### To run this project locally:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
