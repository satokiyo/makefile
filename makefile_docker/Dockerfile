# FROM python:3.8
FROM python:3.8-slim
USER root
ENV PROJECT_NAME sample
WORKDIR /${PROJECT_NAME}

RUN apt-get -y update && \
    apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less wget git
RUN pip install --upgrade pip setuptools wheel
COPY ./requirements.txt /${PROJECT_NAME}
RUN pip install --no-cache-dir -r /${PROJECT_NAME}/requirements.txt

COPY .gitconfig /root/.gitconfig
COPY .bashrc /root/.bashrc
COPY ./hello.sh /${PROJECT_NAME}/hello.sh
RUN chmod +x /${PROJECT_NAME}/hello.sh
RUN mkdir -p /${PROJECT_NAME}/workspace
ENTRYPOINT ["/bin/bash"]
# ENTRYPOINT ["python"]
# CMD ["./hello.sh"]
