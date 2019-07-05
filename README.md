# public
Script to sort those e-mails not registered on public servers. It should with acceptable quality yield only those e-mails which looks like business.

Input is two .csv files with no additional mark-up, commas etc, just one item per line.

emails_list.csv -- list of e-mails to sort.

domains_list.csv -- list of known public e-mail servers. You may add more domains there.

Output is list of e-mail not registered on servers from domains_list.csv.
By default is just printed to console but if I found some time -- saving output to file will be in my TODO.

To do a job put .py sript and both .csv files in the same folder. Than use any IDE (CodeRunner from Setapp will fit) to open .py scrip and run it. This is Python 3 code, it requires tweeking to get it running with earlier versions of Python.

In case something is not working @alexp may help. I did not asked him for help but he's the only one in company who I know use Python. Any case, scrip is primitive, so other backend people may help as well.

No dependencies used so installing extra modules not required.