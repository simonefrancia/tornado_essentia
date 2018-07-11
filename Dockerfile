FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    vim \
    nano 

RUN apt-get update \
    && apt-get install -y libyaml-0-2 libfftw3-3 libtag1v5 libsamplerate0 \
       libavcodec-ffmpeg56 \
       libavformat-ffmpeg56 \
       libavutil-ffmpeg54 \
       libavresample-ffmpeg2 \
       python python-numpy libpython2.7 python-yaml python-six \
    && rm -rf /var/lib/apt/lists/*



######################################## GAIA 

RUN apt-get update \
    && apt-get install -y build-essential libqt4-dev libyaml-dev python-dev pkg-config

RUN apt-get install -y apt-utils libpcre3 libpcre3-dev

RUN wget -O swig-3.0.12.tar.gz 'https://downloads.sourceforge.net/project/swig/swig/swig-3.0.12/swig-3.0.12.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fswig%2Ffiles%2Fswig%2Fswig-3.0.12%2Fswig-3.0.12.tar.gz%2Fdownload&ts=1486782132&use_mirror=superb-sea2' \
    && tar xf swig-3.0.12.tar.gz && cd swig-3.0.12 && ./configure --prefix=/usr && make -j 4 && make install && cd .. && rm swig-3.0.12.tar.gz 

RUN apt-get update \
    && git clone https://github.com/MTG/gaia.git \
    && cd gaia \
    && python ./waf configure \
    && python ./waf \
    && python ./waf install \
    && ldconfig \
    && apt-get install -y build-essential libyaml-dev libfftw3-dev \
       libavcodec-dev libavformat-dev libavutil-dev libavresample-dev \
       libsamplerate0-dev libtag1-dev python-numpy-dev


########################################   ESSENTIA


RUN mkdir /essentia && cd /essentia \
    && git clone https://github.com/MTG/essentia.git \
    && cd /essentia/essentia && git checkout v2.1_beta2 \
    && ./waf configure --mode=release --with-examples --with-python --with-vamp --with-gaia \ 
    && ./waf \
    && ./waf install \
    && ldconfig \
    &&  apt-get remove -y build-essential libyaml-dev libfftw3-dev libavcodec-dev \
        libavformat-dev libavutil-dev libavresample-dev python-dev libsamplerate0-dev \
        libtag1-dev python-numpy-dev \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && cd / 


##################################### ALSAAUDIO

RUN apt-get update && apt-get install libasound2-dev \
&& wget -c 'https://downloads.sourceforge.net/project/pyalsaaudio/pyalsaaudio/pyalsaaudio-0.5/pyalsaaudio-0.5.tar.gz' \ 
&& tar xf pyalsaaudio-0.5.tar.gz && cd pyalsaaudio-0.5 && python setup.py build && python setup.py install && cd / && rm pyalsaaudio-0.5.tar.gz


########################################## TORNADO 

RUN apt-get update -y && apt-get install git python python-pip python-numpy python-scipy python-matplotlib -y

RUN mkdir tornado_api

COPY src tornado_api

RUN pip install tornado==4.0.2 \
    boto3 botocore

EXPOSE 8888

WORKDIR tornado_api






