# Advent-of-Code #

## _fmkr.py_ file - the file-maker
The file-maker was created to ease the first steps of solving AoC puzzles without having to worry about file-reading, creating functions etc.
### What does the file/directory maker do?
* Depending on the given parameter:

   * If a directory with a given name already exists, it adds new files (_day-xx.py_ and _inputs/input-xx.txt_) to the given directory
   * If a directory doesn't exist, it creates it along with _inputs_ directory and files (_day-01.py_, _inputs/input-00.txt_ and _inputs/input-01.txt_)

* `inputs/input-00.txt` is a file to keep the example input for the current day in. All _.py_ files are connected to it
* `day-xx.py` includes a basic Python setup for AoC with functions prepared to return results of both tasks, automatical file reading, printing the output etc.

### How to use the file/directory maker?
* Move to a desired directory (cd _directory\_name_)
* Execute command `py fmkr.py directory_name` (for example "_py fmkr.py 2015_"), which will create a working directory named 2015 or a file with a number incremented from the previous one if the directory already exists
* You can add an optional argument like `py fmkr.py directory_name day_number` (for example "_py fmkr.py 2015 6_"), which will create the working directory (or just _.py_ and _.txt_ files if the directory already exists)
* Add your puzzle input to the _input-xx.txt_ files and start coding!