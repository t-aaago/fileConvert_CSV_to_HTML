import pandas as pd
from sys import argv

new_name = argv[2]

file = pd.read_csv(argv[1])
file.to_html(new_name + '.html')