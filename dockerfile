#her valgte jeg base immage python 3.13 slim for å minimere størrelsen på docker imaget
FROM python:3.13-slim

#setter arbeidskatalogen i containeren til /app
WORKDIR /app

#kopierer requirements.txt filen til arbeidskatalogen i containeren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# denne kopierer filene fra den lokale maskinen til arbeidskatalogen i containeren
COPY . .

# her brukes det port 6565 for å eksponere applikasjonen
EXPOSE 6565

#her defineres kommandoen som skal kjøres når containeren startes
CMD ["python", "Patrykkkk_Kantineapp.py"]
