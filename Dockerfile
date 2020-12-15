#For First fore line which is coded by https://github.com/sppidy thanks it prevented app suspention thanks bro
FROM kalilinux/kali-rolling
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt upgrade -y && apt-get install sudo -y && apt-get install apt-utils -y 
RUN touch ~/.hushlogin
RUN apt-get install -y\
    coreutils \
    bash \
    nodejs \
    bzip2 \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    #aria2 \
    util-linux \
    libevent-dev \
    libjpeg-dev \
    libffi-dev \
    libpq-dev \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    musl \
    neofetch \
    libcurl4-openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-server-dev-all \
    #chromedriver \
    openssl \
    pv \
    jq \
    wget \
    python3 \
    python3-dev \
    python3-pip \
    libreadline-dev \
    metasploit-framework \
    apktool \
    openjdk-13-jdk \
    #zipalign \
    sqlite3 \
    ffmpeg \
    libsqlite3-dev \
    chromium-bsu \
    zlib1g-dev \
    recoverjpeg \
    zip \
    megatools \
    axel \
    procps \
    policykit-1\
    libfreetype6-dev

RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

# install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
#RUN apt-get install -y chromium
RUN pip3 install --upgrade pip setuptools 
#RUN pip3 install --upgrade pip install wheel 
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi 
RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 
RUN rm -r /root/.cache
RUN axel https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install -y ./google-chrome-stable_current_amd64.deb && rm google-chrome-stable_current_amd64.deb
RUN axel https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && chmod +x chromedriver && mv -f chromedriver /usr/bin/ && rm chromedriver_linux64.zip
RUN git clone https://github.com/Sh1vam/javes-3.0 /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/
RUN mv userbot/javes_main/extra/apktool /usr/local/bin
RUN mv userbot/javes_main/extra/apktool.jar /usr/local/bin
#RUN mv userbot/javes_main/extra/apk.rb /usr/share/metasploit-framework/lib/msf/core/payload
RUN chmod +x /usr/local/bin/*
RUN pip3 install -r requirements.txt
#RUN python3 -m pip install --no-warn-script-location --no-cache-dir --upgrade -r requirements.txt
#RUN sudo chmod o+r /usr/lib/python3/dist-packages/*
CMD ["python3","-m","userbot"]
