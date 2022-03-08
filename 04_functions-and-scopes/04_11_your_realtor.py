# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def real_estate_ads(greeting,*args):
    infos = []
    for info in args:
        sentence = f"{greeting}! This property has {info}. Feel free to contact me 0210757620."
        infos.append(sentence)
    return infos

hot_deals = real_estate_ads("Happy Easter!", "3 bedrooms, 1 bathroom: 22 Pinehill", "5 bedrooms, 3 bathrooms: 45 Idyll Place", "2 bedrooms, 1 bathroom: 3 Topliss Drive")
print(hot_deals)