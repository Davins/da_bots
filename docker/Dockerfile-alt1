FROM debian:stable 
RUN apt-get update -y && apt-get install -y wget curl unzip libgconf-2-4
RUN sh -c 'echo "APT::Default-Release "stable";" >> /etc/apt/apt.conf' 
RUN sh -c 'echo "deb http://ftp.hr.debian.org/debian sid main contrib non-free" >> /etc/apt/sources.list'
RUN apt-get update -y && apt-get install -yt sid firefox
RUN apt-get update -y && apt-get install -y xvfb python3 python3-pip 
RUN wget https://github.com/mozilla/geckodriver/releases/download/`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'`/geckodriver-`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'`-linux64.tar.gz
RUN tar -zxf geckodriver-`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'`-linux64.tar.gz -C /usr/local/bin
RUN chmod +x /usr/local/bin/geckodriver
RUN mkdir -p /opt/app
WORKDIR /opt/app
RUN pip3 install selenium
COPY test.py .
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null
COPY run.sh .
CMD /bin/bash run.sh