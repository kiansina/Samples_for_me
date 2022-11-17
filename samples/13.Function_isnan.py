def isnan(value):
    try:
        import math
        return math.isnan(float(value))
    except:
        return False
