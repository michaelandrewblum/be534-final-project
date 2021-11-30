# be534-final-project
Final project for BE 534 Biosystems Analytics

The program should take a cvs data file which is the output from
a Campbell Scientific CS1000X datalogger and append it to the end
of an ongoing datafile.

The program should optionally, given the option "-d" or "--dashboard",
print out the averages for the sensor data just input.

To run use from the main folder:

```
python3 env_data/env_data.py new_data/test_data.csv -d
```
