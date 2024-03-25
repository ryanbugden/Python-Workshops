# Start an empty Bezier path
path = BezierPath()
print(path)
print(path.onCurvePoints)

# Move to a point, to start
path.moveTo((100, 100))
# Draw a line to a point
path.lineTo((100, 900))
path.lineTo((900, 900))
# Close the path
path.closePath()
# Now this Bezier path has some points. Check out the coordinates.
print(path.onCurvePoints)

# Now let's put the path on the page <-
fill(None)
stroke(0)
drawPath(path)