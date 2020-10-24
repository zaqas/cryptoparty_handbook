VPN
=============================================

Virtual Private Network (VPN) allows users to connect to a server (in an unrestricted location), to which one or more clients connect. When you're surfing on the Internet, websites and corporations can see your real IP address and even your ISP can see which websites you visit and sell these information to third-parties.

In some countries searching for a controversial topic could pose huge risks to someones life and work. VPN services encrypt your Internet traffic and protect users against hackers, trackers and other adversaries. If you're sitting in a coffee shop and you're using the public WiFi, no hacker is able to see what websites you're visiting since your communication is encrypted by your VPN provider.

It should be noted that choosing a reputable VPN provider is very important because they're able to log information about you and build a profile on you and sell your information (which many providers do). You should look for providers that are respected in the industry and people know they have the technical knowledge and the motivation to protect their information.

Using a VPN also comes in handy if you're in a country which censors websites or you want to bypass a geographical access restrictions. It's beneficial to use a VPN in a country which has hostile attitude towards Internet. For example a country may use a technique such as DNS spoofing to redirect users to another login page instead of Gmail's login page to grab user's passwords. This method could be used by low level adversaries as well. 

A VPN in the right scenario against the right threat model could be very effective and we recommend using one to protect your privacy. Even if you don't trust commercial providers, you can create your own VPN.



Hosting Your Own VPN
-----------------------------------------

If you're a techie and you want to use your own VPN instead of using a commerical VPN because you don't trust other companies with your data, you can use these tools to host your own VPN:

