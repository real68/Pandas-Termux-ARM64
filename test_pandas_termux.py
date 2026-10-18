#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pandas Termux ARM64 - Global Test Script
----------------------------------------
Questo script è pensato per chiunque abbia appena scaricato il file .whl 
da questo repository. Serve a verificare che Pandas sia installato 
correttamente e che le librerie native (C/C++) rispondano sul sistema Android/Termux.

Autore: real68 (Progetto Thoth)
"""

import sys
import platform
import pandas as pd
import numpy as np

def print_header():
    print("\033[36m" + "="*50)
    print(" PANDAS TERMUX ARM64 - SYSTEM VERIFICATION")
    print("="*50 + "\033[0m")

def check_system():
    print("\n\033[33m[+] SYSTEM INFORMATION:\033[0m")
    print(f"  - OS:           {platform.system()} {platform.release()}")
    print(f"  - Architecture: {platform.machine()}")
    print(f"  - Python:       {sys.version.split()[0]}")
    print(f"  - Pandas:       {pd.__version__}")
    print(f"  - NumPy:        {np.__version__}")

def test_dataframe():
    print("\n\033[33m[+] DATAFRAME & NATIVE MATH TEST:\033[0m")
    
    # Creazione di un DataFrame di test con numeri casuali
    data = {
        'Signal_A': np.random.randn(5),
        'Signal_B': np.random.randn(5)
    }
    df = pd.DataFrame(data)
    
    # Calcolo della media e della deviazione standard
    mean_a = df['Signal_A'].mean()
    std_a = df['Signal_A'].std()
    
    print(f"  - DataFrame shape:      {df.shape}")
    print(f"  - Mean of Signal_A:     {mean_a:+.4f}")
    print(f"  - Std Dev of Signal_A:  {std_a:.4f}")
    
    # Test di una funzione che usa i calcoli nativi di Pandas
    df['Sum'] = df['Signal_A'] + df['Signal_B']
    print(f"  - Operation 'A+B' on column: OK")

def conclusion():
    print("\n\033[32m[+] SUCCESS: Pandas is fully operational on this device!\033[0m")
    print("    The C-extensions are working. You are ready for data analysis.\n")

if __name__ == "__main__":
    print_header()
    try:
        check_system()
        test_dataframe()
        conclusion()
    except Exception as e:
        print(f"\n\033[31m[!] ERROR: {e}\033[0m")
        print("Something went wrong. Check if the wheel file was installed correctly for your Python version.")
