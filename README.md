# CSS-parser

``` bash
$ python3 main.py
Do you have more than 1 .css file? (yes/no):
Path to directory / Path to .css file:

Do you have more than 1 .html file? (yes/no):
Path to directory / Path to .html file:

Identified [ ] unique classes and [ ] unique IDs.

Unused class:  [    ] : file1.css
Unused ID:     [    ] : file2.css
```

0. prompts user for path to/filename of singular or multiple .css file(s)
1. prompts user for path to/filename of singular or multiple .html file(s)
2. parses files
3. prints names of unused classes and IDs and corresponding file

TODO:
0. print line number along with .css file name
