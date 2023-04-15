import os
import sys

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Header, Footer, Static, Checkbox, TextLog, Input

from folderUtil import list_subfolders, getSourcePath, getDestinationPath, symlinkFolder, unlinkFolder, isLinkedFolder, setSourcePath, setDestinationPath
from util import isAdmin
from staticElements import NoAdminWarning

def checkboxChanged(box):
  checked = box.value
  path = str(box.label)
  print(path)
  print(getSourcePath())
  linkOrigin = getSourcePath() + path
  linkDestination = getDestinationPath() + path
  if checked:
    symlinkFolder(linkOrigin, linkDestination)
  else:
    unlinkFolder(linkDestination)
  

def createCheckbox(folder, path):
  print(path)
  relPath = folder.replace(path, "")
  checkBox = Checkbox(relPath)
  checkBox.value = isLinkedFolder(getDestinationPath() + relPath)
  return checkBox

class DriveList(Container):
  """A list of drives."""
  def compose(self) -> ComposeResult:
      """idk man."""
      path = getSourcePath()
      yield Button("Refresh list (must be used after changing source or destination paths)")
      for folder in list_subfolders(path):
        yield createCheckbox(folder, path)


  def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
    checkboxChanged(event.checkbox)

class PathEditor(Container):
  def compose(self) -> ComposeResult:
    self.id = "pathEditor"
    yield Input(placeholder="Source", id="source", value=getSourcePath())
    yield Input(placeholder="Destination", id="destination", value=getDestinationPath())

  def on_input_changed(self, event):
    input = event.input
    print(input.value, input.id)
    if input.id == "source":
      setSourcePath(input.value)
    if input.id == "destination":
      print("setting destination")
      setDestinationPath(input.value)



class DriveMgrApp(App):
  CSS_PATH = "app.css"

  def compose(self) -> ComposeResult:
    """Called to add widgets to the app."""
    yield Header()
    yield Footer()
    if isAdmin():
      yield Container(PathEditor(), DriveList(), id="driveList")
    else:
      yield NoAdminWarning()
  

if __name__ == '__main__':
    app = DriveMgrApp()
    app.run()