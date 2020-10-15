# Save Image from CSV with Image Link

### I doubt anyone would be in my exact situation... but I'm making it open source anyway

### P.S. I am REALLY bad at naming, don't judge me

## Usage

- **Example** Usage
```python
from saveImagesFromcsv import SaveImgFromCSV

newInstance = SaveImgFromCSV('./csv/women-clothing-fashion.csv', delimiter=';')

newInstance.run('women-clothings')
```

`class SaveImgFromCSV` does your stuff for you...
`newInstance = SaveImgFromCSV()` creates a new object instance to variable `newInstance`, but needs parameters...
- csv_file_name: `required` : give the filepath / filename to your csv file
- delimiter: `optional`: default: `','`: the delimiter in csv file (the sample csv files are separated by `';'`)
  
## Methods
`getIndices()` => returns array of Indices matching the following...
- "MainImage"
- "Image2"
- "Image3"
- "Image4"
- "Image5"
- "Image6"
- "Image7"
- "Image8"

`run(directory, startIndex=0)` => does the saving for you
- directory: where the directory should be
- startIndex: where to start saving

## Dependencies
- urllib
- csv
- os (if I get the time to update this repo)
- ssl