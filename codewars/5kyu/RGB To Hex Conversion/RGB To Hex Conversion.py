def rgb(r, g, b):
    # your code here :)
    def convert_2_hex_str(v):
        if v >= 255:
            return "FF"
        if v < 0:
            return f"00"
        return "%02X" % v

    return convert_2_hex_str(r)  + convert_2_hex_str(g) + convert_2_hex_str(b)