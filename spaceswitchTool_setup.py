'''
Nathaniel H.
04/29/2021
Quick setup for complex space switching tool
'''


import pymel.core as pm

def phaseOne():

    ctrl = pm.ls(sl = True)

    pm.select(cl=1)
    pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=1.46609e-05, nr=(0, 1, 0))
    pm.move(6, 0, 0, r=1, os=1, wd=1)
    pm.xform(ro = (0,0,90))
    pm.group(n='ltHand_NULL', world = True) 
    pm.circle(c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=1.46609e-05, nr=(0, 1, 0))
    pm.move(-6, 0, 0, r=1, os=1, wd=1)
    pm.xform(ro = (0,0,90))
    pm.group(n='rtHand_NULL', world = True)
    pm.spaceLocator(p=(0, 0, 0))
    pm.select('nurbsCircle1','nurbsCircle2','locator1')

phaseOne()
print 'Phase One Check'


def nrhRename():
    
    oldName = pm.ls(sl=True)
    
    for old in oldName:
        newName = 'Item' + '_#'
        pm.rename(old, newName)

def coffeeBreak():
    sel = pm.ls(selection = True)
    for obj in sel:
        pm.xform(obj, centerPivots = True)   
    pm.delete(constructionHistory=True)  
    pm.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    print "Object's Cleaned"

nrhRename()
coffeeBreak()
print "Task One Completed Successfully."


def item1_blue():

    pm.select('Item_1')   
    
    pm.addAttr(longName='switcher', k=1, at='enum', enumName='world:oppositeHand')
    
    item1_color = pm.ls(sl=True)
    
    for n in item1_color:
        n.overrideEnabled.set(1)
        n.overrideRGBColors.set(1)
        n.overrideColorRGB.set(0, 0, 3)
        
    pm.rename('Item_1', 'ltHand_ctrl')


def item2_red():

    pm.select('Item_2')   
    
    pm.addAttr(longName='switcher', k=1, at='enum', enumName='world:oppositeHand')
    
    item2_color = pm.ls(sl=True)
    
    for n in item2_color:
        n.overrideEnabled.set(1)
        n.overrideRGBColors.set(1)
        n.overrideColorRGB.set(1, 0, 0)
        
    pm.rename('Item_2', 'rtHand_ctrl')


item1_blue()
item2_red()
pm.select('Item_3')
pm.rename('Item_3', 'worldLocator')
pm.select(d = True)

print 'Colors changed.'

def setSpacez():
    
    nrhSpacegrp = pm.group(n = 'spaces_grp', world = True)
    pm.select(d = True)
    nrhLtspace = pm.group(n = 'ltHand_space', world = True)
    pm.select(d = True)
    nrhRtspace = pm.group(n = 'rtHand_space', world= True)
    pm.select(d = True)
    nrhWorldloc = pm.group(n = 'worldLocator_space', world= True)
    pm.select(d = True)
    pm.parent(nrhLtspace, nrhRtspace, nrhWorldloc, nrhSpacegrp)
    
    pm.parentConstraint('rtHand_ctrl', nrhRtspace, mo = False)
    pm.parentConstraint('ltHand_ctrl', nrhLtspace, mo = False)
    pm.parentConstraint('worldLocator', nrhWorldloc, mo = False)
    
setSpacez()

def nrhctrlGrps():
    pm.select('ltHand_ctrl')
    pm.group(n='lt_ctrlSpace_grp')
    pm.select('rtHand_ctrl')
    pm.group(n='rt_ctrlSpace_grp')
    pm.select(d=True)
    
    pm.group(n= 'rtHand_space_ltHand_inbetween', world = True)
    pm.select(d = True)
    pm.group(n= 'worldLocator_space_ltHand_inbetween', world = True)
    pm.parent('rtHand_space_ltHand_inbetween', 'worldLocator_space_ltHand_inbetween', 'ltHand_NULL')
    pm.select(d=True)
    
    pm.group(n= 'ltHand_space_rtHand_inbetween', world = True)
    pm.select(d = True)
    pm.group(n= 'worldLocator_space_rtHand_inbetween', world = True)
    pm.parent('ltHand_space_rtHand_inbetween', 'worldLocator_space_rtHand_inbetween', 'rtHand_NULL')
    pm.select(d = True)
    
    #creating offsets for specific control groups to avoid snap to
    pm.group(n= 'worldLocator_space_ltHand_offset', world = True)
    pm.select(d = True)
    pm.group(n= 'worldLocator_space_rtHand_offset', world = True)
    pm.parent('worldLocator_space_ltHand_offset', 'worldLocator_space_rtHand_offset', 'worldLocator_space')
    pm.select(d = True)
    
    pm.group(n= 'ltHand_space_rtHand_offset', world = True)
    pm.parent('ltHand_space_rtHand_offset', 'ltHand_space')
    pm.select(d = True)
    
    pm.group(n= 'rtHand_space_ltHand_offset', world = True)
    pm.parent('rtHand_space_ltHand_offset', 'rtHand_space')
    pm.select(d = True)

nrhctrlGrps()
print "phase 2 complete"

