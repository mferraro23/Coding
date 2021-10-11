import json
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

siteURL = ""

def checkoutProcess():
    checkout = driver.find_element_by_class_name("PSRHhd")
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(checkout).click(checkout).perform()

def choiceApps():
    appOptions = [
        "Fried Calamari",
        "Our Famous Wings",
        "4 Piece Garlic Rolls",
        "5 Piece Mozzarella Sticks",
        "4 Piece Garlic Rolls With Sauce",
        "Eggplant",
        "French Fries",
        "Broccoli Rabe",
        "Onion Rings",
        "Chicken Fingers With Fries",
        "Clams",
        "Mussels",
        "Shrimp Basket",
        "Meatballs",
        "Sausages",
        "Eggplant Layers"
    ]
    time.sleep(2)
    n = 1
    for i in appOptions:

        print("#", n, ":", appOptions[n-1])
        n = n + 1

    optionFood = int(input("What do you want to order? (enter the option #)"))
    time.sleep(2)
    optionFood = optionFood - 1
    appChoice = appOptions[optionFood]
    print("Do you want to add ", appChoice, "to your order?")
    y = input("(Enter 'y or n' to continue: )").lower()

    if y == "y" or "yes":
        f = open('food.json',)
        data = json.load(f)

        item = str(data['food_apps'][optionFood])
        itemID = item.split(':')[1].lstrip().split(' ')[
            0].lstrip('"').rstrip('"}')

        time.sleep(2)

        addFood = driver.find_element_by_id(itemID[1:-1])
        driver.implicitly_wait(10)
        ActionChains(driver).move_to_element(addFood).click(addFood).perform()

        if appChoice == "Broccoli Rabe":
            choiceBroccoliRabe = input(
                "Do you want your Broccoli Rabe Steamed or with Garlic Oil?").lower()
            if choiceBroccoliRabe == "steamed":
                steamed = driver.find_element_by_id("c476")
                steamed.click()
            elif choiceBroccoliRabe == "garlic oil" or "garlic" or "oil":
                garlic = driver.find_element_by_id("c482")
                garlic.click()
        if appChoice == "Our Famous Wings":
            choiceWings = input("How many wings do you want? 4, 8, 10, or 12?")
            if choiceWings == "4":
                amntWings = driver.find_element_by_id("c492")
                amntWings.click()
            elif choiceWings == "8":
                amntWings = driver.find_element_by_id("c497")
                amntWings.click()
            elif choiceWings == "10":
                amntWings = driver.find_element_by_id("c502")
                amntWings.click()
            elif choiceWings == "12":
                amntWings = driver.find_element_by_id("c508")
                amntWings.click()
            choiceWingsSauce = input(
                "What sauce would you like on the wings? (Plain, Buffalo Sauce, BBQ Sauce, Buffalo and BBQ Mix Sauce, Honey Mustard Sauce, Italian Creamy Sauce, Italian Creamy Parmesan Sauce, or Pesto Sauce)").lower()
            if choiceWingsSauce == 'plain' or 'plain sauce':
                wingSauce = driver.find_element_by_id("c513")
                wingSauce.click()
            elif choiceWingsSauce == 'buffalo' or 'buffalo sauce':
                wingSauce = driver.find_element_by_id("c518")
                wingSauce.click()
            elif choiceWingsSauce == 'bbq sauce' or 'bbq':
                wingSauce = driver.find_element_by_id("c522")
                wingSauce.click()
            elif choiceWingsSauce == 'buffalo and bbq mix sauce' or 'buffalo and bbq sauce' or 'buffalo and bbq mix' or 'buffalo & bbq sauce' or 'buffalo & bbq sauce mix' or 'buffalo & bqq mix' or 'buffalo & bbq sauce':
                wingSauce = driver.find_element_by_id("c528")
                wingSauce.click()
            elif choiceWingsSauce == 'honey' or 'honey mustard' or 'honey mustard sauce':
                wingSauce = driver.find_element_by_id("c533")
                wingSauce.click()
            elif choiceWingsSauce == 'italian creamy sauce' or 'creamy italian':
                wingSauce = driver.find_element_by_id("c538")
                wingSauce.click()
            elif choiceWingsSauce == 'italian creamy parm' or 'italian creamy parmesan sauce' or 'creamy parmesan sauce' or 'italian parmesan sauce':
                wingSauce = driver.find_element_by_id("c543")
                wingSauce.click()
            elif choiceWingsSauce == 'pesto' or 'pesto sauce':
                wingSauce = driver.find_element_by_id("c548 ")
                wingSauce.click()

        time.sleep(2)
        addToCart = driver.find_element_by_class_name("ulVjFf")
        driver.implicitly_wait(10)
        ActionChains(driver).move_to_element(
            addToCart).click(addToCart).perform()

        print("We added  ", appChoice, "to your cart.\n")
        n = input("Is there anything else you want? ").lower()
        time.sleep(2)
        if n == "y" or "yes":
            review = input("Ok what do you want to order?").lower()
            if review == 'pizza':
                choicePizza()

            elif review == 'salads':
                choiceSalad()

            elif review == "appetizers" or "apps":
                choiceApps()

            elif review == "pasta":
                choicePasta()

            elif review == "entrees":
                choiceEntrees()

            elif review == "subs" or "hot subs" or "cold subs" or "hot and cold subs":
                choiceSubs()

        elif n == "n" or "no":
            checkoutProcess()
            driver.close()

