# Base Image
FROM python:3.13-slim

# Install system dependencies
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

# Set environment so Selenium knows where to find Chromium
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="/usr/lib/chromium/:${PATH}"

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY test_script.py .

# Install Python packages
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run the test
CMD ["python", "test_script.py"]
