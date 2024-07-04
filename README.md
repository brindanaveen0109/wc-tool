### CCWC - CREATING MY OWN WORD COUNT TOOL

I have built my own version of the  Linux command line  tool : wc
I have taken the input text file as test.txt from https://codingchallenges.fyi/challenges/challenge-wc/

It works similar to the wc command used in Linux Command line with the similar options as listed below:

ccwc - prints the total charcater, number of words, and number of lines in the text file
ccwc -l : Prints the total number of lines
ccwc -w : Prints the total number of words
ccwc -c : Prints the toral number of charcters

### How to give the commands and where to give the commands.
Open the command line in your Ubuntu or WSL in windows.
Move to path where the python code ccwc.py is stored.
After creation of the python file, make the file executable using the shell using the following command:

```terminal
chmod +x filename.py
chmod +x ccwc.py
```

and then  run the following commands to get the contents of the file.

### Commands

The commands can be used by giving the file name as mentioned below:
1. To print out all the options(words, lines and characters):
   
```terminal
$ ./ccwc.py test.txt
```
<br>

#### Options available
1. -l : Displays the number of lines in the input file.
```terminal
$./ccwc.py -l test.txt
```
<br>

2. -w : Displays the number of words in the input file.
```terminal
$.\ccwc.py -w test.txt
```
<br>

3. -c : Displays the number of characters in the input file.
```terminal
$.\ccwc.py -c test.txt
```
<br>


