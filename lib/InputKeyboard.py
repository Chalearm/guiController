import pyautogui
import time

def setInputFromKeyboard(input_string, frequency_ms):
    """
    Simulate keyboard input for the provided string with the specified frequency.

    Parameters:
    input_string (str): The string of characters to be input.
    frequency_ms (int): The frequency of input in milliseconds.
    """
    # Convert milliseconds to seconds for sleep
    frequency_sec = frequency_ms / 1000.0
    
    for char in input_string:
        pyautogui.typewrite(char)  # typewrite sends the character to keyboard
        time.sleep(frequency_sec)   # wait for the specified duration


#exmaple function
def functionExample1():
    input_data = "abcdef"  # The string to type
    frequency = 200        # Frequency in milliseconds
    
    print(f"Typing '{input_data}' with a frequency of {frequency} ms per character.")
    setInputFromKeyboard(input_data, frequency)
    setInputFromKeyboard("mN7LxyxN", 60)


# Example usage
if __name__ == "__main__":
    functionExample1()