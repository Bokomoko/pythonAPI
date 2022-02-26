# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Create an Flask API that returns the phonetic portuguese pronounciation of a word.
def get_pronounciation(word):
    url = 'https://api.dictionaryapi.dev/api/v1/entries/en/{}'.format(word)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]['pronunciation']
    else:
        return None

# create a flask app with route /pronounciation and a function that returns the pronounciation of the word
app = Flask(__name__)
app.route('/pronounciation')
def get_pronounciation(word):
    url = 'https://api.dictionaryapi.dev/api/v1/entries/en/{}'.format(word)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]['pronunciation']
    else:
        return None