def choicePizza():
    pizzaList = [
        "Margherita Pizza",
        "Buffalo Chicken Pizza",
        "Cheese Pizza",
        "Brooklyn style thin crust",
        "Tomato Pizza",
        "White Ricotta Pizza",
        "White Pizza",
        "Hawaiian Pizza",
        "Homestyle Pizza",
        "Bruschetta Pizza",
        "Steak Pizza",
        "Chicken Pizza",
        "Chicken, Broccoli & Garlic Pizza",
        "Chicken, Bacon & Ranch Pizza",
        "Chicken Caesar Pizza",
        "BBQ Steak Pizza",
        "BBQ Chicken Pizza",
        "Honey Mustard Chicken Pizza",
        "4 Cheese Pizza"
    ]

    askPizzaType = input(
        'What pizza do you want? (Enter either 14" 16" 18" Personal or Slice.\n')
    if askPizzaType == '14"' or '14" artisan pizza' or '14" pizza' '14" artisan':
        n = 1
        for i in pizzaList:
            print("#", n, ":", pizzaList[n-1])
            n = n + 1
        optionFood = int(
            input('What 14" pizza would you like? (enter the option #)\n'))
        time.sleep(2)
        optionFood = optionFood - 1
        appChoice = pizzaList[optionFood]
        print("Do you want to add ", appChoice, "to your order?")
        y = input("(Enter 'y or n' to continue: )").lower()

        if y == "y" or "yes":
            f = open('food.json',)
            data = json.load(f)

            item = str(data['pizza_14'][optionFood])
            itemID = item.split(':')[1].lstrip().split(' ')[
                0].lstrip('"').rstrip('"}')
            itemID.lstrip("'").rstrip("'")

            time.sleep(2)

            addFood = driver.find_element_by_id(itemID[1:-1])
            addFood.click()
            time.sleep(2)
            addToCart = driver.find_element_by_class_name("ulVjFf")
            driver.implicitly_wait(10)
            ActionChains(driver).move_to_element(
                addToCart).click(addToCart).perform()
            # addToCart.click()
            print("We added  ", appChoice, "to your cart.\n")
            n = input("Is there anything else you want? ").lower()
            time.sleep(2)
            if n == "y" or "yes":
                review = input("Ok what do you want to order?").lower()
                if review == 'pizza':
                    choicePizza()

                elif review == 'salads':
                    choiceSalad()
                elif review == "appetizers" or "apps":
                    choiceApps()
                elif review == "pasta":
                    choicePasta()
                elif review == "entrees":
                    choiceEntrees()
                elif review == "subs" or "hot subs" or "cold subs" or "hot and cold subs":
                    choiceSubs()
                else:
                    print("finish later")
                    driver.close()

    elif askPizzaType == '16"' or '16" artisan pizza' or '16" pizza' '16" artisan':
        n = 1
        for n in pizzaList:
            print("#", n, ":", pizzaList[n-1])
            n = n + 1
        optionFood = int(
            input('What 16" pizza would you like? (enter the option #)\n'))
        time.sleep(2)
        optionFood = optionFood - 1
        appChoice = pizzaList[optionFood]
        print("Do you want to add ", appChoice, "to your order?")
        y = input("(Enter 'y or n' to continue: )").lower()
        if y == "y" or "yes":
            f = open('food.json',)
            data = json.load(f)

            item = str(data['pizza_16'][optionFood])
            itemID = item.split(':')[1].lstrip().split(' ')[
                0].lstrip('"').rstrip('"}')
            itemID.lstrip("'").rstrip("'")

            time.sleep(2)

            addFood = driver.find_element_by_id(itemID[1:-1])
            addFood.click()
            time.sleep(2)
            addToCart = driver.find_element_by_class_name("ulVjFf")
            driver.implicitly_wait(10)
            ActionChains(driver).move_to_element(
                addToCart).click(addToCart).perform()

            print("We added  ", appChoice, "to your cart.\n")
            n = input("Is there anything else you want? ").lower()
            time.sleep(2)
            if n == "y" or "yes":
                review = input("Ok what do you want to order?").lower()
                if review == 'pizza':
                    choicePizza()

                elif review == 'salads':
                    print("choiceSalad()")
                elif review == "appetizers" or "apps":
                    print("choiceApps()")
                elif review == "pasta":
                    print("choicePasta()")
                elif review == "entrees":
                    print("choiceEntrees")
                elif review == "subs" or "hot subs" or "cold subs" or "hot and cold subs":
                    print("choiceSubs()")
                else:
                    print("finish later")
                    driver.close()
    elif askPizzaType == '18"' or '18" artisan pizza' or '18" pizza' '18" artisan':
        n = 1
        for n in pizzaList:
            print("#", n, ":", pizzaList[n-1])
            n = n + 1
        optionFood = int(
            input('What 18" pizza would you like? (enter the option #)\n'))
        time.sleep(2)
        optionFood = optionFood - 1
        appChoice = pizzaList[optionFood]
        print("Do you want to add ", appChoice, "to your order?")
        y = input("(Enter 'y or n' to continue: )").lower()
        if y == "y" or "yes":
            f = open('food.json',)
            data = json.load(f)

            item = str(data['pizza_18'][optionFood])
            itemID = item.split(':')[1].lstrip().split(' ')[
                0].lstrip('"').rstrip('"}')
            itemID.lstrip("'").rstrip("'")

            time.sleep(2)

            addFood = driver.find_element_by_id(itemID[1:-1])
            addFood.click()
            time.sleep(2)
            addToCart = driver.find_element_by_class_name("ulVjFf")
            driver.implicitly_wait(10)
            ActionChains(driver).move_to_element(
                addToCart).click(addToCart).perform()

            print("We added  ", appChoice, "to your cart.\n")
            n = input("Is there anything else you want? ").lower()
            time.sleep(2)
            if n == "y" or "yes":
                review = input("Ok what do you want to order?").lower()
                if review == 'pizza':
                    choicePizza()

                elif review == 'salads':
                    choiceSalad()

                elif review == "appetizers" or "apps":
                    choiceApps()

                elif review == "pasta":
                    choicePasta()

                elif review == "entrees":
                    choiceEntrees()

                elif review == "subs" or "hot subs" or "cold subs" or "hot and cold subs":
                    choiceSubs()

                else:
                    print("finish later")
                    driver.close()
    elif askPizzaType == 'personal' or 'personal pizza':
        n = 1
        for n in pizzaList:
            print("#", n, ":", pizzaList[n-1])
            n = n + 1
        optionFood = int(
            input('What personal pizza would you like? (enter the option #)\n'))
        time.sleep(2)
        optionFood = optionFood - 1
        appChoice = pizzaList[optionFood]
        print("Do you want to add ", appChoice, "to your order?")
        y = input("(Enter 'y or n' to continue: )").lower()
        if y == "y" or "yes":
            f = open('food.json',)
            data = json.load(f)

            item = str(data['pizza_personal'][optionFood])
            itemID = item.split(':')[1].lstrip().split(' ')[
                0].lstrip('"').rstrip('"}')
            itemID.lstrip("'").rstrip("'")

            time.sleep(2)

            addFood = driver.find_element_by_id(itemID[1:-1])
            addFood.click()
            time.sleep(2)
            addToCart = driver.find_element_by_class_name("ulVjFf")
            driver.implicitly_wait(10)
            ActionChains(driver).move_to_element(
                addToCart).click(addToCart).perform()

            print("We added  ", appChoice, "to your cart.\n")
            n = input("Is there anything else you want? ").lower()
            time.sleep(2)
            if n == "y" or "yes":
                review = input("Ok what do you want to order?").lower()
                if review == 'pizza':
                    choicePizza()

                elif review == 'salads':
                    choiceSalad()

                elif review == "appetizers" or "apps":
                    choiceApps()

                elif review == "pasta":
                    choicePasta()

                elif review == "entrees":
                    choiceEntrees()

                elif review == "subs" or "hot subs" or "cold subs" or "hot and cold subs":
                    choiceSubs()
                else:
                    print("finish later")
                    driver.close()
    elif askPizzaType == 'slice' or 'by the slice' or 'by slice':
        n = 1
        for i in pizzaList:
            print("#", n, ":", pizzaList[n-1])
            n = n + 1
        optionFood = int(
            input('What slice pizza would you like? (enter the option #)\n'))
        time.sleep(2)
        optionFood = optionFood - 1
        appChoice = pizzaList[optionFood]
        print("Do you want to add ", appChoice, "to your order?")
        y = input("(Enter 'y or n' to continue: )").lower()
        if y == "y" or "yes":
            f = open('food.json',)
            data = json.load(f)

            item = str(data['pizza_slice'][optionFood])
            itemID = item.split(':')[1].lstrip().split(' ')[
                0].lstrip('"').rstrip('"}')
            itemID.lstrip("'").rstrip("'")

            time.sleep(2)

            addFood = driver.find_element_by_id(itemID[1:-1])
            addFood.click()
            time.sleep(2)
            addToCart = driver.find_element_by_class_name("ulVjFf")
            driver.implicitly_wait(10)
            ActionChains(driver).move_to_element(
                addToCart).click(addToCart).perform()

            print("We added  ", appChoice, "to your cart.\n")
            n = input("Is there anything else you want? ").lower()
            time.sleep(2)
            if n == "y" or "yes":
                review = input("Ok what do you want to order?").lower()
                if review == 'pizza':
                    choicePizza()

                elif review == 'salads':
                    choiceSalad()

                elif review == "appetizers" or "apps":
                    choiceApps()

                elif review == "pasta":
                    choicePasta()

                elif review == "entrees":
                    choiceEntrees()

                elif review == "subs" or "hot subs" or "cold subs" or "hot and cold subs":
                    choiceSubs()

                else:
                    print("finish later")
                    driver.close()

    else:
        print("ERROR")

