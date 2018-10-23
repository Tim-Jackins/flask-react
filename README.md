# Flask React


[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?longCache=true&style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![pep8 compliant](https://img.shields.io/badge/code%20style-PEP8-ff69b4.svg?longCache=true&style=flat-square)](https://www.python.org/dev/peps/pep-0008/)
[![GitHub license](https://img.shields.io/github/license/Tim-Jackins/slackbot-template.svg?longCache=true&style=flat-square)](https://github.com/Tim-Jackins/slackbot-template/blob/master/LICENSE)

> This is an example file with maximal choices selected.

This is a long description.

## Table of Contents

- [Security](#security)
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [API](#api)
- [Contribute](#contribute)
- [License](#license)

## Security

This will serve your flask-react app over http so be careful sending sensitive info. If you are interested in serving over https I recommend you look at [JrCs](https://github.com/JrCs)'s [Let's Encrypt helper container](https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion).

## Background

Flask is a microframework to make webapps in python. React is a painless way to create interactive UIs. Nginx can be used as an excellent reverse proxy. Docker is a phenominal container platform. There's got to be a way to combine all of these technologies to make and serve interactive web apps with ease... Right? That's what this repo is for. A tutorial for constructing beautiful apps with ease. P.S. you need to have access to a domain.

## Install

These steps should be carried out wherever you want to host your apps. I typically use a [digital ocean droplet](https://www.digitalocean.com/pricing/).

First [install npm](https://www.taniarascia.com/how-to-install-and-use-node-js-and-npm-mac-and-windows/).

Then use npm to install npx:

```bash
npm i npx
```

Now clone this repo to your server:

```bash
git clone https://github.com/Tim-Jackins/flask-react.git
```

Go into the repository, start a new react app, and build it:

```bash
cd flask-react
npx create-react-app my-app
cd my-app
npm run build
```

Nice!

Now `cd` out of the react app and make a file called `.env`.

For now edit your `.env` file so it looks like this:

```bash
SECRET_KEY=12345678
DEBUG=False
```

This file is where you're going to keep your "secrets" (API keys, passwords, configurations, etc). You can always store these as environment variables but I prefer using python decouple. If you look at lines 7 and 8 of [app.py](/app.py) you can find an example of decouple's coolness.

Next go to your domain and make an A record named apptest that points to your server's IP.

Finally, go into `docker-compose.yml` and change `example.com` on line 22 to `apptest.yourdomain.com`.

## Usage

Bring your app up with the command:

```bash
docker-compose up
```

The repo is designed to be a template for any web app you want to make so usage from here on is open ended!

## Contribute

See [the contribute file](contribute.md)!

PRs accepted.

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

### Any optional sections

## License

[MIT © Richard McRichface.](../LICENSE)
