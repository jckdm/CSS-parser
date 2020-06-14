# CSS parser

``` bash
$ python3 main.py
Do you have more than 1 .css file? (yes/no):
Path to directory / Path to .css file:
Read [    ].css
Do you have more than 1 .html file? (yes/no):
Path to directory / Path to .html file:
Read [    ].html
Identified [ ] unique classes and [ ] unique IDs.

Unused class:  .[    ] : file1.css,  line 0, 00
Unused ID:     #[    ] : file2.css, line 000, 0

May I remove these unused rules and output new .css files? (yes/no):
Cleaned [    ].css
```

0. prompts user for path to/filename of singular or multiple .css file(s)
1. prompts user for path to/filename of singular or multiple .html file(s)
2. parses files
3. prints unused classes and IDs, corresponding files and line numbers
4. [BETA] re-writes css files without unused classes and IDs

TODO:

0. handle :hover, :focus, etc.
1. handle re-writing multiple files
2. thoroughly edge case re-writing stage
