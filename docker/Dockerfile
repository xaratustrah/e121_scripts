FROM rootproject/root

ENV REPO https://git.chalmers.se/expsubphys/ucesb.git

RUN apt-get update && apt-get install -q -y --no-install-recommends \
    git build-essential bison flex libncurses5-dev

RUN cd /opt \
    && git clone ${REPO} \
    && mkdir /opt/ucesb/e121

COPY e121/* /opt/ucesb/e121/

RUN cd /opt/ucesb/e121 \
    && make -j 20 NO_CERNLIB=1

ENV PATH="${PATH}:/opt/ucesb/e121"

WORKDIR /opt/ucesb/e121

ENTRYPOINT [ "E121" ]
