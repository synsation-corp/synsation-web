# synsation-web

An example of building a docker image, creating various supply chain content, and registering them on a SCITT based immutable Append-only log.

For each git commit, the [`scitt-register.yml`](./.github/workflows/scitt-register.yml) github action performs the following steps:

1. A SCITT Feed is created, based on the image name and version.
1. Docker Build/push of the image, using the following format: `${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}` (eg `ghcr.io/synsation-corp/synsation-web:3fcf9b7ddde947c35ac2c952d6a24b26d26a1860`)
1. Generate and register the output of docker scout cves
1. Generate and register an SPDX SBOM
1. Generate and register a CycloneDX SBOM
1. Generate and register an attestation of compliance

Once complete, the following query can be run, using the SCITT Feed to identify all the signed statements.

1. Save the FEED:

    ```sh
    FEED=ghcr.io/synsation-corp/synsation-web:3fcf9b7ddde947c35ac2c952d6a24b26d26a1860
    ```

1. Query DataTrails for Signed Statements, based on the FEED:

    ```sh
    curl https://app.datatrails.ai/archivist/v2/publicassets/-/events?event_attributes.feed_id=$FEED | jq
    ```
