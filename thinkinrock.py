# set up imports
import requests # type: ignore
import subprocess
import os
import time
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# grab vars from .env file
sampler_name = os.environ.get("SAMPLER_NAME") or "DPM++ 2M SDE"
scheduler = os.environ.get("SCHEDULER_NAME") or "Karras"
img_width = int(os.environ.get("IMAGE_WIDTH") or 1024)
img_height = int(os.environ.get("IMAGE_HEIGHT") or 1024)
cfg = float(os.environ.get("CFG_SCALE") or 4.5)
steps = os.environ.get("STEPS") or 30

# set up variables
payload = {
    "prompt": input("what do you want the big ol thinkin' rock to make for you? "),
    "sampler_name": sampler_name,
    "scheduler": scheduler,
    "steps": steps,
    "cfg_scale": cfg,
    "width": img_width,
    "height": img_height
}
auto1111_bat = r"C:\Users\alexa\auto1111\run.bat"

def start_auto1111():
    print("starting auto1111...")
    try:
        subprocess.Popen(
            [auto1111_bat],
            shell=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        print("auto1111 started successfully.")
    except Exception as e:
        print(f"Failed to start auto1111: {e}")
        exit(1)

def stop_auto1111():
    print("stopping auto1111...")
    try:
        # Find python processes with the run.bat in their command line
        result = subprocess.run(
            [
                "wmic", "process", "where",
                f'CommandLine like "%%{auto1111_bat}%%" and Name=\'python.exe\'',
                "get", "ProcessId", "/VALUE"
            ],
            capture_output=True, text=True
        )
        pids = [
            line.split("=")[1].strip()
            for line in result.stdout.splitlines()
            if line.startswith("ProcessId=")
        ]
        if not pids:
            print("No auto1111 process found to stop.")
            return
        for pid in pids:
            subprocess.run(["taskkill", "/F", "/PID", pid], check=True)
        print("auto1111 stopped successfully.")
    except Exception as e:
        print(f"Failed to stop auto1111: {e}")
        exit(1)

def check_auto1111_running():
    print("checking if auto1111 is already running...")
    if requests.get("http://localhost:7860/login_check/").status_code != 200:
        print("auto1111 is not running, starting it now...")
        return False


# function to call auto1111 api endpoint
def create_image():
    print("the thinkin' rock is now thinking about your request...")
    image_response = requests.post("http://localhost:7860/sdapi/v1/txt2img", json=payload)
    if image_response.status_code == 200:
        data = image_response.json()
        images = data.get('images')
        if images and len(images) > 0:
            import base64
            img_data = base64.b64decode(images[0])
            from datetime import datetime
            user_folder = input("where should the rock put the image? (enter a folder, leave blank for current directory): ").strip()
            timestamp = datetime.now().strftime("%S%M%H%d%m%y")
            filename = f'output_{timestamp}.png'
            if user_folder:
                output_path = os.path.join(user_folder, filename)
            else:
                output_path = os.path.join(os.getcwd(), filename)
            with open(output_path, 'wb') as f:
                f.write(img_data)
            print(f"Image saved to {output_path}")
        else:
            print("No image data found in response.")
    else:
        print(f"the rock fell over, here were its final words: {image_response.status_code}")

# the actual script starts here

auto1111_was_running = check_auto1111_running() != False
try:
    if not auto1111_was_running:
        start_auto1111()
    # here is where the actual things happen
    try:
        create_image()
        print("the rock has produced a lovely image for you")
    finally:
        pass
    exit(0)
except KeyboardInterrupt:
    print("\nuser has decided to put the rock back to bed. goodnight rock!")
    try:
        if not auto1111_was_running:
            stop_auto1111()
    except Exception as e:
        print(f"Error while stopping auto1111: {e}")
        exit(1)






