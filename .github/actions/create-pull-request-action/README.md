# Create Pull Reqeust Action

This action will create a pull request using the input values "head" and "base"

## Inputs

### `head`

**Required** The name of the head branch

### `base`
**Optional** Defaults to "master". The name of the base branch

## Outputs

### `pull-request-id`

The id of the pull request for this PR

### `created`

Boolean True if we created the pull request, False otherwise

## Example usage

uses: Ahuge/create-pull-request-action@v1
with:
  head: dev
  base: release
