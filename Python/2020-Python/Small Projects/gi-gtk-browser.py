from gi.repository import Gtk
window = Gtk.Window()
Gtk.main()

def on_destroy(window):
    Gtk.main_quit()

window.connect("destroy",on_destroy)
window.add(webview)
window.set_title("Tarun's Browser")

Gtk.main()
