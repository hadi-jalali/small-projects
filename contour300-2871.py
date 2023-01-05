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
renderView1.CenterOfRotation = [127.10183238983154, 136.65554809570312, 257.8966097831726]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [86.26458048748935, -1006.55077582106, 224.73068085245825]
renderView1.CameraFocalPoint = [127.1018323898316, 136.65554809570312, 257.8966097831726]
renderView1.CameraViewUp = [0.9992805916909024, -0.03603865368235448, 0.011811626079558267]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 296.1966990607806
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
data2raw = ImageReader(registrationName='data2.raw', FileNames=['C:\\Users\\hadi1\\OneDrive\\Desktop\\CS year 3\\Semester 2\\CSC337-Data_Visualisation\\csc337_volvis_cw-master\\csc337_volvis_cw-master\\data2.raw'])
data2raw.DataExtent = [0, 255, 0, 255, 0, 511]

# create a new 'Image Reader'
data1raw = ImageReader(registrationName='data1.raw', FileNames=['C:\\Users\\hadi1\\OneDrive\\Desktop\\CS year 3\\Semester 2\\CSC337-Data_Visualisation\\csc337_volvis_cw-master\\csc337_volvis_cw-master\\data1.raw'])
data1raw.DataExtent = [0, 511, 0, 511, 0, 62]

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=data1raw)
threshold1.Scalars = ['POINTS', 'ImageFile']
threshold1.ThresholdRange = [35.0, 1492.0]

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=data1raw)
contour1.ContourBy = ['POINTS', 'ImageFile']
contour1.Isosurfaces = [746.0, 200.0, 343.55555555555554, 487.1111111111111, 630.6666666666666, 774.2222222222222, 917.7777777777777, 1061.3333333333333, 1204.8888888888887, 1348.4444444444443, 1492.0, 300.0, 432.44444444444446, 564.8888888888889, 697.3333333333334, 829.7777777777778, 962.2222222222223, 1094.6666666666667, 1227.1111111111113, 1359.5555555555557, 1492.0, 300.0, 374.5, 449.0, 523.5, 598.0, 672.5, 747.0, 821.5, 896.0, 970.5, 1045.0, 1119.5, 1194.0, 1268.5, 1343.0, 1417.5, 1492.0, 300.0, 331.63604539563147, 366.6082220188445, 405.26833653284416, 448.0052948393945, 495.24901432280234, 547.4747486536621, 605.2078686582261, 669.0291473471094, 739.5806022686886, 817.5719539590243, 903.7877654578336, 999.0953347113015, 1104.4534192562694, 1220.9218809527752, 1349.6723477872479, 1492.0000000000007]
contour1.PointMergeMethod = 'Uniform Binning'

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

# show data from contour2
contour2Display = Show(contour2, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'ImageFile'
imageFileLUT = GetColorTransferFunction('ImageFile')
imageFileLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1435.5, 0.865003, 0.865003, 0.865003, 2871.0, 0.705882, 0.0156863, 0.14902]
imageFileLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour2Display.Representation = 'Surface'
contour2Display.ColorArrayName = ['POINTS', 'ImageFile']
contour2Display.LookupTable = imageFileLUT
contour2Display.SelectTCoordArray = 'None'
contour2Display.SelectNormalArray = 'Normals'
contour2Display.SelectTangentArray = 'None'
contour2Display.OSPRayScaleArray = 'ImageFile'
contour2Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour2Display.SelectOrientationVectors = 'None'
contour2Display.ScaleFactor = 50.53915338516236
contour2Display.SelectScaleArray = 'ImageFile'
contour2Display.GlyphType = 'Arrow'
contour2Display.GlyphTableIndexArray = 'ImageFile'
contour2Display.GaussianRadius = 2.5269576692581177
contour2Display.SetScaleArray = ['POINTS', 'ImageFile']
contour2Display.ScaleTransferFunction = 'PiecewiseFunction'
contour2Display.OpacityArray = ['POINTS', 'ImageFile']
contour2Display.OpacityTransferFunction = 'PiecewiseFunction'
contour2Display.DataAxesGrid = 'GridAxesRepresentation'
contour2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour2Display.ScaleTransferFunction.Points = [300.0, 0.0, 0.5, 0.0, 2871.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour2Display.OpacityTransferFunction.Points = [300.0, 0.0, 0.5, 0.0, 2871.0, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for imageFileLUT in view renderView1
imageFileLUTColorBar = GetScalarBar(imageFileLUT, renderView1)
imageFileLUTColorBar.Title = 'ImageFile'
imageFileLUTColorBar.ComponentTitle = ''

# set color bar visibility
imageFileLUTColorBar.Visibility = 1

# show color legend
contour2Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'ImageFile'
imageFilePWF = GetOpacityTransferFunction('ImageFile')
imageFilePWF.Points = [0.0, 0.0, 0.5, 0.0, 2871.0, 1.0, 0.5, 0.0]
imageFilePWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(contour2)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')