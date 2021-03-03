FROM kalilinux/kali-rolling
ARG DEBIAN_FRONTEND=noninteractive
#RUN apt-get update && apt upgrade -y && apt-get install sudo -y && apt-get install apt-utils -y 
#RUN apt-get update && apt upgrade -y 
RUN apt-get update && apt upgrade -y && apt-get install sudo -y
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
    #util-linux \
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
    python3 \
    python3-dev \
    python3-pip \
    openssl \
    pv \
    jq \
    wget \
    libreadline-dev \
    #apktool \
    #zipalign \
    sqlite3 \
    ffmpeg \
    imagemagick \
    libsqlite3-dev \
    chromium\
    zlib1g-dev \
    recoverjpeg \
    zip \
    megatools \
    #axel \
    #procps \
    #policykit-1\
    libfreetype6-dev
RUN sed -i '/<policy domain="path" rights="none" pattern="@\*"/d' /etc/ImageMagick-6/policy.xml
##RUN pip3 install --upgrade pip setuptools 
RUN pip install --upgrade pip setuptools wheel
#RUN pip3 install --upgrade pip install wheel 
#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
#RUN axel https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install -y ./google-chrome-stable_current_amd64.deb && rm google-chrome-stable_current_amd64.deb
#RUN axel https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && chmod +x chromedriver && mv -f chromedriver /usr/bin/ && rm chromedriver_linux64.zip
RUN git clone https://github.com/Sh1vam/javes-3.0 /root/ub
RUN mkdir /root/ub/bin/
WORKDIR /root/ub/
RUN mv ub/javes_main/extra/apktool /usr/local/bin
RUN mv ub/javes_main/extra/apktool.jar /usr/local/bin
RUN chmod +x /usr/local/bin/*
##RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
##RUN python3.9 -m pip install --no-warn-script-location --no-cache-dir --upgrade -r requirements.txt
RUN sudo chmod o+r /usr/lib/python3.9 /dist-packages/*
CMD ["python3","-m","ub"]