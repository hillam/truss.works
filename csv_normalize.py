#!/usr/bin/python
import csv
import sys
from datetime import timedelta
from dateutil.parser import parse

# Convert "HH:MM:SS.MS" to decimal seconds
def convert_duration(duration):
    hours, minutes, seconds = duration.split(':')
    total_seconds = float(seconds)
    total_seconds += float(minutes) * 60
    total_seconds += float(hours) * 3600
    return total_seconds
# end convert_duration

# Decode row values to utf-8 and replace invalid characters with the unicode
# replacement character
def decode_row(row):
    for value in row:
        value.decode('utf-8', 'replace')
# end decode_row

# Convert the given name to uppercase
def normalize_name(name):
    return name.upper()
# end normalize_name

# Convert given timestamp from Pacific to Eastern return ISO-8601 format
def normalize_timestamp(timestamp):
    timestamp = parse(timestamp)
    # Convert from EST to PST
    timestamp = timestamp + timedelta(hours=3)
    # Return ISO-8601 format
    return timestamp.isoformat()
# end normalize_timestamp

# Front-pad the given zipcode with 0's to ensure 5-char zip
def normalize_zipcode(zipcode):
    return format(int(zipcode), '05')
# end normalize_zipcode

# Normalize the CSV from stdin and write it to stdout.
def main():
    csv_reader = csv.reader(sys.stdin)
    csv_writer = csv.writer(sys.stdout)

    # Add the header row to the output
    normalized_csv = [csv_reader.next()]

    # Iterate over the input rows
    for row in csv_reader:
        try:
            decode_row(row)

            # Timestamp
            row[0] = normalize_timestamp(row[0])

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

            normalized_csv.append(row)
        except:
            # If any part of the row can't be processed, skip it
            print >>sys.stderr, "error processing row - skipping..."
    # end row in csv_reader

    csv_writer.writerows(normalized_csv)
# end main

main()
