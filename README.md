# Rover Brain 

A Python-based control system for a Raspberry Pi rover with a web interface for remote control.

## Overview

This project provides a complete solution for controlling a Raspberry Pi-based rover through a web browser. The system includes motor control, a Flask web server, and a responsive web interface for directional control.

## Features

- **Web-based Control Interface**: Clean, responsive HTML interface with directional buttons
- **Real-time Motor Control**: PWM-based speed control for precise movement
- **Raspberry Pi Compatible**: Native GPIO support with mock mode for development
- **Four-directional Movement**: Forward, backward, left turn, and right turn
- **Emergency Stop**: Immediate halt functionality
- **Cross-platform Development**: Mock GPIO mode for testing without hardware

## Hardware Requirements

- Raspberry Pi (any model with GPIO pins)
- Dual motor setup (left and right motors)
- Motor driver board (e.g., L298N or similar)
- Power supply for motors
- Chassis/frame for the rover

## GPIO Pin Configuration

| Motor | Pin Type | GPIO Pin | Function |
|-------|----------|----------|----------|
| Right Motor | IN1 | GPIO 17 | Direction Control 1 |
| Right Motor | IN2 | GPIO 27 | Direction Control 2 |
| Right Motor | EN | GPIO 22 | PWM Speed Control |
| Left Motor | IN3 | GPIO 23 | Direction Control 1 |
| Left Motor | IN4 | GPIO 24 | Direction Control 2 |
| Left Motor | EN | GPIO 25 | PWM Speed Control |

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/prathoseraaj/rover_brain.git
   cd rover_brain
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install flask RPi.GPIO
   ```

## Usage

### Running the Rover Control System

1. **Start the web server**:
   ```bash
   python main.py
   ```

2. **Access the control interface**:
   - Open a web browser
   - Navigate to `http://<raspberry-pi-ip>:5000`
   - For local access: `http://localhost:5000`

3. **Control the rover**:
   - Use the directional buttons (FORWARD, BACKWARD, LEFT, RIGHT)
   - Use STOP for emergency halt
   - Speed is set to 60% by default

### Development Mode

For development without Raspberry Pi hardware, the system automatically enters mock mode:

```bash
python main.py
```

The mock mode will simulate GPIO operations and print debug information to the console.

### Testing Motor Functions

You can test individual motor functions:

```bash
python motor_system.py
```

This runs a test sequence with forward movement, left turn, and stop.

## File Structure

```
rover_brain/
├── main.py           
├── motor_system.py   
└── README.md         
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main control interface |
| `/cmd/forward` | GET | Move rover forward |
| `/cmd/backward` | GET | Move rover backward |
| `/cmd/left` | GET | Turn rover left |
| `/cmd/right` | GET | Turn rover right |
| `/cmd/stop` | GET | Stop rover movement |

## Configuration

### Speed Control

Default speed is set to 60%. To modify speed, edit the speed parameter in `main.py`:

```python
move_forward(speed=60)  # Change to desired speed (0-100)
```

### GPIO Pin Mapping

To change GPIO pins, modify the pin definitions in `motor_system.py`:

```python
RIGHT_IN1 = 17  # Change to your desired pin
RIGHT_IN2 = 27
# ... etc
```

## Safety Features

- **Automatic Cleanup**: GPIO pins are automatically cleaned up on exit
- **PWM Control**: Smooth speed control prevents sudden motor stress
- **Emergency Stop**: Immediate halt functionality
- **Mock Mode**: Safe development without hardware

## Troubleshooting

### Common Issues

1. **Permission Denied (GPIO)**:
   ```bash
   sudo python main.py
   ```

2. **Module Not Found (RPi.GPIO)**:
   - On Raspberry Pi: `pip install RPi.GPIO`
   - For development: The system will automatically use mock mode

3. **Web Interface Not Accessible**:
   - Check firewall settings
   - Ensure the Flask server is running on `0.0.0.0`
   - Verify the Raspberry Pi's IP address

4. **Motors Not Responding**:
   - Check wiring connections
   - Verify power supply to motors
   - Confirm GPIO pin assignments

## Development

### Adding New Commands

1. Add a new function in `motor_system.py`:
   ```python
   def custom_movement(speed=50):
       # Your custom movement logic
       pass
   ```

2. Add a new route in `main.py`:
   ```python
   elif action == "custom":
       custom_movement(speed=60)
       response_message = 'Custom Movement'
   ```

3. Add a button to the HTML template in `main.py`

### Extending Functionality

- Add sensor integration (ultrasonic, camera, etc.)
- Implement autonomous navigation
- Add joystick/gamepad support
- Include logging and telemetry

## License

This project is open source. Feel free to modify and distribute according to your needs.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

For issues and questions:
- Check the troubleshooting section
- Review GPIO wiring
- Ensure proper power supply
- Verify software dependencies

---

**Happy Roving! 🚀**
