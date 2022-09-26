# ====================================================================================================
# HERE WE GOING ]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
# ====================================================================================================

# All libraries that we need
import os
import time
import pyttsx3
import requests
import pandas as pd
from bs4 import BeautifulSoup
import speech_recognition as sr


def main():  # main() def to restart the code incase user want to scrape more

    def wishMe():

        # Male voice
        engM = pyttsx3.init()
        voice = engM.getProperty('voices')
        engM.setProperty('voice', voice[0].id)

        # Intro of Beast Boi
        print("\nBeastBoi X DNA")
        print("Hello!! It's Beast Boy here")
        engM.say("Hello!! It's Beast Boy here")
        engM.runAndWait()
        # This is the command |||||| 'i want to scrape the web pages' ||||||
        engM.say("Tell me how may i help you??")
        engM.runAndWait()

    # It takes microphone input from the user and returns string output
    def takeCommand():
        extra_spaces = ' ' * 10
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\rListening...", end="")
            # time.sleep(2)
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("\rRecognizing...", end="")
            query = r.recognize_google(audio, language='en-in')
            print(f"\rNoted: {query}", end='')
            time.sleep(2)
            print("\rYour request has been forwarded to -:| DNA |:-")
        except Exception as e:
            # print(e)
            print("\rSay that again please...")
            return "None"
        return query

    def DNA():

        # Female voice
        engF = pyttsx3.init()
        voice = engF.getProperty('voices')
        engF.setProperty('voice', voice[1].id)

        print(
            "\nHello sir!! I'm DNA!! I've received your request from our --[|BEAST|]-- Boy."
        )
        engF.say(
            "Hello sir!! I'm DNA!!.  I've received your request from our Beast Boy"
        )
        engF.runAndWait()

        print(
            "Please tell me your requirements regarding to the web page scraping."
        )
        engF.say(
            "Please tell me your requirements regarding to the web page scraping, Okay?"
        )
        engF.runAndWait()

        extra_spaces = ' ' * 30

        # Lists Section
        topic_list = [
            'data-visualization', 'react', 'java', 'json', 'javascripts',
            'python', 'graphql', 'machine-learning', 'flask'
        ]

        sp_topic_list = ['postgressql']
        nolist = ['Nope', 'N', 'n', 'nope']
        yeslist = ['yeah', 'y', 'Yeah', 'yes']

        # to clear previous output from the terminal
        clear = lambda: os.system("cls")
        # if 1:

        print("\nHere we going!! Let's scrape the website with Beast Boi Code")
        engF.say(
            "Here we going!! Let's scrape the website with Beast Boy Code")
        engF.runAndWait()
        engF.say("Enter the topic name:")
        engF.runAndWait()

        topic = input('Enter the topic name: ').lower()  # Getting topic name
        print("\rOkay!!", end='')
        time.sleep(0.700)
        print("\rLoading...", end='')
        engF.say("Loading...")
        engF.runAndWait()

        main_url = 'https://github.com/topics'  # Main url incase user asked us to
        base_url = ("https://github.com/topics/" + topic + "?page="
                    )  # Base url ( main topic page url )

        url_list = []

        # To make 8 different webpages
        if topic in topic_list:
            p_val = 8
        elif topic in sp_topic_list:
            p_val = 6
        else:
            clear()
            print('\nEnter correct topic name!!!#$%')
            engF.say("Enter correct topic name")
            engF.runAndWait()
            main()

        for p_num in range(1, p_val):
            url_list.append(base_url + str(p_num))

        time.sleep(0.300)
        print("\rGetting URLs...", end='')
        engF.say("Getting URLs..")
        engF.runAndWait()
        first30name = []
        time.sleep(2)
        print("\rConverting data to readable format...", end='')
        engF.say("Converting data to readable format...")
        engF.runAndWait()
        time.sleep(4)
        print("\rDone!   " + extra_spaces, end='')
        engF.say("Done!")
        engF.runAndWait()
        time.sleep(0.500)
        print("\rScraping data...", end='')
        engF.say("Scraping data...")
        engF.runAndWait()
        start = time.time()
        for url in url_list:
            r = requests.get(url).text
            soup = BeautifulSoup(r, 'lxml')

            # All div classes
            main_divs = soup.find_all(
                'div', class_='d-flex flex-justify-between my-3')

            for items in main_divs:
                all_h3 = items.find_all(
                    'h3', class_='f3 color-fg-muted text-normal lh-condensed')

                # User names
                for owner in all_h3:
                    owner_name = owner.find('a')
                    name = owner_name.text.strip()

                # Repository names
                for reposs in all_h3:
                    repo_name = reposs.find('a',
                                            class_='text-bold wb-break-word')
                    repository = repo_name.text.strip()

                # Repository links
                for links in items.find_all('a',
                                            class_='text-bold wb-break-word',
                                            href=True):
                    repo_links = "https://github.com/" + links['href']

                # Repository Stars
                for star1 in items.find_all('span',
                                            class_='Counter js-social-count'):
                    stars = star1.text.strip()
                    ownername_dict = {
                        'User Name': name,
                        'Repository Name': repository,
                        'Stars': stars,
                        'Repository URL': repo_links
                    }

                first30name.append(ownername_dict)
            df = pd.DataFrame(first30name)

        end = time.time()
        total_time = end - start
        print("\rScraping Time: " + str(total_time) + ":SECONDS\n")
        print("\rScraping Done Successfully!!", end='')
        engF.say("Scraping Done Successfully!!")
        engF.runAndWait()

        def okay_save():

            slash_ver = "\ "
            slash_ver.strip()
            time.sleep(2)
            print(
                "\rWe have successfully scraped all the data you asked us to scrape from "
                + main_url + " for " + topic + " .")
            engF.say(
                "We have successfully scraped all the data you asked us to scrape"
            )
            engF.runAndWait()

            engF.say("Do you want to save scraped data? ")
            engF.runAndWait()
            save_or_not = input("Do you want to save scraped data? ")

            if save_or_not in yeslist:
                folder_path_here = input(
                    "Give the exact path of folder to save data: ")
                file_name = input("Enter file name: ")
                file_extension = input("Enter file extension: ")

                df.index = df.index + 1
                # df.to_excel((folder_path_here + slash_ver + file_name + "." +
                #              file_extension),
                #             index_label='Sr No.')
                # Deleting 10 extra rows from Data Frame
                update_df = df.drop(
                    index=[201, 202, 203, 204, 205, 206, 207, 208, 209, 210])

                reindex_df = update_df.reset_index(drop=True)
                reindex_df.index = reindex_df.index + 1
                reindex_df.to_excel((folder_path_here + slash_ver + file_name +
                                     "." + file_extension),
                                    index_label='Sr No.')

            elif save_or_not in nolist:
                engF.say("Really do not want to save? ")
                engF.runAndWait()
                really_not = input("Really do not want to save? ")

                if really_not in yeslist:
                    print("Okay let's save the data!")
                    engF.say("Okay let's save the data!")
                    engF.runAndWait()
                    folder_path_here = input(
                        "Give the exact path of folder to save data: ")
                    file_name = input("Enter file name: ")
                    file_extension = input("Enter file extension: ")
                    df.index = df.index + 1
                    df.to_excel((folder_path_here + slash_ver + file_name +
                                 "." + file_extension),
                                index_label='Sr No.')

                elif really_not in nolist:
                    print("Okay no worries!!!\n")
                    engF.say("Okay no worries!!!")
                    engF.runAndWait()
                    # exit()
                else:
                    clear()
                    print(
                        "Your answer was inappropriate so that's why we going to end our deal here, sorry for your lose, and thank you to visit us have a good day!!! "
                    )
                    engF.say(
                        "Your answer was inappropriate so that's why we going to end our deal here, sorry for your lose, and thank you to visit us have a good day!!! "
                    )
                    engF.runAndWait()
                    exit()  #Modified

            else:
                clear()  #Modified
                print("Your answer was inappropriate!! Try again...")
                time.sleep(2)
                clear()  #Modified
                okay_save()
                # exit()  #Modified2

            if save_or_not in yeslist:
                # clear()
                print("We have successfully saved your data to your computer")
                engF.say(
                    "We have successfully saved your data to your computer")
                engF.runAndWait()

            elif really_not in nolist:
                print("You didn't allow us to save your data!!")
                engF.say("You didn't allow us to save your data!!")
                engF.runAndWait()

            elif save_or_not or really_not in yeslist:
                print("We have successfully saved your data to your computer")
                engF.say(
                    "We have successfully saved your data to your computer")
                engF.runAndWait()

            else:
                clear()
                print("You didn't allow us to save your data!!")
                engF.say("You didn't allow us to save your data!!")
                engF.runAndWait()

        okay_save()

        print("Do you want to scrape any more data from this (" + main_url +
              ") website?")
        engF.say("Do you want to scrape any more data from this website?")
        engF.runAndWait()

        engF.say("If yes say Yeah, If not say Nope ")
        engF.runAndWait()
        restart = input("If yes say Yeah if not say Nope: ").lower()

        # modified
        def option_restart():  #modified
            if restart in yeslist:

                clear()
                print("We're going to restart....")
                engF.say("We're going to restart....")
                engF.runAndWait()
                clear()

                main()

            elif restart in nolist:

                clear()

                # Modified
                def Beast():  #Modified
                    engF.say(
                        "Would you like to know about the code writer Beast Boy? "
                    )
                    engF.runAndWait()
                    bb = input(
                        "\nWould you like to know about the code writer Beast Boi? "
                    )

                    if bb in yeslist:

                        print(
                            "Go and check out the https://github.com/beastboixdna"
                        )
                        engF.say("Go and check out the his Git Hub profile")
                        engF.runAndWait()
                        print("We Done <3\n")
                        exit()

                    elif bb in nolist:

                        print("Never Mind!! Go ahead...")
                        engF.say("Never Mind!! Go ahead..")
                        engF.runAndWait()
                        print("We Done <3\n")
                        exit()

                    else:
                        clear()
                        print('Just enter yes or no')
                        time.sleep(2)
                        clear()
                        Beast()  #Modified

                Beast()


# Modified

            else:
                clear()
                # print("You moron! Do whatever you want. Btw u r bullshit")
                print("Your answer was inappropriate!! ")
                option_restart()
                exit()

        option_restart()  #Modified

        # Modified

        exit()

    # That's it
    if __name__ == "__main__":

        engM = pyttsx3.init()
        voice = engM.getProperty('voices')
        engM.setProperty('voice', voice[0].id)

        wishMe()
        while True:
            # if 1:
            query = takeCommand().lower()

            if 'i want to scrape the web pages' in query:
                engM.say(
                    "Okay sir!, Please talk to DNA to scrape the webpages for you"
                )
                engM.runAndWait()
                DNA()

            elif 'i want to scrape the web page' in query:
                engM.say(
                    "Okay sir!, Please talk to DNA to scrape the webpages for you"
                )
                engM.runAndWait()
                DNA()

            elif 'scrap the web pages' in query:
                engM.say(
                    "Okay sir!, Please talk to DNA to scrape the webpages for you"
                )
                engM.runAndWait()
                DNA()

main()

# =========================================================================================
# HERE I'VE DONE FROM MY SIDE NO MORE CHANGES EVERYTHING HAS SET ||||||||BB X DNA||||||||<3
# =========================================================================================
