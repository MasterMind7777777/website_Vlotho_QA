rgb_scale = 255
cmyk_scale = 100

class Convert():

    def rgb_to_cmy(rgb):
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        if (r == 0) and (g == 0) and (b == 0):
            # black
            return 100, 100, 100

        # rgb [0,255] -> cmy [0,1]
        c = 1 - r / float(rgb_scale)
        m = 1 - g / float(rgb_scale)
        y = 1 - b / float(rgb_scale)

        # rescale to the range [0,cmyk_scale]
        return c*cmyk_scale, m*cmyk_scale, y*cmyk_scale

    def hex_to_rgb(value):
        """Return (red, green, blue) for the color given as #rrggbb."""
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    def rgb_to_hex(rgb):
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        return "#{:02x}{:02x}{:02x}".format(r,g,b)