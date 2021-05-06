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
print 'Raiden Wins'


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

    pm.group(n='spaces_grp', world = True)
    pm.select(d = True)
    pm.group(n = 'ltHand_space')
    pm.select(d = True)
    pm.group(n = 'rtHand_space')
    pm.select(d = True)
    pm.group(n = 'worldLocator_space')
    pm.select(d = True)
    
    pm.select('ltHand_space', 'rtHand_space','worldLocator_space')
    
    popIn = pm.ls(sl = True)
    
    pm.parent(popIn, 'spaces_grp')
    
    pm.parentConstraint('rtHand_ctrl', 'rtHand_space', mo = False)
    pm.parentConstraint('ltHand_ctrl', 'ltHand_space', mo = False)
    pm.parentConstraint('worldLocator', 'worldLocator_space', mo = False)
    
setSpacez()

print "phase 2 complete"
