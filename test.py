from direct.showbase.ShowBase import ShowBase


class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.plane = self.loader.loadModel('1.egg')
        self.plane.reparentTo(self.render)
        self.tex = self.loader.loadTexture('nanana.jpg')
        self.plane.setTexture(self.tex, 1)

app = MyApp()
app.run()

