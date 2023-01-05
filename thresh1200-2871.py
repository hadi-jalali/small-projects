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
renderView1.CenterOfRotation = [127.47231388092041, 119.60713958740234, 247.67825937271118]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [229.99650529958348, -945.6786251220142, 269.9165826758461]
renderView1.CameraFocalPoint = [127.47231388092041, 119.60713958740234, 247.67825937271118]
renderView1.CameraViewUp = [0.9954027336700769, 0.09576034324775273, -0.0018315193721127328]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 277.04998297041817
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

# create a new 'Image Reader'
data1raw = ImageReader(registrationName='data1.raw', FileNames=['C:\\Users\\hadi1\\OneDrive\\Desktop\\CS year 3\\Semester 2\\CSC337-Data_Visualisation\\csc337_volvis_cw-master\\csc337_volvis_cw-master\\data1.raw'])
data1raw.DataExtent = [0, 511, 0, 511, 0, 62]

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=data1raw)
contour1.ContourBy = ['POINTS', 'ImageFile']
contour1.Isosurfaces = [746.0, 200.0, 343.55555555555554, 487.1111111111111, 630.6666666666666, 774.2222222222222, 917.7777777777777, 1061.3333333333333, 1204.8888888888887, 1348.4444444444443, 1492.0, 300.0, 432.44444444444446, 564.8888888888889, 697.3333333333334, 829.7777777777778, 962.2222222222223, 1094.6666666666667, 1227.1111111111113, 1359.5555555555557, 1492.0, 300.0, 374.5, 449.0, 523.5, 598.0, 672.5, 747.0, 821.5, 896.0, 970.5, 1045.0, 1119.5, 1194.0, 1268.5, 1343.0, 1417.5, 1492.0, 300.0, 331.63604539563147, 366.6082220188445, 405.26833653284416, 448.0052948393945, 495.24901432280234, 547.4747486536621, 605.2078686582261, 669.0291473471094, 739.5806022686886, 817.5719539590243, 903.7877654578336, 999.0953347113015, 1104.4534192562694, 1220.9218809527752, 1349.6723477872479, 1492.0000000000007]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=data1raw)
threshold1.Scalars = ['POINTS', 'ImageFile']
threshold1.ThresholdRange = [134.28, 1312.96]

# create a new 'Image Reader'
data2raw = ImageReader(registrationName='data2.raw', FileNames=['C:\\Users\\hadi1\\OneDrive\\Desktop\\CS year 3\\Semester 2\\CSC337-Data_Visualisation\\csc337_volvis_cw-master\\csc337_volvis_cw-master\\data2.raw'])
data2raw.DataExtent = [0, 255, 0, 255, 0, 511]

# create a new 'Contour'
contour2 = Contour(registrationName='Contour2', Input=data2raw)
contour2.ContourBy = ['POINTS', 'ImageFile']
contour2.Isosurfaces = [1435.5, 300.0, 385.577310795753, 495.5662086682824, 636.9302868652111, 818.6195572461853, 1052.137091492647, 1352.2673010873332, 1738.011964767616, 2233.7932650198018, 2870.9999999999995, 400.0, 497.9298070755206, 619.8352319356629, 771.586093640838, 960.4892868718426, 1195.6406132755026, 1488.3627497498203, 1852.7504421032984, 2306.3491754889524, 2871.0, 800.0, 922.0412337306274, 1062.7000458743717, 1224.8165767295, 1411.6642343767396, 1627.015790347663, 1875.2195582892134, 2161.2871938009857, 2490.994888273083, 2870.999999999999]
contour2.PointMergeMethod = 'Uniform Binning'

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=contour2)
threshold2.Scalars = ['POINTS', 'ImageFile']
threshold2.ThresholdRange = [1200.0, 2871.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from threshold2
threshold2Display = Show(threshold2, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'ImageFile'
imageFileLUT = GetColorTransferFunction('ImageFile')
imageFileLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1435.5, 0.865003, 0.865003, 0.865003, 2871.0, 0.705882, 0.0156863, 0.14902]
imageFileLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'ImageFile'
imageFilePWF = GetOpacityTransferFunction('ImageFile')
imageFilePWF.Points = [0.0, 0.0, 0.5, 0.0, 2871.0, 1.0, 0.5, 0.0]
imageFilePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'
threshold2Display.ColorArrayName = ['POINTS', 'ImageFile']
threshold2Display.LookupTable = imageFileLUT
threshold2Display.SelectTCoordArray = 'None'
threshold2Display.SelectNormalArray = 'Normals'
threshold2Display.SelectTangentArray = 'None'
threshold2Display.OSPRayScaleArray = 'ImageFile'
threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold2Display.SelectOrientationVectors = 'None'
threshold2Display.ScaleFactor = 50.53915338516236
threshold2Display.SelectScaleArray = 'ImageFile'
threshold2Display.GlyphType = 'Arrow'
threshold2Display.GlyphTableIndexArray = 'ImageFile'
threshold2Display.GaussianRadius = 2.5269576692581177
threshold2Display.SetScaleArray = ['POINTS', 'ImageFile']
threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold2Display.OpacityArray = ['POINTS', 'ImageFile']
threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
threshold2Display.PolarAxes = 'PolarAxesRepresentation'
threshold2Display.ScalarOpacityFunction = imageFilePWF
threshold2Display.ScalarOpacityUnitDistance = 2.1437941505104963
threshold2Display.OpacityArrayName = ['POINTS', 'ImageFile']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold2Display.ScaleTransferFunction.Points = [300.0, 0.0, 0.5, 0.0, 1738.011962890625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold2Display.OpacityTransferFunction.Points = [300.0, 0.0, 0.5, 0.0, 1738.011962890625, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for imageFileLUT in view renderView1
imageFileLUTColorBar = GetScalarBar(imageFileLUT, renderView1)
imageFileLUTColorBar.Title = 'ImageFile'
imageFileLUTColorBar.ComponentTitle = ''

# set color bar visibility
imageFileLUTColorBar.Visibility = 1

# show color legend
threshold2Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(threshold2)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')