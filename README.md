Pdf Suspaudimas  
=======================

# Gui aplikacija

### Kad sukompiliuotų gui reikia pridėti ./data/ dokumnetus 
`$ ./venv/Scripts/pyinstaller.exe --onefile --windowed -F --add-data="data/*;." guy.py`

GS pridėtas /data/ kataloge, nereikia papildomai nieko

Suspaudimo reikšmės, nuo 0 iki 4 nuo mažiausio iki didžiausio suspaudimo


Reikia papildomai ghostscript `gsdll32.dll` failą idėtį į `data/` katalogą


GUI kurtas naudojas QT designer.
