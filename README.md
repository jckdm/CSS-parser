# CSS parser

``` bash
$ python3 main.py
Do you have more than 1 .css file? (yes/no):
Path to directory / Path to .css file:
Read file1.css
Read file2.css
Do you have more than 1 .html file? (yes/no):
Path to directory / Path to .html file:
Read file1.html

Identified [ ] unique classes and [ ] unique IDs.

Undefined class: .[    ] : file1.html
Undefined ID:    #[    ] : file1.html

Unused class:  .[    ] : file1.css,  line 0, 00
Unused ID:     #[    ] : file2.css, line 000, 0

May I remove these unused rules and output new .css files? (yes/no):
Wrote file1-clean.css
Wrote file2-clean.css
```

0. prompts user for path to/filename of singular or multiple .css file(s)
1. prompts user for path to/filename of singular or multiple .html file(s)
2. prints undefined classes and IDs, corresponding files
3. prints unused classes and IDs, corresponding files and line numbers
4. re-writes .css files without unused classes and IDs

TODO:

0. thoroughly edgecase re-writing stage
1. fix comments disappearing in media queries?
2. comment your code, dummy
