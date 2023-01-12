# FROM python:3.6-alpine

FROM python:3.6-slim

# Install manually all the missing libraries
RUN apt-get update
#RUN apt-get install -y gconf-service wget libasound2 libgbm1 libappindicator3-1 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils
RUN apt-get install -y wget
# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# 环境变量来传递命令
ENV EXECUTE_CMD ${EXECUTE_CMD}
ENV EXECUTE_TIMEOUT ${EXECUTE_TIMEOUT}

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip3 install chromedriver-binary==108.0.5359.22.0 -i https://pypi.doubanio.com/simple

RUN pip3 install -r requirements.txt -i https://pypi.doubanio.com/simple
#CMD [ "chromedriver" ]
CMD ["python3", "start.py","${EXECUTE_CMD}","${EXECUTE_TIMEOUT}"]

