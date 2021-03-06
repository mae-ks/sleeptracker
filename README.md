
            >>> MAIN DSC <<<

This is a sleep-tracker application by Mae Kyaw San (@02983828). Everyday, program takes in data from user to calculate the
optimal amount of sleep user should have to feel rested. Program can show details for the week in a chart. I added testing command lines for
both Windows and Mac.

Can expect to:
    be asked for name if data is overwritten,
    print N/A if command is unavailable,
    exit if exit is entered,
    work in real-time using today's date and info,
    work over months and even years if data is never deleted,
    show a new chart every week,
    indicate if file is empty or not,
    not be able to enter new data for the day if already entered.

'sleeptrack.py' is the main program.
'emodays.txt', 'maindat.txt', and 'name.txt' are where all data collected is stored.
The rest are test files.

            >>> TESTING <<<

    > MANUAL TESTING <
You can change date and enter data for each day manually by going to 'sleeptrack.py' and entering whatever day into 
variable 'day_name'  on line 9.
    eg. day_name = 'Sun' #current_date.strftime('%a')

    > AUTOMATIC TESTING <
Run 'randomizer.py' first, so there will be data in the files.
python3 randomizer.py
If not, will say no files available or something along those lines.
Run multiple times for data over more weeks, and months.
Overwrite files to start fresh again.

Copy-paste the following to commandline to test the program.

>> to test calculation functions
python3 test.py

>> for chart
TYPE test_graph.txt | python sleeptrack.py
or
python3 sleeptrack.py < test_graph.txt

>> for getting recommendation
TYPE test_rec.txt | python sleeptrack.py
or
python3 sleeptrack.py < test_rec.txt

>> to overwrite all files
TYPE test_delete.txt | python sleeptrack.py
or
python3 sleeptrack.py < test_delete.txt
(remember to run 'randomizer.py' again before running more test!)
(if not will return something like no existing files.)

            >>> CREDITS <<<

(for getting abbreviated day name in real-time))
https://www.programiz.com/python-programming/datetime/strftime
(for markov chain)
https://docs.google.com/document/d/e/2PACX-1vRN67LoWEW2flUijuRvNKwec-9pDnX6mRtkO0yg3gixzA-8FBIsPGolm9CgJRcxLOzRk22xFE_3Thc_/pub
(getting file size/ using os import)
https://stackoverflow.com/questions/2104080/how-can-i-check-file-size-in-python
(getting real-time date)
https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
