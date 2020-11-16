# Wires the selected node down to the closest node to the mouse cursor
#
# Eg. Shift + W key

def getContextType():
    pane = kwargs['pane']
    contextname = pane.pwd().childTypeCategory().name()

def getCurrentNetworkEditorPane():
    editors = [pane for pane in hou.ui.paneTabs() if isinstance(pane, hou.NetworkEditor) and pane.isCurrentTab()]
    return editors[-1]

cursorPosition = getCurrentNetworkEditorPane().cursorPosition()
children = getCurrentNetworkEditorPane().pwd().children()
childrenList = list(children)

infinity = 9999
wireTo = getCurrentNetworkEditorPane().pwd()

for child in childrenList:
    if child in hou.selectedNodes():
        childrenList.remove(child)

for child in childrenList:
    length = (cursorPosition - child.position()).length()
    if length < infinity:
        infinity = length
        wireTo = child

i=0
for node in hou.selectedNodes():
    wireTo.setNextInput(node, i, False)
    i += 1
