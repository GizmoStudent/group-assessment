import app

OPTS = {
    "1": "distance",
    "2": "date",
    "3": "category"
}


def sort_option():
    expected = set(['distance', '1',  'date', '2', 'category', '3'])
    while True:
        criteria = input("Please enter a option: \n[1] distance \n[2] date \n[3] category: \n").lower()
        app.main.check_app_commands(criteria.lower())
        if criteria in ['quit', 'q',  '4']:
            app.main.check_app_commands('quit')
        if criteria in expected:
            #print("it is in expected")
            return OPTS[criteria]
        else:
            print('\n\nPlease choose/enter one of the following: \n\n*For distance* 1 \n*For date*  2 \n*For category* 3 \n*To Quit* 4 \n\n')


def ask_to_sort():
    yes = ['yes', 'y']
    no = ['no', 'n']

    while True:
        userInput_ask = input("\n\nDo you want to Sort by Distance, Date or Category? \nPlease Enter 'Y' or 'N'\n\n").lower()
        app.main.check_app_commands(userInput_ask.lower())
        if userInput_ask in yes:
            return True
        elif userInput_ask in no:
            return False
            # sys.exit("Program Terminated \n")
        else:
            print(userInput_ask + " was not recognised." + "\nPlease type only " + ",".join(yes) + "," + ",".join(no))


def check_ext(ui):
    arr = ['.exe', '.csv', '.py', 'txt']
    for value in arr:
        if ui.__contains__(value):
            ui = ui.replace(value, "")
    return ui


def remove_special_chars(ui):
    temp_string = ''
    temp_list = list(ui)
    for item in temp_list:
        if item not in list("[@_!#$%^&*\".()£¬`<>?/\|}{~:])({}~-_''"):
            temp_string = temp_string + item
    return temp_string


def export_name():
    ui = input("What did you want to call the export file: ")
    app.main.check_app_commands(ui.lower())
    ui = check_ext(ui)
    ui = remove_special_chars(ui)
    return ui


if __name__ == '__main__':
    if ask_to_sort():
        print("sorted Value ", sort_option())
