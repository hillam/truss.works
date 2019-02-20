#!/usr/bin/python
import csv
import sys
from datetime import timedelta
from dateutil.parser import parse

# Convert "HH:MM:SS.MS" to
def convert_duration(duration):
    hours, minutes, seconds = duration.split(':')
    total_seconds = float(seconds)
    total_seconds += float(minutes) * 60
    total_seconds += float(hours) * 3600
    return total_seconds
# end convert_duration

def normalize_name(name):
    return name.upper()
# end normalize_name

def normalize_timestamp(timestamp):
    timestamp = parse(timestamp)
    # Convert from EST to PST
    timestamp = timestamp - timedelta(hours=3)
    # Return ISO-8601 format
    return timestamp.isoformat()
# end normalize_timestamp

def normalize_zipcode(zipcode):
    # Front-pad with 0's to ensure 5-char zip
    return format(int(zipcode), '05')
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
    # end row in csv_reader

    csv_writer.writerows(normalized_csv)
# end main

main()
