# Rolodex

An application that takes entries of personal information in multiple formats and normalizes each entry into a standard JSON format.

# Input

The program will be read an input file (/data/data.in) of n lines. Each line should consist of “entry” information that includes first name, last name, a USA-style phone number, color, and a 5-digit ZIP code.

These are the three different acceptable entry/line input formats: <br />
Lastname, Firstname, (703)-742-0996, Blue, 10013 <br />
Firstname Lastname, Red, 11237, 703 955 0373 <br />
Firstname, Lastname, 10013, 646 111 0101, Green 

Some of these input lines might not follow the above formats and should not be normalized or interfere with the normalization of subsequent valid entries. An entry is invalid if its phone number doesn't contain 10 digits, the ZIP code doesn't contain 5 digits, or the firstname/lastname do not conform to the above formats. 

# Output
The application will write a formatted JSON object that adheres to the valid input formats to '/data/result.out'. The JSON representation will be indented with 2 spaces and the keys will be sorted alphabetically.

The JSON object will contain 2 key value pairs. The 'entries' key will contain a list of successfully normalized entries, and the 'errors' key will contain a list of the line numbers that do not conform to any of the above input formats.

The “entries” list will be sorted in ascending alphabetical order by (last name, first name).

# Sample

input: <br />
Daniel T., Zhang, 61820, 373 111 2345, grey <br />
Derrick, Rose, (633)-777-9999, pink, 413245312 <br />
John Doe, space grey, 60654, 012 234 4567 <br />
kfhalksdhfkahds <br />
54345 3454 <br />

output: <br />
{ <br />
  "entries": [ <br />
    { <br />
      "color": "yellow", <br />
      "firstname": "Daniel T.", <br />
      "lastname": "Zhang", <br />
      "phonenumber": "373-111-2345", <br />
      "zipcode": "61820" <br />
    }, <br />
    { <br />
      "color": "space grey", <br />
      "firstname": "John", <br />
      "lastname": "Doe", <br />
      "phonenumber": "012-234-4567", <br />
      "zipcode": "60654" <br />
    }  <br />
  ], <br />
  "errors": [ <br />
    1, <br />
    3, <br />
    4 <br />
  ] <br />
} <br />

## How to Use
1. Have Python 2.7.x installed or activate the virtualenv (```source venv/bin/activate```)
2. If the result.out file already exists in the data folder, then delete it first before running
3. Run ``python run.py``
4. Open the result.out file in the data folder
