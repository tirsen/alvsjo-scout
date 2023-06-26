import csv
import sys

scoutnet_emails_file = sys.argv[1]
groups_emails_file = sys.argv[2]

scoutnet_emails = set()
with open(scoutnet_emails_file) as f:
    for row in csv.DictReader(f):
        scoutnet_emails.add(row['Primär e-postadress'].strip().lower())
        # for e in row['Kontakt-e-post'].split(','):
        #     if e:
        #         scoutnet_emails.add(e.strip().lower())
        scoutnet_emails.add(row['Anhörig 2 e-post'].strip().lower())

groups_emails = set()
with open(groups_emails_file) as f:
    for row in csv.DictReader(f):
        groups_emails.add(row['Member Email'].strip().lower())

if '' in scoutnet_emails:
    scoutnet_emails.remove('')
if '' in groups_emails:
    groups_emails.remove('')

print("in groups:")
print("==========================")
for email in sorted(groups_emails):
    print(email)

print("")
print("in groups not in scoutnet:")
print("(these will disappear if we synk)")
print("==========================")
for email in (groups_emails - scoutnet_emails):
    print(email)

print("")
print("in scoutnet not in groups:")
print("==========================")
for email in (scoutnet_emails - groups_emails):
    print(email)
