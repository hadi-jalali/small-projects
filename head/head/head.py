# state file generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1205, 786]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [127.0, 124.0, 92.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [71.276001781279, 744.6407218586526, 211.51449747774737]
renderView1.CameraFocalPoint = [126.99999999999999, 124.0000000000001, 92.00000000000001]
renderView1.CameraViewUp = [0.07659000503133105, 0.19516326516807664, -0.9777756752232261]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 164.21936548409874
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1205, 786)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
headsqvti = XMLImageDataReader(registrationName='headsq.vti', FileName=['C:\\Program Files\\ParaView 5.9.0-Windows-Python3.8-msvc2017-64bit\\examples\\headsq.vti'])
headsqvti.PointArrayStatus = ['Scalars_']
headsqvti.TimeArray = 'None'

# create a new 'ExodusIIReader'
canex2 = ExodusIIReader(registrationName='can.ex2', FileName=['C:\\Program Files\\ParaView 5.9.0-Windows-Python3.8-msvc2017-64bit\\examples\\can.ex2'])
canex2.ElementVariables = []
canex2.PointVariables = []
canex2.GlobalVariables = []
canex2.NodeSetArrayStatus = []
canex2.SideSetArrayStatus = []
canex2.ElementBlocks = ['Unnamed block ID: 1', 'Unnamed block ID: 2']

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=headsqvti)
threshold1.Scalars = ['POINTS', 'Scalars_']
threshold1.ThresholdRange = [1515.15, 4054.05]

# create a new 'Histogram'
histogram1 = Histogram(registrationName='Histogram1', Input=threshold1)
histogram1.SelectInputArray = ['POINTS', 'Scalars_']
histogram1.CustomBinRanges = [1475.0, 4095.0]

# create a new 'Iso Volume'
isoVolume1 = IsoVolume(registrationName='IsoVolume1', Input=headsqvti)
isoVolume1.InputScalars = ['POINTS', 'Scalars_']
isoVolume1.ThresholdRange = [0.0, 4095.0]

# create a new 'PVD Reader'
fish_bonepvd = PVDReader(registrationName='fish_bone.pvd', FileName='C:\\Users\\hadi1\\OneDrive\\Desktop\\CS year 3\\Semester 2\\CSC337-Data_Visualisation\\csc337_volvis_cw-master\\fish_bone.pvd')
fish_bonepvd.PointArrays = ['ImageFile', 'Normals']

# create a new 'PVD Reader'
bearpvd = PVDReader(registrationName='bear.pvd', FileName='C:\\Users\\hadi1\\OneDrive\\Desktop\\CS year 3\\Semester 2\\CSC337-Data_Visualisation\\csc337_volvis_cw-master\\bear.pvd')
bearpvd.PointArrays = ['ImageFile']

# create a new 'PVD Reader'
fishpvd = PVDReader(registrationName='fish.pvd', FileName='C:\\Users\\hadi1\\OneDrive\\Desktop\\CS year 3\\Semester 2\\CSC337-Data_Visualisation\\csc337_volvis_cw-master\\fish.pvd')
fishpvd.PointArrays = ['ImageFile', 'Normals']

# create a new 'ExodusIIReader'
disk_out_refex2 = ExodusIIReader(registrationName='disk_out_ref.ex2', FileName=['C:\\Program Files\\ParaView 5.9.0-Windows-Python3.8-msvc2017-64bit\\examples\\disk_out_ref.ex2'])
disk_out_refex2.PointVariables = []
disk_out_refex2.NodeSetArrayStatus = []
disk_out_refex2.SideSetArrayStatus = []
disk_out_refex2.ElementBlocks = ['Unnamed block ID: 1']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from threshold1
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Scalars_'
scalars_LUT = GetColorTransferFunction('Scalars_')
scalars_LUT.RGBPoints = [0.0, 1.0, 1.0, 1.0, 240.88223249999967, 0.919118, 0.948529, 0.948529, 497.82300749999985, 0.832843, 0.893627, 0.893627, 754.7637825, 0.746569, 0.838725, 0.838725, 1011.7066049999996, 0.660294, 0.783824, 0.783824, 1268.6473799999999, 0.603922, 0.708987, 0.728922, 1525.5881550000001, 0.54902, 0.63317, 0.67402, 1782.5289299999997, 0.494118, 0.557353, 0.619118, 2039.470585425, 0.439216, 0.481536, 0.564216, 2296.4125275, 0.384314, 0.405719, 0.509314, 2553.3533025, 0.329412, 0.329902, 0.454412, 2810.2940775, 0.27451, 0.27451, 0.379085, 3067.2348524999998, 0.219608, 0.219608, 0.303268, 3324.1756275, 0.164706, 0.164706, 0.227451, 3581.11845, 0.109804, 0.109804, 0.151634, 3838.059225, 0.054902, 0.054902, 0.075817, 4095.0, 0.0, 0.0, 0.0]
scalars_LUT.ColorSpace = 'Lab'
scalars_LUT.NanColor = [1.0, 0.0, 0.0]
scalars_LUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Scalars_'
scalars_PWF = GetOpacityTransferFunction('Scalars_')
scalars_PWF.Points = [0.0, 0.0, 0.5, 0.0, 3788.20849609375, 0.3163265287876129, 0.5, 0.0, 4095.0, 0.26530611515045166, 0.5, 0.0]
scalars_PWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold1Display.Representation = 'Point Gaussian'
threshold1Display.ColorArrayName = ['POINTS', 'Scalars_']
threshold1Display.LookupTable = scalars_LUT
threshold1Display.SelectTCoordArray = 'None'
threshold1Display.SelectNormalArray = 'None'
threshold1Display.SelectTangentArray = 'None'
threshold1Display.OSPRayScaleArray = 'Scalars_'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.ScaleFactor = 23.5
threshold1Display.SelectScaleArray = 'Scalars_'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'Scalars_'
threshold1Display.GaussianRadius = 1.175
threshold1Display.SetScaleArray = ['POINTS', 'Scalars_']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'Scalars_']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = scalars_PWF
threshold1Display.ScalarOpacityUnitDistance = 2.884746699051141
threshold1Display.OpacityArrayName = ['POINTS', 'Scalars_']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1Display.ScaleTransferFunction.Points = [246.0, 0.0, 0.5, 0.0, 4095.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1Display.OpacityTransferFunction.Points = [246.0, 0.0, 0.5, 0.0, 4095.0, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for scalars_LUT in view renderView1
scalars_LUTColorBar = GetScalarBar(scalars_LUT, renderView1)
scalars_LUTColorBar.Title = 'Scalars_'
scalars_LUTColorBar.ComponentTitle = ''

# set color bar visibility
scalars_LUTColorBar.Visibility = 1

# show color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(threshold1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')