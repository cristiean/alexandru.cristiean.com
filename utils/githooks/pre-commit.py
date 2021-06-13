import re
import sys

from datetime import datetime

try:
    # Get stamp
    datetime_string = "{:%d %B %Y, %H:%M}".format(datetime.now())
    
    # Get files to be stamped
    output = sys.stdin.read() # reads input from pipe
    html_filenames = output.strip().split('\n') # list of staged html filenames

    # Stamp
    for html_filename in html_filenames:
        try:
            with open(html_filename,) as html_file:
                html = html_file.read()
            
            with open(html_filename, 'w') as html_file:   
                print(f"Datetimestamping with datetime {datetime_string}: {html_filename}")
                html_file.write(re.sub(r"<datetimestamp>.*</datetimestamp>", f"<datetimestamp>{datetime_string}</datetimestamp>", html))
        
        except Exception as FileNotFoundError:
            print(f"Datetimestamping: {html_filename} does not exist anymore (may be deleted?)")

except Exception as e:
    print("Datetimestamping ERROR! Failed due to: ", e)
    print(35*'-',' ABORT ', 35*'-')
    exit