def choiceEntrees():
    print("does nothing yet")

def choiceSalad():
    print("does nothing yet")

def choicePasta():
    print("does nothing yet")

def choiceSubs():
    print("does nothing yet")


choiceOrder = input(
    "Do you want to pick up your order or have it delivered? \n").lower()
time.sleep(2)


if (choiceOrder == "pick up" or "pickup" or "pick-up"):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome()
    siteURL = ("https://food.google.com/chooseprovider?restaurantId=/g/1tcxf3dw&hl=en-US&gl=us&cs=1&ssta=1&fo_m=MfohQo559jFvMWwP9igWZeWQMczq7voErUdXMT_RFPQ05bfKMQVr5-7IofUJMU_hT8vrWuwRMUOzJVpjPL1YMfaXTPp5KXh-OAE%3D&gei=RPlNYdqNL-PB_Qb224zgCA&fo_s=OA,AH&orderType=2&sei=CXOeg4KHbv-eEWRLD3Wg9SOp&utm_campaign&utm_source=search")
    driver.get(siteURL)
    startFood = input(
        'Do you want Appetizers, Salads, Pasta, Pizza, Entrees, or Hot & Cold Subs?\n').lower()
    if startFood == ("apps" or "appetizers"):
        choiceApps()
    elif startFood == 'pizza':
        choicePizza()
    elif startFood == 'salad' or 'salads':
        choiceSalad()
    elif startFood == 'pasta':
        choicePasta()
    elif startFood == 'entrees' or 'entree':
        choiceEntrees()
    elif startFood == 'subs' or 'hot and cold subs' or 'hot & cold subs' or 'hot and cold' or 'hot & cold' or 'sub' or 'hot and cold sub' or 'hot & cold sub':
        choiceSubs()


elif(choiceOrder == "delivery" or "delivered"):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome()
    siteURL = ("https://food.google.com/chooseprovider?restaurantId=/g/1tcxf3dw&hl=en-US&gl=us&cs=1&ssta=1&fo_m=MfohQo559jFvMWwP9igWZeWQMczq7voErUdXMT_RFPQ05bfKMQVr5-7IofUJMU_hT8vrWuwRMUOzJVpjPL1YMfaXTPp5KXh-OAE%3D&gei=RPlNYdqNL-PB_Qb224zgCA&sei=CXOeg4KHbv-eEWRLD3Wg9SOp&utm_campaign&utm_source=search&addressId=-9080876262808778934&orderType=1&partnerId=07382683665824229530&fulfillmentTime&menuSearchQuery&cartId&fo_s=OA%2CAH&dineInLocationId")
    driver.get(siteURL)
    # driver.quit()
