# Gunakan image Python resmi sebagai base
FROM python:3.11-slim

# Set working directory di dalam container
WORKDIR /app

# Install dependensi sistem (jika diperlukan)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt terlebih dahulu untuk caching
COPY requirements.txt .

# Install dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh kode aplikasi ke container
COPY . .

# Expose port yang digunakan (Railway akan menggantinya dengan PORT env)
EXPOSE 8000

# Jalankan aplikasi dengan uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
