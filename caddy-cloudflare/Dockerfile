FROM caddy:2.8.4-builder-alpine AS builder

RUN xcaddy build \
    --with github.com/caddy-dns/cloudflare

FROM caddy:2.8.4-alpine
LABEL description="Caddy-Cloudflare" \
    author="viacooky" \
    github="https://github.com/viacooky/Dockerfiles"

COPY --from=builder /usr/bin/caddy /usr/bin/caddy
