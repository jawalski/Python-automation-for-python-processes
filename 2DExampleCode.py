#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
foamfoam = OpenFOAMReader(FileName='./foam.foam')
foamfoam.MeshRegions = ['internalMesh', 'lagrangian/coalCloud1']
foamfoam.CellArrays = ['C', 'C2H2', 'C2H3', 'C2H3O', 'C2H4', 'C2H5', 'C3H2', 'C3H3', 'CH', 'CH2', 'CH2CO', 'CH2O', 'CH2OH', 'CH2S', 'CH3', 'CH3O', 'CH3OH', 'CH4', 'CO', 'CO2', 'H', 'H2', 'H2O', 'H2O2', 'HCCO', 'HCO', 'HO2', 'N2', 'O', 'O2', 'OH', 'PaSR:kappa', 'T', 'U', 'alphat', 'dQ', 'k', 'nut', 'p', 'pDyn', 'rho', 'rhoEffLagrangian']
foamfoam.LagrangianArrays = ['Cp', 'T', 'U', 'UTurb', 'YC(s)', 'YH2O(l)', 'YN2(g)', 'YO2(g)', 'Yash(s)', 'Ygas', 'Yliquid', 'Ysolid', 'active', 'age', 'd', 'dTarget', 'mass0', 'nParticle', 'origId', 'origProcId', 'rho', 'tTurb', 'typeId']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on foamfoam
foamfoam.MeshRegions = ['internalMesh', 'inlet', 'pilot', 'coflow', 'outer', 'outlet', 'lagrangian/coalCloud1']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1501, 766]

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# show data in view
foamfoamDisplay = Show(foamfoam, renderView1)
# trace defaults for the display properties.
foamfoamDisplay.Representation = 'Surface'
foamfoamDisplay.ColorArrayName = ['POINTS', 'p']
foamfoamDisplay.LookupTable = pLUT
foamfoamDisplay.OSPRayScaleArray = 'p'
foamfoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
foamfoamDisplay.SelectOrientationVectors = 'U'
foamfoamDisplay.ScaleFactor = 0.03810000121593476
foamfoamDisplay.SelectScaleArray = 'p'
foamfoamDisplay.GlyphType = 'Arrow'
foamfoamDisplay.GlyphTableIndexArray = 'p'
foamfoamDisplay.DataAxesGrid = 'GridAxesRepresentation'
foamfoamDisplay.PolarAxes = 'PolarAxesRepresentation'
foamfoamDisplay.GaussianRadius = 0.01905000060796738
foamfoamDisplay.SetScaleArray = ['POINTS', 'p']
foamfoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
foamfoamDisplay.OpacityArray = ['POINTS', 'p']
foamfoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
foamfoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Slice'
slice1 = Slice(Input=foamfoam)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.0, 0.0, 0.19050000607967377]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# show data in view
slice1Display = Show(slice1, renderView1)
# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'p']
slice1Display.LookupTable = pLUT
slice1Display.OSPRayScaleArray = 'p'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'U'
slice1Display.ScaleFactor = 0.03810000121593476
slice1Display.SelectScaleArray = 'p'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'p'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.GaussianRadius = 0.01905000060796738
slice1Display.SetScaleArray = ['POINTS', 'p']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'p']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(foamfoam, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'T'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'T'
tLUT = GetColorTransferFunction('T')

# set active source
SetActiveSource(foamfoam)

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

renderView1.AxesGrid.AxesToLabel = 5
# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.XTitle = 'X Axis'
renderView1.AxesGrid.ZTitle = 'Z Axis'
renderView1.AxesGrid.XTitleFontSize = 18
renderView1.AxesGrid.ZTitleFontSize = 18
renderView1.AxesGrid.XLabelFontSize = 18
renderView1.AxesGrid.ZLabelFontSize = 18
renderView1.AxesGrid.DataBoundsInflateFactor = 0.02
renderView1.AxesGrid.DataScale = [5.0, 1.0, 1.0]
# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.XAxisUseCustomLabels = 1
renderView1.AxesGrid.XAxisLabels = [-0.03, -0.02, -0.01, 0.0, 0.01, 0.02, 0.03]


# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.DataBoundsInflateFactor = 0.001

# set active source
SetActiveSource(slice1)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
tLUT.ApplyPreset('Blue to Red Rainbow', True)

# Rescale transfer function
tLUT.RescaleTransferFunction(307.9, 308.1)

# get opacity transfer function/opacity map for 'T'
tPWF = GetOpacityTransferFunction('T')

# Rescale transfer function
tPWF.RescaleTransferFunction(307.9, 308.1)

# get color legend/bar for tLUT in view renderView1
tLUTColorBar = GetScalarBar(tLUT, renderView1)

# Properties modified on tLUTColorBar
tLUTColorBar.WindowLocation = 'AnyLocation'
tLUTColorBar.Title = 'T(K)'
tLUTColorBar.TitleFontSize = 6
tLUTColorBar.LabelFontSize = 6
tLUTColorBar.AddRangeLabels = 0

# Properties modified on tLUTColorBar
tLUTColorBar.ScalarBarThickness = 5
tLUTColorBar.ScalarBarLength = 0.5

# change scalar bar placement
tLUTColorBar.Position = [0.6628914057295137, 0.1919060052219321]
tLUTColorBar.ScalarBarLength = 0.6

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, -1.1554233637385614, 0.19050000607967377]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.19050000607967377]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.29904557169195695

# save screenshot
#SaveScreenshot('./2DTempParticlePlot.jpg', renderView1, ImageResolution=[1501, 766])
SaveAnimation('./2DAnimation.jpg', renderView1, ImageResolution=[1500, 764],
    FrameWindow=[0,86])

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
