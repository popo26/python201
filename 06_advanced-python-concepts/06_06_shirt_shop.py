# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

# product = []

# for color in colors:
#     for size in sizes:
#         product.append([color, size])
# print(product)

# product = [(colors[a],sizes[b]) for a in range(len(colors)) for b in range(len(sizes))]

product = [(color, size) for color in colors for size in sizes]
print(product)


