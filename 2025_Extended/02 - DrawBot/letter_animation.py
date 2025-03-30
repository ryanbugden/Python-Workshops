# drawBot
# Run this script in the RoboFont DrawBot extension

from random import choice

width = 1500
height = 1500
on_curve_radius = 8
off_curve_radius = 3

font = CurrentFont()

for i, glyph_name in enumerate(font.glyphOrder):
    # if i > 20:
    #     break
    glyph = font[glyph_name]
    
    # Set up the new page
    newPage(width, height)
    fill(1)
    rect(0,0,width,height)
    
    # Find some way of calculating where to move the glyph
    side_margin = (width - glyph.width) / 2
    vertical_margin = (height - font.info.capHeight) / 2
    translate(side_margin, vertical_margin)
    
    # Choose a cool color randomly
    fill(choice([0,1]), choice([0,1]), choice([0,1]))
    stroke(0)
    strokeWidth(0.5)

    # Copy the glyph so this script doesn't affect your actual font
    glyph = glyph.copy()
    # Decompose the components
    glyph.decompose()
    # Remove overlaps
    glyph.removeOverlap()
    # Draw the glyph itself
    bezier_path = BezierPath()
    glyph.draw(bezier_path)
    drawPath(bezier_path)

    # Loop through each contour in the glyph
    for contour in glyph.contours:
        # Loop through each bPoint in the contour
        for b_point in contour.bPoints:
            fill(0)
            stroke(None)

            # Draw on-curve points
            on_x, on_y = b_point.anchor
            oval(on_x - on_curve_radius, on_y - on_curve_radius, on_curve_radius*2, on_curve_radius*2)

            # Draw off-curves
            in_x, in_y = on_x + b_point.bcpIn[0], on_y + b_point.bcpIn[1]
            oval(in_x - off_curve_radius, in_y - off_curve_radius, off_curve_radius*2, off_curve_radius*2)
            out_x, out_y = on_x + b_point.bcpOut[0], on_y + b_point.bcpOut[1]
            oval(out_x - off_curve_radius, out_y - off_curve_radius, off_curve_radius*2, off_curve_radius*2)

            # Draw handles
            stroke(0)
            strokeWidth(0.5)
            # ... from in-handle point to on-curve point
            line((in_x, in_y), (on_x, on_y))
            # ... from on-curve point to out-handle point
            line((on_x, on_y), (out_x, out_y))
            
# Save the collection of pages as an animated gif
saveImage("~/Desktop/letters_with_handles.gif")
            