def nrhctrlHookup():
    pm.parentConstraint('worldLocator_space_ltHand_offset', 'worldLocator_space_ltHand_inbetween', mo = False)
    pm.parentConstraint('worldLocator_space_rtHand_offset', 'worldLocator_space_rtHand_inbetween', mo = False)
    pm.parentConstraint('ltHand_space_rtHand_offset', 'ltHand_space_rtHand_inbetween', mo = False)
    pm.parentConstraint('rtHand_space_ltHand_offset', 'rtHand_space_ltHand_inbetween', mo = False)
    
    #contraining inbetweens to the space group
    pm.parentConstraint('ltHand_space_rtHand_inbetween', 'worldLocator_space_rtHand_inbetween', 'rt_ctrlSpace_grp', mo = False)
    pm.parentConstraint('rtHand_space_ltHand_inbetween', 'worldLocator_space_ltHand_inbetween', 'lt_ctrlSpace_grp', mo = False)
    
    print "it works"
    
nrhctrlHookup()

def nrhRightsetup():
    #creating a condition node for each space
    pm.shadingNode('condition', asUtility=1, n='rtHand_world_node')
    pm.shadingNode('condition', asUtility=1, n='rtHand_ltHand_node')
    
    #set node attributes to reflect enum
    pm.setAttr("rtHand_world_node.colorIfTrueR", 1)
    pm.setAttr("rtHand_world_node.colorIfFalseR", 0)
    pm.setAttr("rtHand_world_node.colorIfFalseB", 0)
    pm.setAttr("rtHand_world_node.colorIfTrueG", 0)
    pm.setAttr("rtHand_world_node.colorIfFalseG", 10)
    
    pm.setAttr("rtHand_ltHand_node.colorIfTrueR", 1)
    pm.setAttr("rtHand_ltHand_node.secondTerm", 1)
    pm.setAttr("rtHand_ltHand_node.colorIfFalseR", 0)
    pm.setAttr("rtHand_ltHand_node.colorIfFalseB", 0)
    pm.setAttr("rtHand_ltHand_node.colorIfTrueG", 0)
    pm.setAttr("rtHand_ltHand_node.colorIfFalseG", 10)
    
    pm.connectAttr('rtHand_world_node.outColorR', 'rt_ctrlSpace_grp_parentConstraint1.worldLocator_space_rtHand_inbetweenW1', f=1)
    pm.connectAttr('rtHand_ltHand_node.outColorR', 'rt_ctrlSpace_grp_parentConstraint1.ltHand_space_rtHand_inbetweenW0', f=1)
    pm.connectAttr('rtHand_world_node.outColorG', 'worldLocator_space_rtHand_inbetween.nodeState', f=1)
    pm.connectAttr('rtHand_ltHand_node.outColorG', 'ltHand_space_rtHand_inbetween.nodeState', f=1)
    pm.connectAttr('rtHand_ctrl.switcher', 'rtHand_world_node.firstTerm', f=1)
    pm.connectAttr('rtHand_ctrl.switcher', 'rtHand_ltHand_node.firstTerm', f=1)
    
    
     
def nrhLeftsetup():
    #Reapeating mirror of previous function for the left side
    pm.shadingNode('condition', asUtility=1, n='ltHand_world_node')
    pm.shadingNode('condition', asUtility=1, n='ltHand_rtHand_node')
    
    
    pm.setAttr("ltHand_world_node.colorIfTrueR", 1)
    pm.setAttr("ltHand_world_node.colorIfFalseR", 0)
    pm.setAttr("ltHand_world_node.colorIfFalseB", 0)
    pm.setAttr("ltHand_world_node.colorIfTrueG", 0)
    pm.setAttr("ltHand_world_node.colorIfFalseG", 10)
    
    pm.setAttr("ltHand_rtHand_node.colorIfTrueR", 1)
    pm.setAttr("ltHand_rtHand_node.secondTerm", 1)
    pm.setAttr("ltHand_rtHand_node.colorIfFalseR", 0)
    pm.setAttr("ltHand_rtHand_node.colorIfFalseB", 0)
    pm.setAttr("ltHand_rtHand_node.colorIfTrueG", 0)
    pm.setAttr("ltHand_rtHand_node.colorIfFalseG", 10)
    
    pm.connectAttr('ltHand_world_node.outColorR', 'lt_ctrlSpace_grp_parentConstraint1.worldLocator_space_ltHand_inbetweenW1', f=1)
    pm.connectAttr('ltHand_rtHand_node.outColorR', 'lt_ctrlSpace_grp_parentConstraint1.rtHand_space_ltHand_inbetweenW0', f=1)
    pm.connectAttr('ltHand_world_node.outColorG', 'worldLocator_space_ltHand_inbetween.nodeState', f=1)
    pm.connectAttr('ltHand_rtHand_node.outColorG', 'rtHand_space_ltHand_inbetween.nodeState', f=1)
    pm.connectAttr('ltHand_ctrl.switcher', 'ltHand_world_node.firstTerm', f=1)
    pm.connectAttr('ltHand_ctrl.switcher', 'ltHand_rtHand_node.firstTerm', f=1)

nrhRightsetup()
print "Right Hand Completed"
nrhLeftsetup()
print "Left Hand Completed"

def nrhCleanitup():
    
    pm.select('rtHand_ctrl')
    pm.move(-6, 0, 0, r=1, os=1, wd=1)
    pm.select('ltHand_ctrl')
    pm.move(6, 0, 0, r=1, os=1, wd=1)
    
    print "Object's Cleaned"

nrhCleanitup()

pm.select('ltHand_ctrl', 'rtHand_ctrl')
coffeeBreak()

print 'Operation Complete'
