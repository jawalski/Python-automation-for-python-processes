#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1501, 766]

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

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

# set scalar coloring
ColorBy(foamfoamDisplay, ('POINTS', 'T'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
foamfoamDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
foamfoamDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'T'
tLUT = GetColorTransferFunction('T')

# create a new 'Slice'
slice1 = Slice(Input=foamfoam)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.0, 0.0, 0.19050000607967377]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

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

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
tLUT.ApplyPreset('Blue to Red Rainbow', True)

# get color legend/bar for tLUT in view renderView1
tLUTColorBar = GetScalarBar(tLUT, renderView1)

# Properties modified on tLUTColorBar
tLUTColorBar.AddRangeLabels = 0

# set active source
SetActiveSource(foamfoam)

# show data in view
foamfoamDisplay = Show(foamfoam, renderView1)

# show color bar/color legend
foamfoamDisplay.SetScalarBarVisibility(renderView1, True)

# create a new 'Slice'
slice2 = Slice(Input=foamfoam)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [0.0, 0.0, 0.19050000607967377]

# Properties modified on slice2.SliceType
slice2.SliceType.Normal = [0.0, 1.0, 0.0]

# Properties modified on slice2.SliceType
slice2.SliceType.Normal = [0.0, 1.0, 0.0]

# show data in view
slice2Display = Show(slice2, renderView1)
# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['POINTS', 'p']
slice2Display.LookupTable = pLUT
slice2Display.OSPRayScaleArray = 'p'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'U'
slice2Display.ScaleFactor = 0.03810000121593476
slice2Display.SelectScaleArray = 'p'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'p'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'
slice2Display.GaussianRadius = 0.01905000060796738
slice2Display.SetScaleArray = ['POINTS', 'p']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'p']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(foamfoam, renderView1)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip1 = Clip(Input=slice2)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'p']
clip1.Value = 101321.3515625

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.0, 0.0, 0.19050000607967377]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# show data in view
clip1Display = Show(clip1, renderView1)
# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'p']
clip1Display.LookupTable = pLUT
clip1Display.OSPRayScaleArray = 'p'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'U'
clip1Display.ScaleFactor = 0.03810000121593476
clip1Display.SelectScaleArray = 'p'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'p'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = pPWF
clip1Display.ScalarOpacityUnitDistance = 0.0119588804886831
clip1Display.GaussianRadius = 0.01905000060796738
clip1Display.SetScaleArray = ['POINTS', 'p']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'p']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(slice2, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(slice2)

# set scalar coloring
ColorBy(slice2Display, ('POINTS', 'T'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice2Display.RescaleTransferFunctionToDataRange(True, False)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice2.SliceType)

# set active source
SetActiveSource(clip1)

# set scalar coloring
ColorBy(clip1Display, ('POINTS', 'T'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
clip1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(foamfoam)

# create a new 'Slice'
slice3 = Slice(Input=foamfoam)
slice3.SliceType = 'Plane'
slice3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = [0.0, 0.0, 0.19050000607967377]

# set active source
SetActiveSource(foamfoam)

# show data in view
foamfoamDisplay = Show(foamfoam, renderView1)

# show color bar/color legend
foamfoamDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(slice3)

# Properties modified on slice3.SliceType
slice3.SliceType.Origin = [0.0, 0.0, 0.0020027162115948322]
slice3.SliceType.Normal = [0.0, 0.0, 1.0]

# Properties modified on slice3.SliceType
slice3.SliceType.Origin = [0.0, 0.0, 0.0020027162115948322]
slice3.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice3Display = Show(slice3, renderView1)
# trace defaults for the display properties.
slice3Display.Representation = 'Surface'
slice3Display.ColorArrayName = ['POINTS', 'p']
slice3Display.LookupTable = pLUT
slice3Display.OSPRayScaleArray = 'p'
slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice3Display.SelectOrientationVectors = 'U'
slice3Display.ScaleFactor = 0.032600000500679016
slice3Display.SelectScaleArray = 'p'
slice3Display.GlyphType = 'Arrow'
slice3Display.GlyphTableIndexArray = 'p'
slice3Display.DataAxesGrid = 'GridAxesRepresentation'
slice3Display.PolarAxes = 'PolarAxesRepresentation'
slice3Display.GaussianRadius = 0.016300000250339508
slice3Display.SetScaleArray = ['POINTS', 'p']
slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display.OpacityArray = ['POINTS', 'p']
slice3Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(foamfoam, renderView1)

# show color bar/color legend
slice3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice3Display, ('POINTS', 'T'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice3Display.SetScalarBarVisibility(renderView1, True)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice3.SliceType)

# Properties modified on slice3Display.DataAxesGrid
slice3Display.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on slice3Display.DataAxesGrid
slice3Display.DataAxesGrid.GridAxesVisibility = 0

# set active source
SetActiveSource(slice1)

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 0

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# set active source
SetActiveSource(slice2)

# Properties modified on slice2Display.DataAxesGrid
slice2Display.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 0

# set active source
SetActiveSource(clip1)

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# set active source
SetActiveSource(slice1)

# set active source
SetActiveSource(clip1)

# set active source
SetActiveSource(slice3)

# Properties modified on slice3Display.DataAxesGrid
slice3Display.DataAxesGrid.GridAxesVisibility = 1

# set active source
SetActiveSource(foamfoam)

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.ShowGrid = 1

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.LabelUniqueEdgesOnly = 1

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.FacesToRender = 63

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.AxesToLabel = 7

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.XTitle = 'XAxis'
renderView1.AxesGrid.YTitle = 'YAxis'
renderView1.AxesGrid.ZTitle = 'ZAxis'
renderView1.AxesGrid.YTitleBold = 1
renderView1.AxesGrid.YTitleFontSize = 14
renderView1.AxesGrid.XTitleBold = 1
renderView1.AxesGrid.XTitleFontSize = 14
renderView1.AxesGrid.ZTitleBold = 1
renderView1.AxesGrid.ZTitleFontSize = 14
renderView1.AxesGrid.DataBoundsInflateFactor = 0.02

# set active source
SetActiveSource(slice1)

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 0

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# set active source
SetActiveSource(slice2)

# Properties modified on slice2Display.DataAxesGrid
slice2Display.DataAxesGrid.GridAxesVisibility = 0

# set active source
SetActiveSource(clip1)

# Properties modified on clip1Display.DataAxesGrid
clip1Display.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on clip1Display.DataAxesGrid
clip1Display.DataAxesGrid.GridAxesVisibility = 0

# set active source
SetActiveSource(slice3)

# Properties modified on slice3Display.DataAxesGrid
slice3Display.DataAxesGrid.GridAxesVisibility = 0

tPWF = GetOpacityTransferFunction('T')
# change scalar bar placement
tLUTColorBar.WindowLocation = 'AnyLocation'
tLUTColorBar.Position = [0.8534976682211859, 0.12049608355091384]
tLUTColorBar.ScalarBarLength = 0.8
tLUTColorBar.Title = 'T(K)'
# Rescale transfer function
tLUT.RescaleTransferFunction(307.9, 308.1)

# Rescale transfer function
tPWF.RescaleTransferFunction(307.9, 308.1)
tLUTColorBar.DrawTickLabels = 1
tLUTColorBar.TitleFontSize = 8
tLUTColorBar.LabelFontSize = 8
tLUTColorBar.ScalarBarThickness = 8

# current camera placement for renderView1
renderView1.CameraPosition = [-0.7924314760738207, -0.5635425288044681, 0.8145795870860825]
renderView1.CameraFocalPoint = [-1.4289630422811202e-17, -1.7037636273351817e-16, 0.19050000607967357]
renderView1.CameraViewUp = [0.38422348435093656, 0.387646414459648, 0.8379156111624873]
renderView1.CameraParallelScale = 0.29904557169195695

# save screenshot
#SaveScreenshot('./3DTempParticlePlot.jpg', renderView1, ImageResolution=[1501, 766])
SaveAnimation('./3DAnimation.jpg', renderView1, ImageResolution=[1500, 764],
    FrameWindow=[0,86])
#### saving camera placements for all active views
