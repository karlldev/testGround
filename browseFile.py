import tkinter
import PySimpleGUI as PSG

left_col = [[PSG.Text(r'Folder'), PSG.In(size = (25, 1), enable_events = True, key = r'-Folder-'), PSG.FolderBrowse()]]
layout = [[PSG.Column(left_col, element_justification = r'c')]]
window = PSG.Window(r'Multiple Format Image Viewer', layout, resizable = True)

while True:
    event, values = window.read()
    if event in (PSG.WIN_CLOSED, r'Exit'):
        break
    if event == r'-FOLDER-':
        folder = values[r'-FOLDER-']