- [Streisand](https://github.com/StreisandEffect/streisand/blob/master/README.md)

- [Algo VPN](https://github.com/trailofbits/algo/blob/master/README.md)

Hosting your own VPN is also useful when you live in a country in which most commerical VPN providers are blocked. In this case you can create your own VPN service to circumvent censorship. You just need a hosting provider.

Although with homemade VPN's you're in control of your data, it's far easier to track you because you're connecting from a single IP address.

By using a commercial VPN, you share your IP address with other customers so it's tracking you becomes harder.

An account from a commercial VPN provider
-----------------------------------------

There are multiple VPN providers out there. Some will give you free trial time, others will begin charging right away at an approximate rate of €5 per month. Look for a VPN provider that offers OpenVPN or WireGuard.

WireGuard vs OpenVPN
-----------------------------------------

In comparison to OpenVPN which has over 600,000 lines of code, WireGuard has only 4,000 lines of code. This makes debugging WireGuard easier and it's less likely for a vulnerability to remain undiscovered. WireGuard is much faster and efficient than OpenVPN. WireGuard is also very easy to use. To read more about WireGuard's technical details, [see this](https://www.wireguard.com/papers/wireguard.pdf).

Choosing a VPN Provider
-----------------------------------------

When choosing a VPN provider you need to consider the following points:

 * Information that is required from you to register an account - the less that is needed the better. A truly privacy concerned VPN provider would only ask you for email address (make a temporary one!), username and password. More isn't required unless the provider creates a user database which you probably don't want to be a part of. Some VPN providers don't even ask for your email address, they generate an account number.
 * Payment method to be used to pay for your subscription. Cash-transfer is probably the most privacy-prone method, since it does not link your bank account and your VPN network ID. Cryptocurrencies and other anonymous payment methods such as gift cards are also acceptable.
 * Avoid VPN providers that require you to install their own proprietary client software. There is a perfect open source solution for any platform, and having to run a "special" client is a clear sign of a phony service.
 * Avoid using PPTP based VPNs, as several security vulnerabilities exist in that protocol. In fact, if two providers are otherwise equal, choose the one _not_ offering PPTP if feasible.
 * Look for a VPN provider that's using OpenVPN or WireGuard.
 * Exit gateways in countries of your interest. Having a choice of several countries allows you to change your geo-political context and appears to come from a different part of the world. You need to be aware of legislation details and privacy laws in that particular country.
 * Look for VPN providers that have kill-switch built in.
 * Anonymity policy regarding your traffic - a safe VPN provider will have a non-disclosure policy. Personal information, such as username and times of connection, should not be logged either.
 * Allowed protocols to use within VPN and protocols that are routed to the Internet. You probably want most of the protocols to be available
 * Price vs. quality of the service and its reliability.
 * Any known issues in regard to anonymity of the users the VPN provider might have had in the past. Look online, read forums and ask around. Don't be tempted by unknown, new, cheap or dodgy offers.
 * Look for providers that have been audited by a third party.

For a detailed comparison between providers look at this website:

 * https://thatoneprivacysite.net/#detailed-vpn-comparison


 
Setting up your VPN client
-----------------------------------------


 > "OpenVPN [..] is a full featured SSL VPN software solution that integrates OpenVPN server capabilities, enterprise management capabilities, simplified OpenVPN Connect UI, and OpenVPN Client software packages that accommodate GNu/Linux, OSX, Windows and  environments. OpenVPN Access Server supports a wide range of configurations, including secure and granular remote access to internal network and/or private cloud network resources and applications with fine-grained access control." ([http://openvpn.net/index.php/access-server/overview.html](http://openvpn.net/index.php/access-server/overview.html))

There is a number of different standards for setting up VPNs, including PPTP, LL2P/IPSec and **OpenVPN**. They vary in complexity, the level of security they provide, and which operating systems they are available for. Do not use PPTP as it has several security vulnerabilities. In this text we will concentrate on OpenVPN. It works on most versions of GNU/Linux, OSX, Windows. OpenVPN is TLS/SSL-based - it uses the same type of **encryption** that is used in HTTPS (Secure HTTP) and a myriad of other encrypted protocols. OpenVPN encryption is based on **RSA** key exchange algorithm. For this to work and in order to communicate, both the server and the client need to have public and private RSA keys.

Once you obtain access to your VPN account the server generates those keys and you simply need to download those from the website of your VPN provider or have them sent to your email address. Together with your keys you will receive a *root certificate (\*.ca)* and a *main configuration file (\*.conf or \*.ovpn)*. In most cases only the following files will be needed to configure and run an OpenVPN client:

 * **client.conf** (or client.ovpn) - configuration file that includes all necessary parameters and settings. NOTE: in some cases certificates and keys can come embedded inside the main configuration file. In such a case the below mentioned files are not necessary.
 * **ca.crt** (unless in configuration file) - root authority certificate of your VPN server, used to sign and check other keys issued by the provider.
 * **client.crt** (unless in configuration file) - your client certificate, allows you to communicate with VPN server.

Based on a particular configuration, your VPN provider might require a username and password to authenticate your connection. Often, for convenience, these can be saved into a separate file or added to the main configuration file. In other cases, key-based authentication is used, and the key is stored in a separate file:

 * **client.key** (unless in configuration file) - client authentication key, used to authenticate to the VPN server and establish an encrypted data channel.

In most cases, unless otherwise necessary, you don't need to change anything in the configuration file and (surely!) **do not edit key or certificate files!** All VPN providers have thorough instructions regarding the setup. Read and follow those guidelines to make sure your VPN client is configured correctly.

NOTE: Usually it's only allowed to use one key per one connection, so you probably shouldn't be using the same keys on different devices at the same time. Get a new set of keys for each device you plan to use with a VPN, or attempt to set up a local VPN gateway (advanced, not covered here).

Download your OpenVPN configuration and key files copy them to a safe place and proceed to the following chapter.


Caveats & Gotchas
-----------------


Although a VPN will obfuscate your IP address, due to the nature of most VPNs your TCP/IP stack meta-data and other identifying information will be sent across the wire as-is.

This may seem trivial, but consider, a standard IP header is 20 bytes in size, some of this is covered by required obvious information, (4 bytes for source IP, 4 bytes for destination IP), etc but some of this header may be other arbitrary options, the TCP header is at least 20 bytes also, with the potential for another 20 bytes of options. The specific configuration of these options varies between operating systems, and even versions of operating system, as such a single TCP SYN packet is often enough to identify a users operating system, version and other potentially revealing information, like the systems uptime. There are [readily available tools](http://lcamtuf.coredump.cx/p0f3/) which you can use to fingerprint this information, as a test, try connecting to a server running this tool with your normal internet connection, then connecting again over your VPN. You will most likely find that the fingerprints are an identicle match both with and without the VPN, and that if your friend were to connect their fingerprint would be different.

As such, it is important to remember some facts:
 * No one will go to jail for you, if your VPN provider is served a legal request for information about you, they will provide it. Just because they claim they don't log, does not mean they do not have logs. VPNs provide privacy, they do not provide anonymity, regardless of the advertising and marketing materials provided.