Pdf Suspaudimas  
=======================

# Gui aplikacija

### Kad sukompiliuotų gui reikia pridėti ./data/ dokumnetus 
`$ ./venv/Scripts/pyinstaller.exe --onefile --windowed -F --add-data="data/*;." guy.py`

GS pridėtas /data/ kataloge, nereikia papildomai nieko

Suspaudimo reikšmės, nuo 0 iki 4 nuo mažiausio iki didžiausio suspaudimo


Reikia papildomai ghostscript sriptus `gsdll32.lib` `gsdll32.dll` `gswin32c.exe` failą idėtį į `data/` katalogą


GUI kurtas naudojas QT designer.
