from implementation.filter import BloomFilter


animals = [
    "dog",
    "cat",
    "giraffe",
    "fly",
    "mosquito",
    "horse",
    "eagle",
    "bird",
    "bison",
    "boar",
    "butterfly",
    "ant",
    "anaconda",
    "bear",
    "chicken",
    "dolphin",
    "donkey",
    "crow",
    "crocodile",
]

other_animals = [
    "badger",
    "cow",
    "pig",
    "sheep",
    "bee",
    "wolf",
    "fox",
    "whale",
    "shark",
    "fish",
    "turkey",
    "duck",
    "dove",
    "deer",
    "elephant",
    "frog",
    "falcon",
    "goat",
    "gorilla",
    "hawk",
]


def bloom_filter():
    bloom_filter = BloomFilter(size=1000)

    for animal in animals:
        bloom_filter.add(animal)

    print(f'capacity: {bloom_filter.size}\ninserted items: {len(bloom_filter)}\nfilter size: {bloom_filter.filter_size}\nfalse-positive probability: {bloom_filter.fp_prob}\nhash functions count: {bloom_filter.num_hashes}')

    for animal in animals + other_animals:
        if animal in bloom_filter:
            if animal in other_animals:
                print(f"'{animal}' is a false positive case. Adjust fp to smaller value.")
            else:
                print(f"'{animal}' is probably in filter.")
        else:
            print(f"'{animal}' is definitely not in the filter as expected.")

    with open('bloom_filter.bin', 'wb') as fp:
        bloom_filter.save(fp)

    with open('bloom_filter.bin', 'rb') as fp:
        bloom_filter = BloomFilter.load(fp)


if __name__ == '__main__':
    bloom_filter()
