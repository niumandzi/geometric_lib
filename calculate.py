import circle
import square

figs = {
    'circle': {
        'area': circle.area,
        'perimeter': circle.perimeter
    },
    'square': {
        'area': square.area,
        'perimeter': square.perimeter
    }
}

sizes = {
    'area-circle': 1,
    'perimeter-circle': 1,
    'area-square': 1,
    'perimeter-square': 1
}


def calc(fig, func, size):
    assert fig in figs, f"Unknown figure: {fig}"
    assert func in figs[fig], f"Unknown function: {func}"
    assert all(s > 0 for s in size), "All size parameters must be positive"

    result = figs[fig][func](*size)
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in figs:
        fig = input(
            f"Enter figure name, available are {list(figs.keys())}:\n"
        )

    while func not in figs[fig]:
        func = input(
            f"Enter function name, available are {list(figs[fig].keys())}:\n"
        )

    while len(size) != sizes[f"{func}-{fig}"]:
        size = list(
            map(int, input("Input figure sizes separated by space:\n").split())
        )

    result = calc(fig, func, size)
    print(f'{func} of {fig} is {result}')
