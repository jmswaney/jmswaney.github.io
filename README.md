# Personal Site

Personal website for Justin Swaney, hosted at [jmswaney.com](https://www.jmswaney.com)

## Build Setup

```bash
# install dependencies
$ yarn install

# serve with hot reload at localhost:3000
$ yarn dev

# build for production and launch server
$ yarn build
$ yarn start

# generate static project
$ yarn generate
```

For detailed explanation on how things work, check out [Nuxt.js docs](https://nuxtjs.org).

## Run Tests

```bash
# Run jest on test/
yarn test
```

## Deployment

Checkout `.github/ci.yml` for automated deployment on changes to `master` branch. Uses `peaceiris/actions-gh-pages@v3` to move `dist/` folder to the `gh-pages` branch (where GitHub is configured to serve the static site from).