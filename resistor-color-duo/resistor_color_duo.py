def value(colors):
    color_order=['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    value = []
    for color in colors[:2]:
        value.append(str(color_order.index(color)))
    return int(''.join(value))



print(value(['yellow','black', 'brown', 'red']))
