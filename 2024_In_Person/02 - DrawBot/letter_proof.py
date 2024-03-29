# Make a function that draws a glyph, feed it a glyph name, font name,
# and whether or not you want it to be outlined.
def draw_glyph(glyph_name, font_name, has_stroke):
    baseline_height = 100
    # Set the font
    font(font_name)
    # Set the font size
    fontSize(600)
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
    text(glyph_name, (width()/2, baseline_height), align='center')

# Make a list of glyph names
my_glyphs = ["a", "b", "c", "d", "e", "f"]
# Loop through each of those glyphs
for glyph_name in my_glyphs:
    newPage('LetterLandscape')
    # Draw white background
    fill(1)
    rect(0, 0, width(), height())
    # Run the function, with some different fonts, and settings
    draw_glyph(glyph_name, 'Helvetica', False)
    draw_glyph(glyph_name, 'Arial', True)
    draw_glyph(glyph_name, 'Times New Roman', True)
    draw_glyph(glyph_name, 'Courier', True)
    draw_glyph(glyph_name, 'Menlo', True)
    draw_glyph(glyph_name, 'Monaco', False)

# Save whole set of pages as a PDF
saveImage("_output/letter_proof.pdf")