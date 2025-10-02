from flask import Flask, render_template_string
from motor_system import (
    move_forward, move_backward, turn_left, turn_right, stop_rover_motion
)
import time

app = Flask(__name__)


TPL = """
<!DOCTYPE html>
<html>
<head>
    <title>RPi Rover Control</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f4; }
        .control-btn { 
            display: inline-block; 
            padding: 15px 30px; 
            margin: 10px; 
            font-size: 18px; 
            text-decoration: none; 
            border: none; 
            cursor: pointer; 
            border-radius: 5px; 
            background-color: #007bff; 
            color: white; 
            min-width: 120px;
        }
        .center-row { 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            margin: 10px 0; 
        }
        .stop-btn { background-color: #dc3545; }
        .log { margin-top: 20px; color: #333; }
    </style>
</head>
<body>
    <h1>RASPBERRY PI ROVER CONTROL</h1>
    
    <div class='center-row'>
        <a href='/cmd/forward' class='control-btn'>FORWARD</a>
    </div>
    
    <div class='center-row'>
        <a href='/cmd/left' class='control-btn'>LEFT</a>
        <a href='/cmd/stop' class='control-btn stop-btn'>STOP</a>
        <a href='/cmd/right' class='control-btn'>RIGHT</a>
    </div>
    
    <div class='center-row'>
        <a href='/cmd/backward' class='control-btn'>BACKWARD</a>
    </div>
    
    <hr>
    <div class='log'>Status: {{ message }}</div> 
</body>
</html>
"""

@app.route("/")
def root():
    print("Running sucessfully!")
    return render_template_string(TPL, message="Ready. Start testing your logic!")

@app.route("/cmd/<action>")
def command_action(action):
    response_message = f"Unknown Command: {action}"

    if action == "forward":
        move_forward(speed=60)
        response_message = 'Moving Forward'
    
    elif action == "backward":
        move_backward(speed=60)
        response_message = 'Moving Backwrad'
    
    elif action == "right":
        turn_right(speed=60)
        response_message = 'Turning Right'
    
    elif action == "left":
        turn_left(speed=60)
        response_message= 'Turning Left'

    elif action == "stop":
        stop_rover_motion()
        response_message = 'Stop the Motion'

    time.sleep(0.1)

    return render_template_string(TPL, message=response_message)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
