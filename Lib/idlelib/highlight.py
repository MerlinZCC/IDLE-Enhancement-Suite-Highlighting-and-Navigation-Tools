"""Format all or a selected region (line slice) of text.

Region formatting options: paragraph, comment block, indent, deindent,
comment, uncomment, tabify, and untabify.

File renamed from paragraph.py with functions added from editor.py.
"""
import re
from tkinter.messagebox import askyesno
from tkinter.simpledialog import askinteger
from idlelib.config import idleConf

LIGHT_BLUE = "light blue"
LIGHT_RED = "#FF7F7F"
LIGHT_YELLOW = "#FFFFBF"
LIGHT_GREEN = "#88FF88"
LIGHT_ORANGE = "#FFBF80"
LIGHT_PURPLE = "#BF80FF"
UNHIGHLIGHT = "white"

class HighlightParagraph:
    def __init__(self, editwin):
        self.editwin = editwin
        self.editwin.text.config(selectbackground="grey")
        # Define all highlight colors here
    
        self.all_colors = [LIGHT_BLUE, LIGHT_RED, LIGHT_YELLOW, LIGHT_GREEN, LIGHT_ORANGE, LIGHT_PURPLE, UNHIGHLIGHT]
        # Convert color names to valid tag names (no # sign)
        self.all_tags = ['highlight_' + color.replace('#', '') for color in self.all_colors]
        
    def create_color_menu(self):
        self.editwin.menudict['edit'].add_cascade(label="Highlight Line Region", menu=self.editwin.color_menu)
        if self.editwin.allow_highlight:
            self.editwin.color_menu.add_command(label="blue", command=lambda: self.toggle_highlight(LIGHT_BLUE))
            self.editwin.color_menu.add_command(label="red", command=lambda: self.toggle_highlight(LIGHT_RED))
            self.editwin.color_menu.add_command(label="yellow", command=lambda: self.toggle_highlight(LIGHT_YELLOW))
            self.editwin.color_menu.add_command(label="green", command=lambda: self.toggle_highlight(LIGHT_GREEN))
            self.editwin.color_menu.add_command(label="orange", command=lambda: self.toggle_highlight(LIGHT_ORANGE))
            self.editwin.color_menu.add_command(label="purple", command=lambda: self.toggle_highlight(LIGHT_PURPLE))
            self.editwin.color_menu.add_command(label="Unhighlight", command=lambda: self.toggle_highlight(UNHIGHLIGHT))
        else:
            self.editwin.update_menu_state('edit', "Highlight Line Region", 'disabled')
        
    def create_next_highlight(self):
        if self.editwin.allow_highlight:
            self.editwin.text.bind("<<next-highlight>>", self.next_highlight)
        else:
            self.editwin.update_menu_state('edit', "Find Next Highlight", 'disabled')
    
    def next_highlight(self, event):
        print("hello")
        return 'break'
    
    def toggle_highlight(self, color):
        # get the selected region
        start, end = self.editwin.get_selection_indices()
        if start and end:
            # Create unique tag for each color
            color_tag = 'highlight_' + color.replace('#', '')
            
            # Iterate over all text in selected region
            index = start
            while index != end:
                # Get all tags at this index
                tags = self.editwin.text.tag_names(index)
                
                # If there is a highlight tag, remove it
                for tag in tags:
                    if tag in self.all_tags:
                        self.editwin.text.tag_remove(tag, index)
                
                # Move to next character
                index = self.editwin.text.index(f"{index}+1c")
            
            # Add the new highlight tag to the selected region
            self.editwin.text.tag_add(color_tag, start, end)
            self.editwin.text.tag_config(color_tag, background=color)
            if color == "white":
                self.editwin.text.tag_remove(color_tag, start, end)
            self.editwin.text.tag_raise("sel")
        return "break"




