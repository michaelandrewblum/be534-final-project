# be534-final-project

At my greenhouse we have a Campbell Scientific CS1000X datalogger that
keeps track of the environmental data.  The data files it produces 
normally are in .csv format without headers. The data files are
automatically named by the convention of "data_YYYY_MM_DD_TTTT.csv"
where "YYYY" is the four-digit year, "MM" is the two-digit month,
"DD" is the two-digit day, and "TTTT" is the time in 24-hour format.

I have to open them with Excel and copy them manually to the end of the
complete datafile that has all data points going back to the beginning
of the project.

I wanted to write a program that would eliminate that manual copy and
paste step and update the datafile automatically.

Requirements of the Program:

* Be given one or more files in the format "data_YYYY_MM_DD_TTTT.csv"
* If more than one file is given to sort those files by date
* Copy each file in chronological order to the end of the datafile
* Move the input files to another folder after they've been input
* Print to stdout which files have been input
* Print to stdout where the output file is
* Calculate average values for certain data points in each input file
* Display these average values when requested
* Have an option to not move the files if not desired (usually desired)
* Have an option to not copy the files in case only want averages

The program will take one or more .csv files generally placed in the new_data directory and will copy them to the master datafile generally found at output/data.csv.

The program will print to stdout when any file is input and will specify which output file was copied to.

If given the -o, --outfile option you can specify a different output datafile if desired.

If given the -d, --dashboard flag you will see a set of relevant data points and the averages of those data points for each input file.

If given the -r, --remain flag the files will be copied to the datafile, but the input files will not be moved.  Be careful with this as in the future you may think you haven't input them when you have.

If given the -n, --nottofile flag you will not copy the input files to the output data file.  This is meant to be used with -d in case you just want to see the dashboard without copying the files.

I wrote a program reset/reset.py to put the data files back into the new_data folder and reinitialize the output/data.csv file.  Because the program moves files it can't be run twice in a row without moving the files back (unless you use the -r flag).  Running this reset program is a quick way to get everything back to the start so the program can be run again.

The project folder has a Makefile setup with the following commands:

* "make test" will run pytest on "tests/test.py"
* "make data" will run env_data/env_data.py on all files in the new_data directory
* "make data_d" will run env_data/env_data.py with the -d flag
* "make data_dr" will run env_data/env_data.py with the -dr flags
* "make data_drn" will run env_data/env_data.py with the -drn flags
* "make reset" will run reset/reset.py which will reset the project folder.
