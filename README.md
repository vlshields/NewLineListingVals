# ChangeSpotter - OSCM
> This tool is part of my Open Source Clinical Central Monitoring Tool-Set Project.


## Installation (only available on Windows)
---------------------
Clone the repo:

```sh
git clone https://github.com/vlshields/NewLineListingVals
```
install requirements

```sh
pip install -r requirements.txt
```
run
```sh
python new_listing_vals.py
```
* or install the exe here [https://github.com/vlshields/NewLineListingVals/releases/tag/v1.0.0]. Your machine will tell you that it may contain harmful files, this is a false positive. Do not run as administrator! 

## Example Use Case
---------------------------------
Sites often enter data in EDC systems later than the respective study documents indicate that they should. This is often refered to as data latency, and it happens at every Clinical Trial.
However, some cases are more egregious than others.\ Lets create a mock Phase III clinical trial as an example:

### Dormira
**Protocol Title:** <br>
A Phase 3, Randomized, Stratified, Observer-Blind, 
Placebo-Controlled Study to Evaluate the Efficacy, and Safety of Insomnistop in 
Adults with insomnia.<br>
Protocol Number: inso7385<br>
Sponsor Name: Dormira

| Primary endpoints| Clinical Significance Threshold|  
|--------------|-----------|
|  Epworth Sleepiness Score (ESS)|2 points|
| and Functional Outcomes of Sleep Questionaire| 1 Point| 



Theres no mention of specific prohibited medications in the mock protocol, but there are known medications that could effect the studies primary endpoints. Sometimes patients taking such medications
should have not met inc/exc in the first place. Other times, the study team my have to render their results unusable.

Lets take Concamitant medications for example. Perhaps a study coordinator neglected to enter a medication in the patients folder, maliciciously or not. Sure DM could have programatic flags for this in
EDC,but in a trial with over 1000 patients screened, I think a way to pull automated reports should be available for CMs and DMs.

First lets make some fake data:

```sh
# you can modify the fake data however you wish in this file
python fake_listing_data.py
```
We pull this first report in november. Take a look at patient 715
<img width="365" alt="Screenshot 2023-11-20 031700" src="https://github.com/vlshields/NewLineListingVals/assets/25306963/6d7782f0-7f83-4ffa-9ca4-da8b9f8e7e6d">

We pull another listing in december, take a look at this patient again: 

<img width="334" alt="Screenshot 2023-11-20 031108" src="https://github.com/vlshields/NewLineListingVals/assets/25306963/4d11345f-5af9-4f7d-8bda-df1129bbf53c">

We can see that there were medications entered later for this patient. We would have to go to EDC to look at exactly who, why, and when this data was entered. In a large clinical trial, I tool like this could help us spot
these misshaps more quickly.

## How to use
-------------------------
1. Open the program in any directory besides C:\User\<yourname>. I suggests making a new folder on your desktop or documents and keeping it there. You can run it the pythonic way or simple click on the .exe file.
2. Click and drag your **first** line listing after prompted. Then drag the listing you want to see changes on.
3. THe program should generate an excel file called NewVals{DateofExecustion}.xlsx. Under the indicator columnm, uncheck both to see the old (some become deleted or updated) and new values.

   <img width="500" alt="image" src="https://github.com/vlshields/NewLineListingVals/assets/25306963/c0ddfa89-3991-4807-9b36-d944916f2d97">

Some data get removed as well:

<img width="463" alt="image" src="https://github.com/vlshields/NewLineListingVals/assets/25306963/d01d81a2-0910-4535-96ac-ce61e9b0efd5">



## Development setup

Make sure to have excel installed or libreoffice installed. I have not tested it in google sheets but if someone does please let me know how it works!

## LICENSE 
----------------

Copyright 2023 Vincent Shields<br>
FPA

## Release History

* 0.0.1
    * Work in progress

