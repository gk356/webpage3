from flask import Flask, request, redirect, url_for, render_template
from flask import flash
import pytest
#from content_management import Content
#import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


# Input Sanitization for BMI function
def sanitize_h(height):
    
    feet, inches = height.split("'")
    total_height = 12*float(feet) + float(inches.strip('"'))
    #height_m = total_height*0.025
    #height_m = round(height_m,2)
    return total_height

def sanitize_w(weight):
    weight_inkg = float(weight)
    #*0.45
    #weight_inkg = round(weight_inkg,2)
    return weight_inkg

# def is_float(field):
#     return re.match('[+-]?[0-9]+\.[0-9]+', field)


#From Submission Route
@app.route("/bmi", methods=["POST", "GET"])
def bmi():    
    if(request.method == 'POST'):
       
        height = request.form['height']
        
        ht = sanitize_h(height)
         
        weight = request.form['weight']
        
        wgt = sanitize_w(weight)     
        

        bodyMI = cal_bmi(ht, wgt)
        #render_template("index.html", body = bodyMI)
        # bodyMI = wgt/(ht*ht)
        # bodyMI = round(bodyMI,1)

        if(round(bodyMI,2) <= 18.5):
            category = "Your are Under Weight"
            prompt = "Your body mass index is " + str(round(bodyMI,2)) + " ."
            return render_template("index.html", body=prompt, cat=category)

        elif(round(bodyMI,2) >= 18.5 and round(round(bodyMI,2)) <= 24.9):
            category = "You are Normal Weight"
            prompt = "Your body mass index is " + str(round(bodyMI,2)) + " ."
            return render_template("index.html", body=prompt, cat=category)

        elif(round(bodyMI,2) >= 25 and round(bodyMI,2) <= 29.9):
            category = "Your Over Weight"
            prompt = "Your body mass index is " + str(round(bodyMI,2)) + " ."
            return render_template("index.html", body=prompt, cat=category)
        elif(round(bodyMI,2) > 29.9):
            category = "Your are Obese"
            prompt = "Your body mass index is " + str(round(bodyMI,2)) + " ."
            return render_template("index.html", body= prompt, cat = category)

        else:
            return render_template("index.html")

def cal_bmi(ht, wgt):
    height_m = ht*0.025
    height_m = round(height_m,2)

    weight_inkg = wgt*0.45
    weight_inkg = round(weight_inkg,2)

    results = weight_inkg/(height_m*height_m)
    results = round(results,2)
    #print(results)
    #results = round(results,1)
    return results
    

@app.route("/retirement", methods=["POST", "GET"])
def retirment():
    if request.method == "POST":
        current_age = request.form['currentage']
        current_age = int(current_age)

        annual_salary = request.form['annualsalary']
        annual_salary = int(annual_salary)

        percent_save = request.form['percentsave']
        percent_save = int(percent_save)
        
        save_goal = request.form['savegoal']
        save_goal = int(save_goal)

        # savings = annual_salary + (0.15*annual_salary)
        # saving_percent = round(percent_save/100,2)
        # after_savings = savings + (saving_percent * savings)
        # year_to_save = round(save_goal/after_savings,2)
        # meet_year = round(year_to_save + current_age,2)
        meet_year = cal_retirement(annual_salary, percent_save, save_goal,current_age)
        if meet_year > 100:
            message = "You will not meet your goal. "
            return render_template("index.html", message = message)
        else:
            message = "You will meet your goal by " + str(meet_year) + " years." 
            return render_template("index.html", message = message)



def cal_retirement(annual_salary, percent_save, save_goal,current_age ):
    savings = annual_salary + (0.15*annual_salary)
    saving_percent = round(percent_save/100,2)
    after_savings = savings + (saving_percent * savings)
    year_to_save = round(save_goal/after_savings,2)
    meet_year = round(year_to_save + current_age,2) 
    return meet_year   
        


if __name__ == "__main__":
    app.run(debug=True)



    
    





##height
##weight

 