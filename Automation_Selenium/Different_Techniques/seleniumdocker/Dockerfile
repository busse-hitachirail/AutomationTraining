# Base Image
FROM python:3.13-slim

# Install system packages for Chromium and ChromeDriver
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    wget \
    curl \
    unzip \
    fonts-liberation \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set Chromium path for Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="/usr/lib/chromium/:${PATH}"

# Create app folder and copy files
WORKDIR /app
COPY requirements.txt .
COPY test_script.py .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

# Run your script
CMD ["python", "test_script.py"]
