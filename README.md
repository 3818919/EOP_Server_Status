# Server Status Alert Bot for Discord

This bot sends alerts on Discord about the status of a server, indicating when it goes online or offline.

## Configuration

To customize your alerts, use the `config.ini` file. You can modify the following properties:

### Server Details
- **Server Name**: Specify the name of your private EO server.
- **Server IP**: Enter the IP address of your server.
- **Server Port**: Define the port number your server uses.
- **Server Logo**: Choose a logo, either from your EO server or Discord server.

### Discord Notifications
- **Discord Role**: Set the Discord role for pinging members. Default is `@here`. For custom roles:
  1. Enable Developer Mode: `Discord Settings > Advanced > Developer Mode`.
  2. On your server's Member Side Panel, left-click a member.
  3. Right-click one of their roles.
  4. Select `Copy Role ID`.
  5. Replace `@here` in `config.ini` with `<&ROLEID>` (e.g., `<&123456789>`).

### Alert Customization
- **Online Title**: Title for online status alerts (e.g., `Server Online`).
- **Online Message**: Message for online status (e.g., `Server is currently online`).
- **Offline Title**: Title for offline status alerts (e.g., `Server Offline`).
- **Offline Message**: Message for offline status (e.g., `Server is currently offline`).
- **Webhook URL**: Your Discord webhook URL for sending alerts.
- **Footer**: Custom footer text for alerts (e.g., `Provided by Vexx`).
- **Timer**: Interval in seconds for status checks (default is 30 seconds).

![Discord Alert](https://cdn.discordapp.com/attachments/1100040855626190848/1183988934900973578/Screenshot_2023-12-12_at_2.29.11_pm.png)

## Setting Up Discord Webhook

To set up a Discord webhook:
1. Navigate to `Server Settings > Integrations > Webhooks`.
2. Create a new webhook, name it, select a posting channel, and set an image/logo.
3. Click `Copy Webhook` and paste the URL into `config.ini` after `WEBHOOK = https://your-discord-webhook.com`.

![Server Settings Integrations](https://cdn.discordapp.com/attachments/1100040855626190848/1183989510862819451/Screenshot_2023-12-12_at_2.31.30_pm.png)
![Webhook Setup](https://cdn.discordapp.com/attachments/1100040855626190848/1183989995195875438/Screenshot_2023-12-12_at_2.33.24_pm.png)

## Running the Bot

The bot is built with Python 3.12.1. Install the required packages using pip:

```bash
pip install configparser
pip install requests==2.6.0
```
