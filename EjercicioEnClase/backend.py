from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import json

file_json = FileSystemLoader('templates')
environment = Environment (loader=file_json)

app = Flask (__name__)
with open ('data.json') as json_file:
    info_json = json.load (json_file)


def message():
    msg = 'Hola desde el metodo'
    return "alert('" + msg + "')"

@app.route ('/')
def index ():
    temp = environment.get_template('index.html')
    return temp.render (my_data = info_json['data'], headers = info_json['headers'])

@app.route ('/Create', methods = ['GET', 'POST'])
def add ():
    if request.method == 'POST':
        idnum = request.form ['id']
        Class = request.form ['type']
        name = request.form ['name']
        img = request.form ['image']
        thumbnail = request.form ['thumbnail']
        print (f'{number}{Class}{name}{image}{thumbnail}')

        json_file['data'].append({"id":idnum, "type":Class, "name":name, "image":{"url":image}, "thumbnail":{"url":thumbnail}})
        return redirect(url_for('index'))
    temp = environment.get_template('form.html')
    return temp.render()

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug = True)


