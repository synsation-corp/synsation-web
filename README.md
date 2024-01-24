# synsation-web

## Docker Build

1. Build a docker image, using the current commit as the tag

```sh
docker build -t synsation-io-web:$(git show --format="%h" --no-patch) .
```

1. Generate an SPDX SBOM
```sh
sbom-tool generate -b /spdx -bc . -pn synsation-web -pv 0.1 -ps synsation-org -nsb synsation.io
```
