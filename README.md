# Flask React

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?longCache=true&style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![pep8 compliant](https://img.shields.io/badge/code%20style-PEP8-ff69b4.svg?longCache=true&style=flat-square)](https://www.python.org/dev/peps/pep-0008/)
[![GitHub license](https://img.shields.io/github/license/Tim-Jackins/slackbot-template.svg?longCache=true&style=flat-square)](https://github.com/Tim-Jackins/slackbot-template/blob/master/LICENSE)

> A example app for making a flask-react app and serving over https.

## Table of Contents

- [Security](#security)
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)
- [License](#license)

## Security

The `ssl-helper` container will allow you to serve the app over https but you should make sure to run flask in [production mode](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjspaaOwP_eAhXI1lkKHfAyCRcQFjAAegQICBAB&url=http%3A%2F%2Fflask.pocoo.org%2Fdocs%2F1.0%2Ftutorial%2Fdeploy%2F&usg=AOvVaw1zxSFWTq2To7-E2PNQgiVT).

## Background

Flask is a microframework to make webapps in python. React is a painless way to create interactive UIs. Nginx can be used as an excellent reverse proxy. Docker is a phenominal container platform. There's got to be a way to combine all of these technologies to make and serve interactive web apps with ease... Right? That's what this repo is for. A tutorial for constructing beautiful apps with ease. P.S. you need to have access to a domain.

## Install

These steps should be carried out wherever you want to host your apps. I typically use a [digital ocean droplet](https://www.digitalocean.com/pricing/).

First [install npm](https://www.taniarascia.com/how-to-install-and-use-node-js-and-npm-mac-and-windows/).

Then use npm to install npx:

```bash
npm install npx
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

Finally, go into `docker-compose.yml` and change it according to comments.

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

## License

[MIT © Jack Timmins.](../LICENSE)
