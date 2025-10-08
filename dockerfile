FROM python:3.11-slim

# Ishchi papka
WORKDIR /app

# Sistem paketlari (agar kerak bo‘lsa)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Kutubxonalarni o‘rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Barcha loyihani ko‘chirish
COPY . .

# Botni ishga tushirish
CMD ["python3", "bot.py"]