from gi.repository import Gtk
window = Gtk.Window()
Gtk.main()

def on_destroy(window):
    Gtk.main_quit()

window.set_title("Tarun's browser")
window.add(webview)
window.connect("destroy", on_destroy)
window.show_all()

Gtk.main()