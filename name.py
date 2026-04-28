import pyfiglet
import shutil
from colorama import Fore, Style, init

init(autoreset=True)

def print_fitted_name(text):
    terminal_width = shutil.get_terminal_size().columns
    
  
    ascii_art = pyfiglet.figlet_format(text, font='slant', width=terminal_width)
    
    print(Fore.YELLOW + Style.BRIGHT + ascii_art)

print_fitted_name("FERRICOOL-STUDIOS")

