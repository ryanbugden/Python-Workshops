path = BezierPath()

print(path)
print(path.onCurvePoints)

# move to a point
path.moveTo((100, 100))
# line to a point
path.lineTo((100, 200))
path.lineTo((200, 200))
# close the path

print(path.onCurvePoints)

fill(None)
stroke(0)
drawPath(path)