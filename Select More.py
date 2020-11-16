# Add to selection the closest node (in current context) to the mouse cursor
#
# Eg. Shift + S edit

def getContextType():
    pane = kwargs['pane']
    contextname = pane.pwd().childTypeCategory().name()

def getCurrentNetworkEditorPane():
    editors = [pane for pane in hou.ui.paneTabs() if isinstance(pane, hou.NetworkEditor) and pane.isCurrentTab()]
    return editors[-1]

cursorPosition = getCurrentNetworkEditorPane().cursorPosition()
children = getCurrentNetworkEditorPane().pwd().children()

infinity = 9999
selectMe = getCurrentNetworkEditorPane().pwd()

for child in children:
    length = (cursorPosition - child.position()).length()
    if length < infinity:
        infinity = length
        selectMe = child

selectMe.setSelected(True, False)
