import PySimpleGUI as sg
import os.path


"""
create nested list of elememts:
- represent vertical column of user interface
"""
file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20),
            key="-FILE LIST-"
        )
    ],
]

# show name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an image:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],  # display name of selected file
    [sg.Image(key="-IMAGE-")],  # display the Image
]

# define layout of the GUI
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),  # alias for VerticalSeparator()
        sg.Column(image_viewer_column),
    ]
]

# create window with title and layout
window = sg.Window("Image Viewer", layout)

# event loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # folder name was filled in, make a list of files
    # check event against FOLDER key
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # get list of files in folder
            file_list = os.listdir(folder)
        except Exception:
            file_list = []

        # filter the list to files excepted
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]

        # update file list in the window
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # file waschosen from list
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except Exception:
            pass

window.close()
