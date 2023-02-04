import random as rng

def get_RG_Coords(coords, range):
    x = rng.random()
    y = rng.random()

    x = (2*x-1)*range[0] + coords[0]
    y = (2*y-1)*range[1] + coords[1]

    return (x,y)

if __name__ == "__main__":
    coords = [-3,10]
    range = [5,5]
    rand_coords = get_RG_Coords(coords, range)

    print(rand_coords)