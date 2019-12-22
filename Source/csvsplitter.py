import csv
import os
import sys
import PySimpleGUI as sg

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


def complete():
    sg.Popup('Complete')
    main_diag()



#Actual Dialog
def main_diag():
    # Layout Window - look and feel
    sg.change_look_and_feel('lightGrey1')
    layout = [[sg.Text('Filename'),sg.Input(key='fname'), sg.FileBrowse()],
            [sg.Text('Destination Folder: '),sg.Input(key='fold'), sg.FolderBrowse()],
            [sg.Text('Rows per split: '),sg.Input('100000', key='split', )],
            [sg.Text('Prefix: '),sg.Input(key='pref')],
            [sg.OK('Split'),sg.Exit('Exit')] ]

    # Actually have Windows
    window = sg.Window('Ricky\'s Splitter', layout)
    event, values = window.read()
    SOURCE_FILEPATH = values['fname']
    DEST_PATH = values['fold']
    FILENAME_PREFIX = values['pref']
    ROW_LIMIT = int(values['split'])

    split_csv(SOURCE_FILEPATH, DEST_PATH, FILENAME_PREFIX, ROW_LIMIT)

    complete()

main_diag()

'''
import PySimpleGUI as sg

sg.change_look_and_feel('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(12,1), key='_OUTPUT_')],
          [sg.Input(key='_IN_')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:  # Event Loop
    event, values = window.read()       # can also be written as event, values = window()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        window['_OUTPUT_'].update(values['_IN_'])
        # above line can also be written without the update specified
        window['_OUTPUT_'](values['_IN_'])

window.close()
'''
