from flask import Flask
from caesar import rotate_string

form="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{
                background-color:#eee;
                padding:20px;
                margin:0 auto;
                width:540 px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width:540px;
                height:120px;
            }
        </style>
    </head>
    <body>
        <form method='post'>
            <label for='rot'>Rotate by:</label>
            <input id='rot' type='text' name='rot' value='0'>
            <input name='text' type=textarea>
            <input type='submit' value='Submit message'>
        <!--create your form here-->
    </body>
</html>
"""
app=Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def index():
    return form

app.run()