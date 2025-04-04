# __init__
class Cat:
    pass

cat1 = Cat()
cat1.breed = "Siamese"
cat1.age = 2
cat1.name = "Murka"
cat1.color = "White"

cat2 = Cat()
cat2.breed = "Persian"
cat2.age = 3
cat2.name = "CAT"
cat2.color = "Black"

cat3 = Cat()
cat3.breed = "Maine Coon"
cat3.age = 4
cat3.name = "Luna"
cat3.color = "Gray"

if __name__ == "__main__":
    print("Cat1 -> breed:", cat1.breed, "age:", cat1.age, "name:", cat1.name, "color:", cat1.color)
    print("Cat2 -> breed:", cat2.breed, "age:", cat2.age, "name:", cat2.name, "color:", cat2.color)
    print("Cat3 -> breed:", cat3.breed, "age:", cat3.age, "name:", cat3.name, "color:", cat3.color)

