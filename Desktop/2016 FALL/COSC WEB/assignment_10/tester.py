#!/home/eperezcr/virtualenv/python34/3.4/bin/python

import cgi
import cgitb
import myPage


##create a form with default values for field data in the form
def generate_form(name='', hours=''):
    print("<form method='post'> ")
    print("<fieldset>\n")
    print("<legend> hourly work </legend>\n")
    print(" Enter name: <input type='text' name='name' value='" + name + "' />\n")
    print("<br  />Hours worked: <input type='text' name='hours' value='" + hours + "' />\n")
    print("<input type='submit' name='submitHours' />\n")
    print("</fieldset>\n")
    print("</form>\n")


## Define main function
## all logic flows from here
def main():
    myPage.printDocHeading("../css/layout.css", "python example #3 ")
    print("<h3> Hours worked Example </h3>\n")
    cgitb.enable()
    form = cgi.FieldStorage()
    if form:
        name = ''
        hours = ''
        name = form.getfirst('name', '')
        hours = form.getfirst('hours', '')
        if hours == '' or name == '':
            print("<h3> you must enter data for both values </h3>\n")
            generate_form(name, hours)
        else:
            try:
                hours = int(hours)
                print(" Your hours: ", str(hours), "<br />\n")
                if hours > 40:
                    print("Hi " + name + " you worked overtime .. " + str(hours) + " hours")
                else:
                    print("Hi " + name)
                    print(" you worked 40 or less hours, no overtime for ")
                    print(str(hours) + " hours")
            except:
                hours = ''
                print("Please enter a whole number of hours. <br />\n")
                generate_form(name, hours)
    else:
        print("<h4> Please enter data below:</h4>\n")
        generate_form()
    myPage.printDocFooter()


# Call main function  (which is defined earlier in this script)

main()

