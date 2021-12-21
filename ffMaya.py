import maya.cmds as create

#-create lights: ambient & directional
create.directionalLight( n='light_directional', intensity=2.5 )
create.ambientLight( n='light_ambient', intensity=2.5 )
create.sets( 'light_directional', 'light_ambient', n='set_lights' )

#-create polyDisc underneath model
create.polyDisc()
create.rename( 'pDisc1', 'sm_disc' )
create.sets( 'sm_disc', n='set_discLighting' )

#-edit lighting positions
create.directionalLight( 'light_directional', e=True, pos=(15,35,0) )
create.directionalLight( 'light_directional', e=True, rot=(-80,0,0) )
create.ambientLight( 'light_ambient', e=True, pos=(-10,35,0) )

#-edit discLighting material, scale, position
lambert = create.createNode( 'lambert' )
create.select('set_discLighting')
create.scale( 5, 0, 5 )

create.select('set_discLighting')
create.move( 0, -1, 0 )

#-add selected lights to new layer
create.select( 'set_lights' )
create.createDisplayLayer( name='layer_lighting' )

#-set material for discLighting
create.hyperShade( assign = lambert )
