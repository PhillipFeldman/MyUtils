def DeepestCopy(container):
    t = type(container)
    if t == int or t == float or t == bool or t == str:
        return container
    new = t()
    if t == list or t == tuple:
        for item in container:
            new.append(DeepestCopy(item))
    if t == dict:
        for item in container:
            new[item] = DeepestCopy(container[item])
    if t == set:
        for item in container:
            new.add(item)
    return new

def test_list():
    x = []
    y = DeepestCopy(x)
    assert x is not y

    x = [1,[2,[3]]]
    y = DeepestCopy(x)
    y[1][1].append(4)
    assert len(x[1][1]) == 1
    assert len(y[1][1]) == 2

def main():
    test_list()

if __name__ == '__main__':
    main()