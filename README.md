# Server_Status
Send discord server status messages when a server goes either online or offline

## Config File
Use the config.ini file to change the properties of your discord alerts, the properties you can change are:
### Server Name
The name of your private EO server
### Server IP
The IP address of your private EO server
### Server Port
The port number of your private EO server
### Server Logo
The logo of your private EO server or the logo of your discord server
### Discord Role
The discord role used to ping members. By default this is set to @here, to use a custom role you will need to:
 1. Activate discord developer mode in `Discord Settings > Advanced > Developer Mode`
 2. In the Member Side Panel of your server > Left Click a Member
 3. Right click one of their roles
 4. Left click `Copy Role ID`
 5. Replace @here in the config.ini with `<&ROLEID>` (eg. `<&123456789>`
### Online Title
The title displayed in the discord alert (eg. `Server Online`)
### Online Message
The message displayed in the discord alert (eg. `I have checked and it appears your server is online`)
### Offline Title
The title displayed in the discord alert (eg. `Server Offline`)
### Offline Message
The message displayed in the discord alert (eg. `I have checked and it appears your server is offline`)
### Webhook URL
The webhook URL which the bot will send the alert
### Footer
The footer text displayed at the bottom of the alert (eg. Provided by Vexx)
### Timer
How many seconds the bot will wait before checking the server status again (default 30 seconds)

![Discord Alert](https://cdn.discordapp.com/attachments/1100040855626190848/1183988934900973578/Screenshot_2023-12-12_at_2.29.11_pm.png)

## Discord Webhook
To obtain a discord webhook URL go to `discorder server settings > Intergrations > Webhooks` and make a new webhook. Give the webhook a name, set the channel it will post messages (or alerts) and give it an image/logo. Click `Copy Webhook` and paste that URL into `config.ini` after `WEBHOOK = https:your-discord-webhook.com`
![Server Settings Intergrations](https://cdn.discordapp.com/attachments/1100040855626190848/1183989510862819451/Screenshot_2023-12-12_at_2.31.30_pm.png)
![Webhook Setup](https://cdn.discordapp.com/attachments/1100040855626190848/1183989995195875438/Screenshot_2023-12-12_at_2.33.24_pm.png)

## Running the bot
The bot runs using Python (Built on Python 3.12.1) and requires:
```
pip install configparser
```
```
pip install requests==2.6.0
```
