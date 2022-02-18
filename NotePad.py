import sublime
import sublime_plugin


class NotePadMakeCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        window = sublime.active_window()
        view = window.active_view()

        window.set_sidebar_visible(False)
        window.set_tabs_visible(False)
        window.set_status_bar_visible(False)
        window.set_minimap_visible(False)

        view.settings().set('gutter',False)
        view.settings().set("toggle_status_bar",False)
        window.run_command('hide_panel')

class NotePadNewCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        sublime.run_command("new_window")
        sublime.run_command('note_pad_make')


class NotePadRevertCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        window = sublime.active_window()
        view = window.active_view()

        window.set_sidebar_visible(True)
        window.set_tabs_visible(True)
        window.set_status_bar_visible(True)
        window.set_minimap_visible(True)

        view.settings().set('gutter',True)
        view.settings().set("toggle_status_bar",True)
