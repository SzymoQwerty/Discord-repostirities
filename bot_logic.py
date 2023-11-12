import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def ekologic_answers():
    which_one = input("Which one? 1-6 ")

    if which_one == 1:
    print("Our adventure with subsequent waste begins at the moment of purchase. How to reduce waste at home? The best way to reduce waste is to choose products without packaging. When going to a store or market, it is worth taking a reusable bag with you, but also smaller nets or boxes in which you can place loose products, fruit or vegetables. Currently, most stores allow you to pack food into your own container, and sometimes the price is several cents lower than using a plastic bag hanging next to the scale. A place where we can buy fresh products without unnecessary packaging is, for example, a local market, any large supermarket and zero waste stores.")
if which_one == 2:
    print("Remember that it is not the colorful packaging, but its content that proves quality. Without a plastic cover, we can easily buy vegetables and fruits, meats and cheeses, groats, nuts, seeds, bread and sweets. Let's give up tea, each sachet of which is packed in foil, vegetables packed individually on a Styrofoam tray and plastic bottles. This is not only a great way to reduce the amount of waste that takes years to decompose, but also an idea for savings. Products by weight are usually much cheaper than those in packages.")
if which_one == 3:
    print("Our planet is littered with plastic, disposable cups, plates and takeaway packaging. How to reduce waste production by making everyday choices? Fortunately, there are great alternatives that will significantly reduce their number. For example, a reusable cup made of durable materials will work perfectly. It will serve us for many years not only during a picnic, but also every day. Manufacturers offer modern models, such as the environmentally safe and compact Stojo, which will fit even into a small handbag. Due to its thermal properties, you can take coffee, tea or cold drinks in it.Instead of buying water in a plastic bottle every day, it is better to choose a good tap water filter and a reusable bottle. The models prepared by Stojo delight with their stylish appearance, but above all, their comfort of use. They are light, foldable and do not take up much space.Disposables surround us at every step, so advice on how to reduce the amount of waste is not limited to obvious choices. We often do not realize that some things can simply be replaced with those less harmful to the environment. An example is a coffee machine. We can choose a model with disposable capsules or choose one that grinds the grains itself.")
if which_one == 4:
    print("Conscious producers use modern patents to reduce waste production in their enterprises. Their efforts are supported by careful sorting of waste, which fortunately is now a necessity. Throwing garbage into appropriate bins contributes to efficient and effective recycling. This, in turn, allows manufacturers to reuse the packaging.When choosing products on store shelves or online, read labels and descriptions. The rule is simple - if a manufacturer has something to be proud of, he will certainly do it. Let's look for information about the origin of the packaging from recycled raw materials. However, the packaging must indicate whether the container is suitable for processing.")
if which_one == 5:
    print("In larger cities and on the Internet we can find zero-waste stores. This means that the products they contain are packed in ecological, glass containers or paper bags. Shopping there is a great way to produce less waste. The owners not only ensure that the customer receives packaging that does not pollute the environment, but also how the products are delivered to the store. The packages in which customers receive products ordered online are also made with zero waste in mind. Often, instead of the classic bubble filling, we find paper shreds of waste paper or remnants of other previously used boxes.When you consider the number of people living in the world, the thought of how much waste we all produce can be terrifying. Let us remember that the choices of each of us can contribute to changing the approach of many other people. Solutions such as a reusable cup or shopping bag turn out to be extremely simple and at the same time very helpful in caring for the environment and the household budget.")
if which_one == 6:
    print("The city authorities have decided that from 2025 only ecological buses will be used in public transport. Ecological transport is the basis for a clean environment for many European cities. This is one of the reasons why many cities have signed the European declaration for the implementation of *clean buses*.")

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
 
