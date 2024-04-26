from pyfunc.block import makeimage
from pyfunc.assetload import assetinit
assetinit()

im = makeimage([
	['iron_bar']
])

im.show()

im = makeimage([
	['iron_bar','air',{'type':'iron_bar','rotate':1}],
	[],
	[
		{'type':'actuator_head','rotate':0},
		{'type':'actuator_head','rotate':1},
		{'type':'actuator_head','rotate':2},
		{'type':'actuator_head','rotate':3},
	],
	[],
	[
		{'type':'frame','rotate':0},
		{'type':'frame','rotate':1},
		{'type':'frame','rotate':2},
		{'type':'actuator_head','rotate':3},
	],
	[],
	[
		{'type':'actuator','rotate':0},
		{'type':'actuator','rotate':1},
		{'type':'actuator','rotate':2},
		{'type':'actuator','rotate':3},
	],
	[],
	[
		{'type':'actuator','rotate':0},
		{'type':'wire','rotate':1},
		{'type':'wire_board','rotate':2},
		{'type':'actuator','rotate':3},
	],
	[],
	[
		{'type':'transistor','rotate':0},
		{'type':'transistor','rotate':1},
		{'type':'transistor','rotate':2},
		{'type':'transistor','rotate':3},
	],
	[],
	[
		{'type':'platform'},
		{'type':'platform'},
		{'type':'transistor'},
		{'type':'platform'},
	],
	[],
	[
		{'type':'iron_plate'},
		{'type':'wafer'},
		{'type':'iron_plate'},
		{'type':'iron_plate'},
	],
])

im.show()