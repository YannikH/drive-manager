import os

sourcePath = "D:/P/src"
destinationPath = "D:/P/dest"

def setSourcePath(val):
  print("setting val", val)
  sourcePath = val
  print(sourcePath)

def setDestinationPath(val):
  print("setting val", val)
  destinationPath = val
  print(destinationPath)

def getSourcePath():
  return sourcePath

def getDestinationPath():
  return destinationPath

def list_subfolders(directory):
    subfolders = []
    for root, dirs, files in os.walk(directory):
        if 'config.cpp' in files:
            subfolders.append(root)
    return subfolders

def symlinkFolder(source, destination):
    target_dir = os.path.dirname(destination)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    if not os.path.exists(source):
        print(f"Error: '{source}' does not exist.")
        return
    if os.path.exists(destination):
        print(f"Error: '{destination}' already exists.")
        return
    try:
        os.symlink(source, destination)
        print(f"Success: '{destination}' symlinked to '{source}'.")
    except Exception as e:
        print(f"Error: {e}")

def unlinkFolder(destination):
  if os.path.islink(destination):
    os.unlink(destination)
    print(f"Symbolic link {destination} has been removed.")
  else:
      print(f"{destination} is not a symbolic link.")

def isLinkedFolder(destination):
  return os.path.islink(destination)