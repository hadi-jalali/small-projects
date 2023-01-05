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
renderView1.CenterOfRotation = [231.58978271484375, 258.08978271484375, 31.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [153.07733731584418, -721.1208020769467, -19.740222250379162]
renderView1.CameraFocalPoint = [231.58978271484338, 258.08978271484386, 30.999999999999982]
renderView1.CameraViewUp = [-0.06494447150555586, 0.056831363072322616, -0.9962692466357707]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 254.5906191720483
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

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(registrationName='ExtractSubset1', Input=data1raw)
extractSubset1.VOI = [20, 445, 100, 430, 0, 62]

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

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=data1raw)
threshold1.Scalars = ['POINTS', 'ImageFile']
threshold1.ThresholdRange = [29.84, 1492.0]

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=threshold1)
clip1.ClipType = 'Cylinder'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'ImageFile']
clip1.Value = 761.0

# init the 'Cylinder' selected for 'ClipType'
clip1.ClipType.Center = [220.0, 183.0, 31.99463038327576]
clip1.ClipType.Axis = [0.0, 0.0, -1.0]
clip1.ClipType.Radius = 219.17988949167818

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [255.5, 255.0, 31.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from clip1
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'ImageFile'
imageFileLUT = GetColorTransferFunction('ImageFile')
imageFileLUT.RGBPoints = [30.0, 0.4, 0.145098, 0.023529, 93.93715499999979, 0.500392, 0.174625, 0.019592, 157.8743100000002, 0.600784, 0.204291, 0.015656, 221.81197449999976, 0.701176, 0.251534, 0.011719, 285.74912950000015, 0.800984, 0.299146, 0.008397, 349.68628449999994, 0.863975, 0.370012, 0.043829, 413.62343949999973, 0.926321, 0.441107, 0.0794, 477.56059450000015, 0.961753, 0.521815, 0.120738, 541.4980399149999, 0.996078, 0.602645, 0.163122, 605.4354140000002, 0.996078, 0.68729, 0.237924, 669.3725689999999, 0.996078, 0.771011, 0.314879, 733.3097239999997, 0.996078, 0.832034, 0.444798, 797.246879, 0.996171, 0.892042, 0.572595, 861.1845434999997, 0.998139, 0.931411, 0.65724, 925.1216985, 1.0, 0.969489, 0.741669, 989.0588535000004, 1.0, 0.985236, 0.822376, 1049.0, 1.0, 1.0, 0.898039]
imageFileLUT.ColorSpace = 'Lab'
imageFileLUT.NanColor = [0.25, 0.0, 0.0]
imageFileLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'ImageFile'
imageFilePWF = GetOpacityTransferFunction('ImageFile')
imageFilePWF.Points = [30.0, 0.41836732625961304, 0.5, 0.0, 93.0650320908988, 0.4693877398967743, 0.5, 0.0, 119.61893347206373, 0.4591836631298065, 0.5, 0.0, 182.68396556296253, 0.22448979318141937, 0.5, 0.0, 202.59939159883623, 0.2857142686843872, 0.5, 0.0, 225.83389407756624, 0.27551019191741943, 0.5, 0.0, 235.7914458657138, 0.5153061151504517, 0.5, 0.0, 249.06839655629625, 0.34183672070503235, 0.5, 0.0, 262.3450247873001, 0.2602040767669678, 0.5, 0.0, 537.8403005487826, 0.3520407974720001, 0.5, 0.0, 537.8403005487826, 0.37755101919174194, 0.5, 0.0, 1049.0, 1.0, 0.5, 0.0]
imageFilePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'ImageFile']
clip1Display.LookupTable = imageFileLUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'ImageFile'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 51.0
clip1Display.SelectScaleArray = 'ImageFile'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'ImageFile'
clip1Display.GaussianRadius = 2.5500000000000003
clip1Display.SetScaleArray = ['POINTS', 'ImageFile']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'ImageFile']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = imageFilePWF
clip1Display.ScalarOpacityUnitDistance = 4.023484921377437
clip1Display.OpacityArrayName = ['POINTS', 'ImageFile']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [30.0, 0.0, 0.5, 0.0, 1466.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [30.0, 0.0, 0.5, 0.0, 1466.0, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for imageFileLUT in view renderView1
imageFileLUTColorBar = GetScalarBar(imageFileLUT, renderView1)
imageFileLUTColorBar.Position = [0.9037344398340249, 0.015267175572519083]
imageFileLUTColorBar.Title = 'ImageFile'
imageFileLUTColorBar.ComponentTitle = ''

# set color bar visibility
imageFileLUTColorBar.Visibility = 1

# show color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(clip1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')