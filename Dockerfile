FROM ubuntu:xenial-20191010
RUN apt update
RUN apt install -y nano apache2 apache2-utils libapache2-mod-wsgi-py3 python3


RUN mkdir /var/www/myapp/
WORKDIR /var/www/myapp/
COPY . .
ADD ./my_site.conf /etc/apache2/sites-available/000-default.conf
ADD ./ports.conf /etc/apache2/ports.conf
RUN python3 ./get-pip.py

RUN pip3 install -r ./requirements.txt
#RUN a2ensite my_site
#RUN a2dissite 000-default

EXPOSE 8000
CMD ["apache2ctl", "-D", "FOREGROUND"]
