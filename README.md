# ChangeSpotter - OSCM
> This tool is meant to make spotting changes in line listings easy. It is part of my Open Source Central Monitoring Project.
> Often times, Data are updated in EDC very quickly. Rather than monitors going through EDC and looking for the changes, this program will spot it for them.
> It is often not as simple as looking at dates, because sometimes values are changed retroactively. I will provide an example.


![](header.png)

## Installation only available on Windows

Clone the repo:

```sh
git clone https://github.com/vlshields/NewLineListingVals
```
install requirements

```sh
pip install -r requirements.txt
```

## Usage example

```sh
python new_height_vals.py
```
You will be prompted to enter the old listing first, then the new listing (the listing with the changes you are looking for). Make sure you pull them from the exact same source in EDC.
You will then be prompted to enter the columns you wish to match. Make sure to add spaces between.
## Development setup

Make sure to have excel installed. You will find a file called NewVals{todaysdate}.xlsx in your working directory. Go to the indicator column and deselect "Both"

## Release History

* 0.0.1
    * Work in progress

