# Caroline NYAMUPANDA
# R00206878
import reviews as reviews


def read_data():
    flavour = []
    figuires = []

    with open(reviews.txt) as data:
        for line in data:
            line = line.split(',')
            flavour.append(line[0])
            figuires.append(int(line[1]))
            return flavour, figuires


def least_popular(flavours, figuires):
    least = min(figuires)
    index_least = figuires.index(least)
    return flavours[index_least]


def main():
    flavours, figuires = read_data()
    print(read_data())
    print(least_popular(flavours, figuires))


if __name__ == '__main__':
    main()
