# Make a function that draws a glyph, feed it a glyph name, font name,
# and whether or not you want it to be outlined.
def draw_glyph(glyph_name, font_name, has_stroke):
    # Set the font
    font(font_name)
    # Set the fill and stroke for has_stroke == True
    if has_stroke == True:
        fill(None)
        stroke(0)
        strokeWidth(1)
        lineDash(3)
    # Set the fill and stroke for has_stroke == Flase
    else:
        fill(0, 0.2)
        stroke(None)
    text(glyph_name, (my_width/2, baseline_height), align='center')

baseline_height = 30
my_glyphs = ["a", "b", "c", "d", "e", "f"]
# Loop through each of those glyphs
for glyph_name in my_glyphs:
    newPage('LetterLandscape')
    my_width = width()
    my_height = height()
    # Draw background white.
    fill(1)
    rect(0, 0, my_width, my_height)
    # Set the fontSize
    fontSize(600)
    # First make the Helvetica glyph
    draw_glyph(glyph_name, 'Helvetica', False)
    # First make the Arial glyph
    draw_glyph(glyph_name, 'Arial', True)
    draw_glyph(glyph_name, 'Times New Roman', True)
    draw_glyph(glyph_name, 'Courier', True)
    draw_glyph(glyph_name, 'Menlo', True)
    draw_glyph(glyph_name, 'Monaco', False)

saveImage("letter_proof.pdf")