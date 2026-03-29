from mojo.subscriber import Subscriber, registerRoboFontSubscriber


class MyRoboFontSubscriber(Subscriber):
    
    def build(self):
        pass
        
    def roboFontDidSwitchCurrentGlyph(self, info):
        glyph = info['glyph']
        print(glyph)
        

registerRoboFontSubscriber(MyRoboFontSubscriber)