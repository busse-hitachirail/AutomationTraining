FROM python:3.13-slim

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies and browsers
RUN apt-get update &&     apt-get install -y         wget         gnupg         curl         unzip         ca-certificates         chromium-driver         firefox-esr         software-properties-common         fonts-liberation         libasound2         libatk-bridge2.0-0         libatk1.0-0         libcups2         libdbus-1-3         libgdk-pixbuf2.0-0         libnspr4         libnss3         libx11-xcb1         libxcomposite1         libxdamage1         libxrandr2         xdg-utils         && rm -rf /var/lib/apt/lists/*

# Install Microsoft Edge (dev channel)
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg &&     install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/ &&     sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge-dev.list' &&     apt-get update &&     apt-get install -y microsoft-edge-stable &&     rm -rf /var/lib/apt/lists/* &&     rm microsoft.gpg

# Install Python dependencies
RUN pip install --no-cache-dir     selenium     pytest     webdriver-manager     pyyaml

WORKDIR /app
COPY . .

# Ensure script is executable
RUN chmod +x run_tests.sh

CMD ["bash", "run_tests.sh"]
