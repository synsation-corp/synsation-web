# synsation-web

## Docker Build

1. Build a docker image, using the current commit as the tag

```sh
docker build -t synsation-io-web:$(git show --format="%h" --no-patch) .
```
