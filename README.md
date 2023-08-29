# Dark_Web_Crawler
Crawler to help you search keywords in a set of given links on darkweb

## What will it do ??
The Python script we'll be looking at uses a fresh random IP address produced every 10 seconds to crawl webpages using the TOR browser. There are several benefits to this. One benefit of using TOR is that it hides the request's origin by routing internet traffic across a network of servers, protecting the web crawler's anonymity. Changing IP addresses every 10 seconds also aids in avoiding being identified and blacklisted by website servers.

## Commands

1. `git clone https://github.com/ch3tanbug/Dark_Web_Crawler.git`

2. `cd Dark_Web_Crawler`

3. `pip install -r requirements.txt`

## Usage
Edit the links to crawl in the python script and then provide the words to search for seperated by commas `,` 

You will need to have the TOR browser and the TOR control port installed and configured on your machine in order for the script to work properly. You can find instructions for installing and configuring TOR on Windows on the TOR website (https://www.torproject.org/). TOR should be running on default

NOTE- You should note that tor should be running on default port 9051 and running in background before running the python script 
Also add the password in controller.authenticate(password=`yourpassword`)

You can add or edit a password in TOR like this:

Locate the torrc Configuration File:
The torrc configuration file contains settings for your Tor instance. The location of this file depends on your operating system. Common locations are:

1. `Linux: /etc/tor/torrc or ~/.torrc`

2. `Windows: C:\Users\<Username>\AppData\Roaming\tor\torrc`

Edit the torrc File:
Open the torrc configuration file using a text editor.

Add or Modify the Authentication Line:
Find or add the following line in the torrc file to set the authentication password:

`HashedControlPassword your_hashed_password_here`

Replace your_hashed_password_here with the hashed form of your desired password. To generate the hashed password, you can use the tor --hash-password command in your terminal:

`tor --hash-password your_password_here`

This command will output a hashed version of your password. Copy that hash and use it in the torrc file.

Save the file change the new password in the python script and restart the TOR and the python script.

## Images
![Alt text](https://github.com/ch3tanbug/Dark_Web_Crawler/blob/main/darkweb.PNG)


