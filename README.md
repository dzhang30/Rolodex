# Rolodex

An application that takes entries of personal information in multiple formats and normalizes each entry into a standard JSON format.

# Input

The program will be read an input file (/data/data.in) of n lines. Each line should consist of “entry” information that includes first name, last name, a USA-style phone number, color, and a 5-digit ZIP code.

These are the three different acceptable entry/line input formats:
Lastname, Firstname, (703)-742-0996, Blue, 10013
Firstname Lastname, Red, 11237, 703 955 0373
Firstname, Lastname, 10013, 646 111 0101, Green

Some of these input lines might not follow the above formats and should not be normalized or interfere with the normalization of subsequent valid entries. An entry is invalid if its phone number doesn't contain 10 digits, the ZIP code doesn't contain 5 digits, or the firstname/lastname do not conform to the above formats. 

# Output
The application will write a formatted JSON object that adheres to the valid input formats to '/data/result.out'. The JSON representation will be indented with 2 spaces and the keys will be sorted alphabetically.

The JSON object will contain 2 key value pairs. The 'entries' key will contain a list of successfully normalized entries, and the 'errors' key will contain a list of the line numbers that do not conform to any of the above input formats.

The “entries” list will be sorted in ascending alphabetical order by (last name, first name).

# Sample

input:
Daniel T., Zhang, 61820, 373 111 2345, grey
Derrick, Rose, (633)-777-9999, pink, 413245312
John Doe, space grey, 60654, 012 234 4567
kfhalksdhfkahds
54345 3454

output:
{
  "entries": [
    {
      "color": "yellow",
      "firstname": "Daniel T.",
      "lastname": "Zhang",
      "phonenumber": "373-111-2345",
      "zipcode": "61820"
    }, 
    {
      "color": "space grey",
      "firstname": "John",
      "lastname": "Doe",
      "phonenumber": "012-234-4567",
      "zipcode": "60654"
    } 
  ],
  "errors": [
    1,
    3,
    4
  ]
}

## How to Use
1. Have Python 2.7.x installed or activate the virtualenv (```source venv/bin/activate```)
2. If the result.out file already exists in the data folder, then delete it first before running
3. Run ```python run.py```
4. Open the result.out file in the data folder
