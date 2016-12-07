#! /usr/bin/python
import cgi
import cgitb
import myPage

## here we're creating a form with some defaults
def generate_Form(name='', hours=''):
    print("<form method='post'>")
    print("<fieldset>\n")
    print("<legend> Credit Hours </legend>\n")
    print("Enter name: <input type='text' name='name' value='" + name + "'/>\n")
    print("<br  />Credit Hours Earned: <input type='text' name='hours' value='" + hours + "'/>\n")
    print("<input type='submit' name='submitHours' />\n")
    print("</fieldset>\n")
    print("</form>\n")

## defining the main function
## all logic comes through here

def main():
    myPage.printDocHeading("../public_html/threeColStyle.css", "Asg10: Eddie Perez")
    print("<h3>Credit Hours</h3>\n")
    cgitb.enable()
    form=cgi.FieldStorage()
    if (form):
        name=''
        hours=''
        name=form.getfirst('name', '')
        hours=form.getfirst('hours', '')
        if (hours == '' or name == ''):
            print("<h3> You must enter data for both values</h3>\n")
            generate_Form(name,hours)
        else:
            try:
                hours=int(hours)
                print("Your hours: ", str(hours), "<br/>\n")
                if (hours < 29):
                    print("Hi" + name + "You're a freshman")
                elif (hours > 30 or hours < 59):
                    print("Hi" + name + "You're a sophomore")
                elif (hours > 60 or hours < 89):
                    print("Hi" + name + "You're a junior")
                elif (hours >= 90):
                    print("Hi" + name + "You're a sophomore")
            except:
                hours=''
                print("Please enter a whole number of hours. <br />\n")
                generate_Form(name,hours)
    else:
        print("<h4>Please enter data below:</h4>\n")
        generate_Form()

    myPage.printDocFooter()

# here we call the main function
main()
