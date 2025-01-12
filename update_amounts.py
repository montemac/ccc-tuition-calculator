# %%
import pprint

BUDGET_SHEET_PASTED = """
Bucket B
$819
$48.12
$144.37
$96.25
Bucket C
$910
$53.24
$159.73
$106.48
Bucket D
$1,000
$58.36
$175.08
$116.72
Bucket E
$1,091
$64.50
$193.51
$129.01
"""

# Parse copy-paste from budget into correct format
amounts = {"Base": {}, "EAM": {}, "PM1": {}, "PM2": {}}
current_bucket = ""
program_cycle = ["Base", "EAM", "PM1", "PM2"]
i = 0
for line in BUDGET_SHEET_PASTED.strip().splitlines():
    if line.startswith("Bucket "):
        current_bucket = line.split()[-1]
    else:
        cents = int(round(float(line.removeprefix("$").replace(",",""))*100))
        amounts[program_cycle[i]][current_bucket] = cents
        i = (i + 1)%len(program_cycle)

    
pp = pprint.PrettyPrinter(indent=4)

pp.pprint(amounts)

