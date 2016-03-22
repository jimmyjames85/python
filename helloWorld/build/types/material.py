class RGB:
    red = 0.0
    green = 0.0
    blue = 0.0

    def __init__(self, r=0, g=0, b=0):
        if(r>=0 and r<=1):
            self.red = r
        if(g>=0 and g<=1):
            self.green = g
        if(b>=0 and b<=1):
            self.blue = b

    def __str__(self):
        return "%3f %3f %3f" %(self.red,self.green, self.blue)


class Material:
    name = ""
    ambientReflectivity = RGB()
    diffuseReflectivity = RGB()
    specularReflectivity = RGB()
    specularExp = 500.0

    #0 - constant color
    #1 - Lambertian shading
    #2 - Phong shading
    illumNo = 1

