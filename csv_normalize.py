#!/usr/bin/python
import csv
import sys

def convert_duration(duration):
    return duration
# end convert_duration

def normalize_address(address):
    return address
# end normalize_address

def normalize_name(name):
    return name
# end normalize_name

def normalize_notes(notes):
    return notes
# end normalize_notes

def normalize_timestamp(timestamp):
    return timestamp
# end normalize_timestamp

def normalize_zipcode(zipcode):
    return zipcode
# end normalize_zipcode

def main():
    csv_reader = csv.reader(sys.stdin)
    csv_writer = csv.writer(sys.stdout)

    # Add the header row to the output
    normalized_csv = [csv_reader.next()]

    # Iterate over the input rows
    for row in csv_reader:
        # Timestamp
        row[0] = normalize_timestamp(row[0])

        # Address
        row[1] = normalize_address(row[1])

        # Zipcode
        row[2] = normalize_zipcode(row[2])

        # Name
        row[3] = normalize_name(row[3])

        # Foo and Bar Durations
        foo_duration = convert_duration(row[4])
        bar_duration = convert_duration(row[5])
        row[4] = str(foo_duration)
        row[5] = str(bar_duration)

        # Total Duration
        total_duration = foo_duration + bar_duration
        row[6] = str(total_duration)

        # Notes
        row[7] = normalize_notes(row[7])

        normalized_csv.append(row)
    # end row in csv_reader

    csv_writer.writerows(normalized_csv)
# end main

main()
