Ansible role: Grafana Annotations Bot [![Build Status](https://travis-ci.org/13rentgen/ansible-role-grafana-annotations-bot.svg?branch=master)](https://travis-ci.org/13rentgen/ansible-role-grafana-annotations-bot)
=========

Ansible role for [Grafana Annotation Bot](https://github.com/13rentgen/grafana-annotations-bot). Currently this works on Debian and RedHat based linux systems (only systemd support). Tested platforms are:

* CentOS 7
* Debian 9
* Ubuntu 18


Role Variables
--------------

| Variable                | Required | Default Value | Description                                                                                               |
|-------------------------|----------|---------------|-----------------------------------------------------------------------------------------------------------|
| telegram_bot_token      | True     |               | The token used to connect with Telegram. Token you get from [@botfather](https://telegram.me/botfather)   |
| telegram_bot_admins     | True     |               | Telegram Bot admin IDs list                                                                               |
| grafana_url             | True     |               | The URL that's used to connect to the Grafana, example: http://localhost:3000                             |
| grafana_api_token       | True     |               | The Bearer token used to connect with Grafana API                                                         |
| grafana_scrape_interval | False    | 5s            | Scrape annotations interval                                                                               |
| telegram_bot_version    | False    | v0.2.0        | Grafana Annotation Bot version. [See releases here](https://github.com/13rentgen/grafana-annotations-bot) |
| telegram_bot_log_level  | False    | warn          | Telegram Bot log level. Possible values: debug, info, warn, error                                         |



Example Playbook
----------------

    - hosts: server
      roles:
        - role: 13rentgen.grafana_annotations_bot
          telegram_bot_token: 'TOKEN'
          telegram_bot_admins: 
            - '123'
            - '456'
          grafana_url: 'http://127.0.0.1:3000'
          grafana_api_token: 'BEARER-TOKEN'

License
-------

[MIT](LICENSE)

Author Information
------------------

This role was created in 2019 by [Aleksandr Zaytsev](https://github.com/13rentgen).
