import google.generativeai as genai
import os
from pathlib import Path
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)


app = Flask(__name__)

def GetTitle(p):
   if p.find("Lesson") != -1:      
      return "Lesson"
   else:
      return p


def GetResponse(p):
   if p.find("Lesson") != -1:
      return "You must have the correct title in your code"
   else:
      return 'Your namespace is wrong. The correct namespace is ' + p  

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['GET','POST'])
def hello():
   lessons_array = ['Lesson01', 'Lesson02', 'Lesson03', 'Lesson04', 'Lesson05', 'Lesson06', 'Lesson07', 'Lesson08', 'Lesson09', 'Lesson10', 'Lesson11', 'Lesson12', 'Lesson13', 'Lesson14', 'Lesson15'] 
   exercises_array = ['Ex1', 'Ex2', 'Ex3', 'Ex4', 'Ex5']    
   lesson = ' '
   exercise = ' '   
   if request.method == 'POST':
      Program = request.form.get('Program') 
      lesson = request.form.get('lesson')
      exercise = request.form.get('exercise')
      project_name = lesson + exercise
      filename = lesson + exercise + '.txt'
      my_file = Path(filename)
      if my_file.is_file():
         f = open(filename, "r")
         solution = f.read()    
      else:
         return render_template('hello.html', Program = Program, response_text = 'Exercise not found', lessons_array=lessons_array, exercises_array=exercises_array, lesson=lesson, exercise=exercise, previous_lesson=lesson, previous_exercise = exercise)                 
      if Program:
         print(GetTitle(project_name))

         if Program.find(GetTitle(project_name)) != -1:
            genai.configure(api_key="YOUR API KEY")
            model = genai.GenerativeModel('gemini-2.5-pro')           
            filename = lesson + exercise + '.txt'
            my_file = Path(filename)  
            prompt = 'This is the solution '
            prompt += solution
            prompt += 'This is the student program '
            prompt += Program
            prompt += ' Check every line of code except comments. '
            prompt += ' Ignore the line with <h1>.'
            prompt += ' If the programs are identical, only reply No mistakes found and say a compliment. '
            prompt += ' If the variable and function names are different, but both programs work the same way, reply No mistakes found and say a compliment. '
            prompt += ' Otherwise, point out the mistakes in the student program.'
            response = model.generate_content(prompt)
            print(prompt)
            return render_template('hello.html', Program = Program, response_text = response.text, lessons_array=lessons_array, exercises_array=exercises_array, lesson=lesson, exercise=exercise, previous_lesson=lesson, previous_exercise = exercise)
         else:
            return render_template('hello.html', Program = Program, response_text = GetResponse(project_name), lessons_array=lessons_array, exercises_array=exercises_array, lesson=lesson, exercise=exercise, previous_lesson=lesson, previous_exercise = exercise)  
      else:
         return render_template('hello.html', Program = Program, response_text = 'You must enter your program', lessons_array=lessons_array, exercises_array=exercises_array, lesson=lesson, exercise=exercise, previous_lesson=lesson, previous_exercise = exercise)
   else:
      return render_template('hello.html', lessons_array=lessons_array, exercises_array=exercises_array, lesson=lesson, exercise=exercise)


if __name__ == '__main__':
   app.run()





