# This is an effort to learn Python by implementing it.
import random
import pycountry
import countryinfo


def capitalGuessing():
    print("welcome to the Capital Guessing game. here are the rules.")
    print("Rules:"
          "\n1. we'll let you choose the number of questions."
          "\n2. once you pick the number of questions we'll ask questions and you have to answer."
          "\n3. final score will be shown at the end of the questions.")

    # Create a mapping of pycountry names to simplified names
    country_mapping = {
        "Bolivia, Plurinational State of": "Bolivia",
        "Venezuela, Bolivarian Republic of": "Venezuela",
        "Korea, Republic of": "South Korea",
        "Korea, Democratic People's Republic of": "North Korea",
        "Russian Federation": "Russia",
        "Taiwan, Province of China": "Taiwan",
        "Iran, Islamic Republic of": "Iran",
        "Syrian Arab Republic": "Syria",
        "Micronesia, Federated States of": "Micronesia",
        "Moldova, Republic of": "Moldova",
        "Congo, The Democratic Republic of the": "Democratic Republic of the Congo",
        "Tanzania, United Republic of": "Tanzania",
        "Holy See (Vatican City State)": "Vatican City",
        "Brunei Darussalam": "Brunei",
        "Türkiye": "Turkey",
        "Viet Nam": "Vietnam",
        "Lao People's Democratic Republic": "Laos",
        "Palestine, State of": "Palestine",
        "Czechia": "Czech Republic",
        "Eswatini": "Swaziland",
        "Timor-Leste": "East Timor"
    }

    countries = [country.name for country in pycountry.countries]
    print(f"select number of questions: 1-{len(countries)}")
    count = int(input())
    questions = random.choices(population=countries, k=count)
    score = 0

    for country, i in zip(questions, range(1, len(questions) + 1)):
        # Clean up country name if it's in our mapping
        clean_country_name = country_mapping.get(country, country)
        print(f"{i}.what is the capital of {country}?\n")

        try:
            country_info = countryinfo.CountryInfo(clean_country_name)
            answer = input("enter your answer: ")
            if answer.lower() == country_info.capital().lower():
                print("Correct Answer!!")
                score += 1
            else:
                print(f"Wrong Answer!! the answer is {country_info.capital()}")
        except:
            print(f"Sorry, we couldn't find capital information for {country}")
            continue

    print(f"your final score is {score}/{count}")


def currencyGuessing():
    print("welcome to the Currency Guessing game. here are the rules.")
    print("Rules:"
          "\n1. we'll let you choose the number of questions."
          "\n2. once you pick the number of questions we'll ask questions and you have to answer."
          "\n3. final score will be shown at the end of the questions.")

    # Same mapping as before for consistency
    country_mapping = {
        "Bolivia, Plurinational State of": "Bolivia",
        "Venezuela, Bolivarian Republic of": "Venezuela",
        "Korea, Republic of": "South Korea",
        "Korea, Democratic People's Republic of": "North Korea",
        "Russian Federation": "Russia",
        "Taiwan, Province of China": "Taiwan",
        "Iran, Islamic Republic of": "Iran",
        "Syrian Arab Republic": "Syria",
        "Micronesia, Federated States of": "Micronesia",
        "Moldova, Republic of": "Moldova",
        "Congo, The Democratic Republic of the": "Democratic Republic of the Congo",
        "Tanzania, United Republic of": "Tanzania",
        "Holy See (Vatican City State)": "Vatican City",
        "Brunei Darussalam": "Brunei",
        "Türkiye": "Turkey",
        "Viet Nam": "Vietnam",
        "Lao People's Democratic Republic": "Laos",
        "Palestine, State of": "Palestine",
        "Czechia": "Czech Republic",
        "Eswatini": "Swaziland",
        "Timor-Leste": "East Timor"
    }

    countries = [country.name for country in pycountry.countries]
    print(f"select number of questions: 1-{len(countries)}")
    count = int(input())
    questions = random.choices(population=countries, k=count)
    score = 0

    for country, i in zip(questions, range(1, len(questions) + 1)):
        clean_country_name = country_mapping.get(country, country)
        print(f"{i}.what is the currency of {country}?\n")

        try:
            country_info = countryinfo.CountryInfo(clean_country_name)
            answer = input("enter your answer: ")
            currencies = [curr.lower() for curr in country_info.currencies()]

            if answer.lower() in currencies:
                print("Correct Answer!!")
                score += 1
            else:
                print(f"Wrong Answer!! the answer is {', '.join(country_info.currencies())}")
        except:
            print(f"Sorry, we couldn't find currency information for {country}")
            continue

    print(f"your final score is {score}/{count}")

def startGame(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print("\t\tWelcome to the Guessing game.")

    gameFlag = True

    while gameFlag == True:
        print("Select one of the options by typing the number:\n"
              "1. Number Guessing.\n"
              "2. Country capital Guessing.\n"
              "3. Country Currency Guessing.\n"
              "4. quit the whole thing."
              )
        option = int(input("your option here: "))
        if option == 1:
            print("\t\tyou have chosen to play the Number guessing.")
            numberGuessing()
        elif option == 2:
            capitalGuessing()
        elif option == 3:
            currencyGuessing()
        elif option == 4:
            gameFlag = False
            print("Thanks for playing the game!!")


def numberGuessing():
    print("welcome to the Number Guessing game. here are the rules.")
    print("you must guess the randomly generated 3 digit number in any number of tries. there will be hints.\n"
          "but if you chose to quit you can do that too..")
    randomNumber = random.randint(1, 999)
    flag = False
    while flag is False:
        answer = int(input("enter value between 1-999 or 0 if you wanna quit: "))
        if answer == randomNumber:
            flag = True
            continue
        elif answer == 0:
            break
        else:
            if answer > randomNumber:
                print("going a little overboard!!")
            else:
                print("underestimating aren't we??")
            print("please try again!!!")
    if flag is True:
        print("you have successfully guessed it!!!")
    else:
        print("we are sad to see you go!! you are a quitter!!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startGame(input('Enter your name:\n'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
