# Pandas-Termux-ARM64
Pandas 2.2.3 compilato nativamente per Python 3.13 su Termux (Android ARM64)

# Pandas 2.2.3 per Termux (ARM64)

Questo repository contiene il file wheel (`.whl`) precompilato di **Pandas 2.2.3** per l'ambiente **Termux** su Android.

## Perché questo repository?

Compilare Pandas da sorgente su un dispositivo mobile (Termux) è un processo complesso e spesso fallimentare a causa della mancanza di dipendenze di sistema (cmake, ninja, meson-python) o per limiti di memoria RAM. 
Questo file `.whl` è stato compilato nativamente e testato per bypassare completamente la fase di build, permettendo un'installazione rapida e indolore.

## Specifiche Tecniche

*   **Libreria:** Pandas 2.2.3
*   **Versione Python:** 3.13 (CPython)
*   **Architettura:** ARM64 (aarch64)
*   **Sistema Operativo:** Android (API 30+)
*   **Ambiente:** Termux

## Installazione

Assicurati di avere le dipendenze di base installate tramite il gestore pacchetti di Termux:

```bash
pkg install python-numpy
