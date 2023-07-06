#!/usr/bin/env python3
import os
import datetime
import reports
import emails
import glob
def getDescriptions(path):
    with open(path) as desc:
        lines = desc.read().strip().splitlines()
    name_field = "name: {}".format(lines[0])
    weight_field = "weight: {}".format(lines[1])
    return "{}<br/>{}<br/><br/>".format(name_field, weight_field)

def main(paths):
    report_file = "/tmp/processed.pdf"
    report_body = ""
    for text in paths:
        report_body += getDescriptions(text)
    date = datetime.datetime.today()
    report_title = "Processed Update on {} {}, {}".format(
        date.strftime("%B"), date.day, date.year
    )
    print('generating reports')
    reports.generate_report(report_file, report_title, report_body)
    content = {
        "sender": "automation@example.com",
        "receiver": "{}@example.com".format(os.environ.get("USER")),
        "subject": "Upload Completed - Online Fruit Store",
        "body": "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        "attachment": report_file,
    }
    message = emails.generate_email(**content)
    emails.send_email(message)


paths = glob.glob("*/descriptions/*.txt", recursive=True)
if __name__ == "__main__":
    main(paths)
