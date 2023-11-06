import time

while True:
    # Get the current time
    current_time = time.strftime("%H:%M:%S")
    
    # Print the current time to the console
    print(current_time, end="\r")  # Use '\r' to overwrite the previous time

    # Wait for one second before updating the time
    time.sleep(1)
