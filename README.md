# Kuando Busy Light for MacOS Webex User Status

This is a quick script to enable integration between a users Webex status and a Kuando BusyLight for users of MacOS where
currently no integration exists.

It requires the Kuando BusyLight HTTP API to be operational on the users machine. This can be obtained from Kuando directly via a helodesk request from
their downloads area.

I run this script as a cronjob via crontab every 10 seconds.

The script will poll the http api of the light, and if the light is found, it will poll the webex api and adjust the light accordingly.

**.env file**

This repo contains an example .env file to use as a template for your own file. It contains the following values
> WEBEX_API_KEY={This is your webex api key}
>
> WEBEX_USER={Your person ID string}

I recommend using a webex bot for an api key as these do not expire unlike personal keys which do expire.

This code is scanned by Sonarcube and dependencies kept up to date with renovate bot. 