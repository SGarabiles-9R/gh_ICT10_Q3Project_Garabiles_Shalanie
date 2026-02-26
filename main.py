from pyscript import display, document

# ----------- LOGIN (GATE THAT SHOWS UP FIRST)-----------
accounts = {}

def checking_account(e):
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    result = document.getElementById("account-output")
    result.innerHTML = ""

    if len(username) >= 7:
        if len(password) >= 10:

            has_letter = False
            has_number = False

            for char in password:
                if char.isalpha():
                    has_letter = True
                if char.isdigit():
                    has_number = True

            if has_letter and has_number:
                accounts["username"] = username
                accounts["password"] = password

                display("Congratulations! you now have an account", target="account-output")

                # hide login section
                document.getElementById("account-section").style.display = "none"
                
                # Show tabs section
                document.getElementById("tabs-section").style.display = "block"

                # the intiator for the 2nd css/logged in
                document.querySelector("body").classList.add("logged-in")

            else:
                display("Password must contain at least a number and letter", target="account-output")
        else:
            display("Password must contain 10 characters", target="account-output")
    else:
        display("Username must be at least 7 characters long", target="account-output")


# ----------- TEAM CHECKER / 1st tab -----------
def check_team(e):
    if "username" not in accounts:
        display("Please create an account first!", target="output")
        return

    # getting the value of like the input field, and then confirming it a variables
    registered = document.querySelector('input[name="registration"]:checked')
    medical = document.querySelector('input[name="clear"]:checked')
    grade = document.getElementById("level").value
    section = document.getElementById("section").value
    document.getElementById("output").innerHTML = ""
    document.getElementById("image").innerHTML = ""


    # is none" is when the input is no value/null
    if registered is None or medical is None:
        display("Please select registration and medical clearance options.", target="output")
        return

    registered = registered.value
    medical = medical.value
    output = document.getElementById("output")

    if registered == "No":
        display("Please register first before joining any team.", target="output")

    elif medical == "No":
        display("Please complete your medical clearance first before joining any team.", target="output")

    elif grade == "lg" or grade == "hg":
        display("Sorry, you cannot join any team due to your grade level.", target="output")

    elif section == "R":
        display("Congrats! You are part of the Blue Bears.", target="output")
        document.getElementById("image").innerHTML = "<img src='sampel.image' height='300' width='200'>"

    elif section == "E":
        display("Congrats! You are part of the Yellow Hornets.", target="output")
        document.getElementById("image").innerHTML = "<img src='sampel.image' height='300' width='200'>"

    elif section == "S": 
        display("Congrats! You are part of the Red Bulldogs.", target="output")
        document.getElementById("image").innerHTML = "<img src='sampel.image' height='300' width='200'>"

    elif section == "T":
        display("Congrats! You are part of the Green Hornets.", target="output")
        document.getElementById("image").innerHTML = "<img src='sampel.image' height='300' width='200'>"


# ----------- players (dwayne) -----------
def players_list(e):
    if "username" not in accounts:
        display("Please create an account first!", target="result")
        return

    names = ["Nardo","Galang", "Oliveros", "Cabatingan", "Villegas", "Baylon", "Canete", 
             "Garabiles", "Dimaculangan", "Ong", "Yao", "Evangelista", "Villafuerte", 
             "Sangreo", "Ala", "Baring", "Olmedo", "Broadhagen", "Rebadulla", "Reyes", 
             "Jamet", "Gonzalez", "Ledesma", "Agena", "Nacino", "Tarachand", "Cervantes"]

    document.getElementById("result").innerHTML = ""  # so like theres no duplicates
    for i, name in enumerate(names, start=1):

        display(f"{i}. {name}", target="result")
