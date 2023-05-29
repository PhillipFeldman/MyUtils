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

def DeepestCopyIterative(container):
    t = type(container)
    if t == int or t == float or t == bool or t == str:
        return container
    new_container = t()
    stack = []
    stack.append((new_container,None))
    while len(stack) > 0:
        temp = stack.pop()
        parent = temp[1]
        parent_type = type(parent)
        current= temp[0]
        current_type = type(current)
        current_copy = current_type()

        if parent_type == list or parent_type == tuple:
            parent.append(current)
        if parent_type == dict:
            for item in container:
                new[item] = DeepestCopy(container[item])
        if parent_type == set:
            for item in container:
                new.add(item)

        if current_type == list or current_type == tuple:
            for i in range(len(current)):
                stack.append((current[i],

                              +))
        if current_type == dict:
            for k in current.keys():
                stack.append(((k,current[k]),current_copy))
        if current_type == set:
            l = list(current)
            for i in range(len(l)):
                stack.append(l[i],current_copy)



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