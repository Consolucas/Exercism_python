def two_fer(name = None):
# deixa o nome como nulo, mas podendo receber um valor posteriormente
    if name is None:
    # caso continue sendo nulo
        return 'One for you, one for me.'
    else:
        return f'One for {name}, one for me.'
    

