import re

def input_validator(ans_input):
    x_y_ops = re.compile(r'((top|mid|low)-(l|m|r))')
    result = x_y_ops.search(ans_input.lower())
    if result.group() != None:
        return True
    else:
        return False

def Converter(ans_input):
    x_options = {
        "top":0,
        "mid":3,
        "low":6
    }
    y_options = {
        "l":1,
        "m":2,
        "r":3
    }
    x_in, y_in = ans_input.split('-')
    return str(x_options[x_in.lower()] + y_options[y_in.lower()])
