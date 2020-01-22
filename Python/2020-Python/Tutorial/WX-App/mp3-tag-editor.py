import eyed3
import glob
import wx

class Mp3Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.row_obj_dict = {}

        self.list_ctrl = wx.ListCtrl(
            self, size=(-1, 100),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.list_ctrl.InsertColumn(0, 'Artist', width=140)
        self.list_ctrl.InsertColumn(1, 'Album', width=140)
        self.list_ctrl.InsertColumn(2, 'Title', width=200)

        mp3s = glob.glob(folder_path + '/*.mp3')
        mp3_objects = []
        index = 0
        for mp3 in mp3s:
            mp3_object = eyed3.load(mp3)
            self.list_ctrl.InsertItem(index, 
            mp3_object.tag.artist)
            self.list_ctrl.SetItem(index, 1, 
            mp3_object.tag.album)
            self.list_ctrl.SetItem(index, 2, 
            mp3_object.tag.title)
            mp3_objects.append(mp3_object)
            self.row_obj_dict[index] = mp3_object
            index += 1

        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        edit_button = wx.Button(self, label = 'Edit')
        main_sizer.Add(edit_button, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(main_sizer)
    
    def on_edit(self, event):
        print('in on_edit')

    def update_mp3_listing(self, folder_path):
        print(folder_path)

class Mp3Frame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
                        title = 'Mp3 Tag Editor')
        self.panel = Mp3Panel(self)
        self.Show()

    def create_menu(self):
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        open_folder_menu_item = file_menu.Append(
            wx.ID_ANY, 'Open Folder',
            'Open a folder with MP3s'
        )
        self.SetMenuBar(menu_bar)

    def on_open_folder(self, event):
        title = "Choose a directory:"
        dlg = wx.DirDialog(self, title,
                            style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.panel.update_mp3_listing(dlg.GetPath())
        dlg.Destroy()

if __name__ == '__main__':
    app = wx.App(False)
    frame = Mp3Frame()
    app.MainLoop()
