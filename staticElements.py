from textual.widgets import Markdown

EXAMPLE_MARKDOWN = """\
# Error

You are currently not running this app in admin mode.

For this app to function, you need to start it in admin mode.

"""

def NoAdminWarning():
  return Markdown(EXAMPLE_MARKDOWN)