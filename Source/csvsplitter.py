#import csv
#import os
#import sys
import worker.split as isp
import PySimpleGUI as sg

# Define Initial Theme and Get themes
theme = 'lightGrey1'

## Set Layout of Main Window
main_layout = [[sg.Text('Filename'),sg.Input(key='fname'), sg.FileBrowse()],
    [sg.Text('Destination Folder: '),sg.Input(key='fold'), sg.FolderBrowse()],
    [sg.Text('Rows per split: '),sg.Input('100000', key='split', )],
    [sg.Text('Suffix: '),sg.Input(key='suff')],
    [sg.OK('Split'),sg.Exit('Exit')] ]


## Layout of popup window
popup_layout = [sg.Text('Splitting Files'),
    [sg.ProgressBar('?',)]]


sg.change_look_and_feel(theme)

## Draw main windows
window = sg.Window('CSV | TXT | File Splitter',layout=main_layout)

## Event Loop Main Window
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Split':
        runsplit=isp.split_csv(values['fname'], values['fold'], values['suff'], int(values['split']))
        if runsplit:
            sg.popup_ok(title='Success')

window.close()

'''class diag:
    def __init__(self):
        self.layout = []
        window = None

    def main(self):
        sg.change_look_and_feel('lightGrey1')
        self.layout = [[sg.Text('Filename'),sg.Input(key='fname'), sg.FileBrowse()],
            [sg.Text('Destination Folder: '),sg.Input(key='fold'), sg.FolderBrowse()],
            [sg.Text('Rows per split: '),sg.Input('100000', key='split', )],
            [sg.Text('Suffix: '),sg.Input(key='suff')],
            [sg.OK('Split'),sg.Exit('Exit')] ]
        print('main')
        return self.layout

    def main(self):
        self.layout = [[sg.Text('Splitting the file.')]
            [sg.l]
        ]
        

    def render(self):
        print('render')
        lay = self.layout
        window = sg.Window('Ricky\'s Splitter', lay) 
        event, values = window.read()

isp.split_csv(SOURCE_FILEPATH, DEST_PATH, FILENAME_SUFFIX, ROW_LIMIT)'''







'''
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

'''




'''def complete():
    sg.Popup('Complete')
    main_diag()

    isp.split_csv(SOURCE_FILEPATH, DEST_PATH, FILENAME_PREFIX, ROW_LIMIT)

    complete()
'''