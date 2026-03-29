# menuTitle: Make Quick Italic & Rearrange Extremes

import math
from fontTools.misc.fixedTools import otRound


# Choose which punctuation to exclude
exclude = []
OFFSET = False


def offset_glyphs(font, glyphs, offset):
    '''
    Offset for italic slant
    Code by Gustavo/Frederik/Lukas
    https://gist.github.com/gferreira/56e4f13b7f104ec4ff69fb90d402dfe1
    '''
    def get_flipped_components(font):
        flipped_components = []
        for g in font:
            for component in g.components:
                if component.naked().transformation:
                    # Flipped horizontal
                    if component.naked().transformation[0] == -1:
                        flipped_components.append(g.name)
                    # Flipped vertical
                    if component.naked().transformation[3] == -1:
                        flipped_components.append(g.name)
        return list(set(flipped_components))
    flipped_components = get_flipped_components(font)
    print("flipped_components", flipped_components)
    if offset:
        component_map = font.getReverseComponentMapping()
        for glyph in glyphs:
            with glyph.undo(f"Offset glyph {glyph.name}"):
                glyph.moveBy((offset, 0))
            for composed_glyph in component_map.get(glyph.name, []):
                for component in font[composed_glyph].components:
                    if component.baseGlyph == glyph.name:
                        if glyph.name not in flipped_components:
                            component.moveBy((-offset, 0))
            glyph.changed()
        for g_name in flipped_components:
            for component in font[g_name].components:
                component.moveBy((offset*2, 0))
                for composed_glyph in component_map.get(g_name, []):
                    for component in font[composed_glyph].components:
                        if component.baseGlyph == g_name:
                            component.moveBy((-offset, 0))
                                
                                
def get_surrounding_points(pt):
    '''
    Gets the points before and after a point.
    '''
    i = pt.index
    prev_pt = pt.contour.points[i - 1]
    # The only reason this isn't using "i + 1" is because we have to be able to reset to index 0
    next_pt = pt.contour.points[i-len(pt.contour.points)+1]
    return prev_pt, next_pt
    
    
def get_skewed_coordinates(pt, skew_angle, origin):
    '''
    Gets the hypothetical coordinates of a point that is skewed.
    '''
    pt = pt.copy()
    pt.skewBy(skew_angle, origin=origin)
    return (otRound(pt.x), otRound(pt.y))


def point_has_vertical_handles(pt):
    '''
    Checks whether a point has two handles, both of which are vertical.
    '''
    # We don't care about off-curve points here.
    if pt.type == "offcurve":
        return False
    # Get the surrounding points
    prev_pt, next_pt = get_surrounding_points(pt)
    # Check to see if surrounding points are both handles
    if prev_pt.type != "offcurve" or next_pt.type != "offcurve":
        return False
    # Check to see if x values are the same (improve to consider italic angle later)
    elif prev_pt.x != pt.x or next_pt.x != pt.x:
        return False
    # Check to see if the handles have a length.
    elif prev_pt.y - pt.y == 0 or next_pt.y - pt.y == 0:
        return False
    # If you've gotten this far, then it's a good point. Grab all surrounding points for removal.
    return True
    

# Choose an angle
slant_angle = 10
# Get our font object
font = CurrentFont()
# Copy original font into a new one
new_font = font.copy()
# Loop through all glyphs in this copy of the font
for glyph in new_font:   
    # Exclude punctuation
    if glyph.name in exclude:
        # Don’t complete the loop
        continue
    # Scan for vertical two-handle points we need to remove later
    coords_to_remove_later = []
    for contour in glyph:
        for point in contour.points:
            if point_has_vertical_handles(point):
                # Store the coordinates of where these points will end up
                coords_to_remove_later.append(get_skewed_coordinates(point, slant_angle, (0, 0)))
    # Skew each contour and anchor in each glyph
    for contour in glyph.contours:    
        contour.skewBy(slant_angle, origin=(0, 0))
    for anchor in glyph.anchors:
        anchor.skewBy(slant_angle, origin=(0, 0))
    # Add extreme points
    glyph.extremePoints()
    # Copy glyph (points not yet removed) to skewed layer
    glyph.copyToLayer("skewed", clear=True)
    # Fix the background skewed layer’s glyph width
    glyph.getLayer("skewed").width = glyph.width
    # Remove previously vertical extremes (foreground only)
    for contour in glyph: 
        for b_point in contour.bPoints:
            if b_point.anchor in coords_to_remove_later:
                contour.removeBPoint(b_point, preserveCurve=True)
# Change font’s italic angle
new_font.info.italicAngle = -slant_angle
new_font.info.styleName += " Italic"
if OFFSET:
    slant_offset = otRound(math.tan(slant_angle * math.pi / 180) * (font.info.xHeight * 0.5))
    new_font.lib['com.typemytype.robofont.italicSlantOffset'] = slant_offset
    offset_glyphs(new_font, new_font, slant_offset)
# Actually open the font
new_font.openInterface()
                