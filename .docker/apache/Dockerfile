FROM httpd:2.4

VOLUME /app/static
VOLUME /app/media
WORKDIR /usr/local/apache2/

COPY .docker/apache/httpd.conf /usr/local/apache2/conf/httpd.conf
COPY .docker/apache/httpd-vhosts.conf /usr/local/apache2/conf/extra/httpd-vhosts.conf

EXPOSE 8080 80
