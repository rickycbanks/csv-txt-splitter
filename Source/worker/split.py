import csv
import os
import sys

def split_csv(source_filepath, dest_path, result_filename_prefix, row_limit):
    if row_limit <= 0:
        raise Exception('row_limit must be > 0')
    filename,exten = os.path.splitext(source_filepath)
    with open(source_filepath, 'r') as source:
        reader = csv.reader(source)
        headers = next(reader)

        file_number = 0
        records_exist = True

        while records_exist:

            i = 0
            target_filename = f'{result_filename_prefix}_{file_number}{exten}'
            target_filepath = os.path.join(dest_path, target_filename)

            with open(target_filepath, 'w', newline='') as target:
                writer = csv.writer(target)

                while i < row_limit:
                    if i == 0:
                        writer.writerow(headers)

                    try:
                        writer.writerow(next(reader))
                        i += 1
                    except:
                        records_exist = False
                        break

            if i == 0:
                # we only wrote the header, so delete that file
                os.remove(target_filepath)

            file_number += 1
        return 'success'