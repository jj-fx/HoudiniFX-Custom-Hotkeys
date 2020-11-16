# Selects the closest node (in current context) to the mouse cursor
#
# Eg. S key

def get_current_networ_editor_pane():
    editors = [pane for pane in hou.ui.paneTabs() if isinstance(pane, hou.NetworkEditor) and pane.isCurrentTab()]
    return editors[-1]

    
def get_closest_node(cursor_position, nodes_in_context):
    infinity = 9999
    selectMe = ""
    for node in nodes_in_context:
        length = (cursor_position - node.position()).length()
        if length < infinity:
            infinity = length
            selectMe = node
    return selectMe
 
    
pane = get_current_networ_editor_pane()
cursorPosition = pane.cursorPosition()
children = pane.pwd().children()

selectMe = get_closest_node(cursor_position = cursorPosition, nodes_in_context = children)

selectMe.setSelected(True, True)
