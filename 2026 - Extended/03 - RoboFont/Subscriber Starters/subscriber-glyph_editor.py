from mojo.subscriber import Subscriber, registerGlyphEditorSubscriber


class MyGlyphEditorSubscriber(Subscriber):
    
    def build(self):
        pass
        
    def glyphEditorDidMouseDown(self, info):
        glyph = info['glyph']
        location = info['locationInGlyph']
        print(glyph.name)
        print(location.x, location.y)
        

registerGlyphEditorSubscriber(MyGlyphEditorSubscriber)