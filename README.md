# Advent-of-Code #

## _fmkr.py_ file - the file-maker
The file-maker was created to automate the first steps of solving AoC puzzles without having to worry about saving input files, file-reading, creating basic functions etc.
### What does the file/directory maker do?
* Scrapes your AoC session cookie
* Downloads your puzzle data from AoC API and saves it
* Creates a base Python template and input directories based on given parameters (check How to use)

### How to use the file/directory maker?
* Move to a desired directory (cd _directory\_name_)
* If you want to create YYYY year's puzzle files or continue with next puzzle in that year:
  * Execute `py fmkr.py YYYY` (for example "_py fmkr.py 2015_")
* If you want to create or rewrite files from year YYYY and day DD:
  * Execute `py fmkr.py YYYY DD` (for example "_py fmkr.py 2015 7_")
* Open `day-DD.py` file and start coding!

Note: The AoC API is buggy and example inputs are sometimes some random values from puzzle's info file. You might have to input them manually.
