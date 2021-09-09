# Tesrifatci-BOT

It is an Discord bot that fetches movie information, sets showtime, break duration and bothers our friend. 

## Invite the Bot
[![](https://image.flaticon.com/icons/png/512/1999/1999142.png )](https://discord.com/api/oauth2/authorize?client_id=792764080648617984&permissions=8&scope=bot)

## To Host or Copy the Bot
* Clone this repo
* Open your command line and type pip install -r requirements.txt
* Visit [Discords Developer Portal] (https://discordapp.com/developers/applications/) </br>
* Click "New Application", Enter in your applications name, Click on "Bot" </br>
* Make your application into a bot process </br>
* Paste your TOKEN within main.py

###  TMDb
To be able fetch information for the movies, Tesrifatci uses TMDb database. Visit [TBDb Developers page](https://developers.themoviedb.org/3/getting-started/introduction) and generate your key. ,/> 
Then replace this line: tmdb.api_key = os.environ['API_KEY']

### asyncio
Tesrifatci uses this library in order to keep track of the time. </br>
More information can be found here: https://pypi.org/project/asyncio/

| Command      | Usage | Description | 
| :----------- | :----------- | :----------- |
| help | %help() | |
| vizyon aliases=['vizyonda'] | %vizyon(string)  | returns movie title, relase date, overview, average vote |
| gösterim | %gösterim(int) | Pings everyone, stars a countdown for spesified minitues |
| ara | %ara(int) | Stars a count down for movie break |
| cancel | %cancel | Cancels the countdown |
| hakan | %hakan(string) | It bother our friend Hakan with random context |      

