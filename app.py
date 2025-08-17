"""
Application module for file operations and basic arithmetic.

This module provides functions for creating timestamped files and adding numbers.
"""
import os
from datetime import datetime

# Please customize the following variables
USER_NAME = "andrewrafael"
VERSION = "1.0.0"

def say_hi(msg: str = "Hi!", file_directory: str = "/app/data/") -> None:
    """
    Create a timestamped file with a message.
    
    Args:
        msg: The message to write to the file
        file_directory: The directory where the file will be created
    """
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M")

    # Define filename with timestamp
    file_name = f"outputfile_{USER_NAME}_{VERSION}_timestamp_{timestamp}.txt"
    file_path = os.path.join(file_directory, file_name)

    # Write the timestamp inside the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(msg)

    print(f"File '{file_path}' created successfully.")

def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b

if __name__ == "__main__":
    say_hi()
