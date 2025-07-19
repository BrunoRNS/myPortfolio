FROM nginx:bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends iptables \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN iptables -A INPUT -p icmp --icmp-type echo-request -j DROP

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

RUN chown -R nginx:nginx /var/cache/nginx \
    && chmod -R 755 /var/log/nginx