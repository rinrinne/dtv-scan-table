FROM debian:jessie
LABEL maintainer "rinrin.ne@gmail.com"

ARG BUILD_PACKAGES="build-essential git autoconf automake libtool libudev-dev gettext pkg-config"
ARG INSTALLED_PACKAGES="python"

ENV HOME_DIR="/home/v4l-utils"

ENV DEBIAN_FRONTEND noninteractive

WORKDIR $HOME_DIR

RUN set -x \
    && apt-get update \
    && apt-get install -y $BUILD_PACKAGES \
    && git clone git://linuxtv.org/v4l-utils.git module \
    && cd module \
    && ./bootstrap.sh \
    && ./configure --disable-doxygen-doc --disable-doxygen-dot --disable-libv4l --disable-v4l2-compliance-libv4l --disable-v4l2-ctl-libv4l --disable-qv4l2 --enable-gconv --without-jpeg --with-gconvdir=/usr/lib/x86_64-linux-gnu/gconv \
    && make \
    && make install \
    && cd .. \
    && rm -rf module \
    && apt-get remove --purge -y $BUILD_PACKAGES $(apt-mark showauto) \
    && apt-get install -y $INSTALLED_PACKAGES \
    && rm -rf /var/lib/apt/lists/* \
    && echo /usr/local/lib > /etc/ld.so.conf.d/locallib.conf \
    && ldconfig \
    && iconvconfig /usr/lib/x86_64-linux-gnu/gconv \
    && mkdir -p /var/run/v4l-utils

ADD home $HOME_DIR/
 
VOLUME /var/run/v4l-utils

#CMD ["./scan.sh"]
