FROM caddy:2.10.0-builder-alpine AS builder

RUN xcaddy build \
    --with github.com/caddy-dns/cloudflare \
    --with github.com/caddyserver/replace-response

FROM caddy:2.10.0-alpine
LABEL description="Caddy-Cloudflare" \
    author="viacooky" \
    github="https://github.com/viacooky/Dockerfiles"

COPY --from=builder /usr/bin/caddy /usr/bin/caddy