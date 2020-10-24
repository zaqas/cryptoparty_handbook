File Sharing
============

The term *File Sharing* refers to the practice of sharing files on a network, often with widest possible distribution in mind. Unfortunately in recent years the term has come to be popularly associated with the distribution of content registered under certain copyright licenses that disallow the distribution of copies (eg. supposed criminal activity). Regardless of this new association, file sharing remains a vital tool for many world wide: from academic groups to scientific networks and open source software communities.

In this book we wish to help you learn to privately distribute files, with other consenting people, without the content of that exchange known to others or the transaction stopped by an external party. Your basic right to anonymity and to not be spied upon protects that. Suspicions that those things *might* have been stolen and are not yours to give does not undermine that same and original right to privacy. 

The history of the internet is littered with attacks of different types on publication and distribution nodes, conducted by different means (court order, Distributed Denial of Service attacks). What such events have demonstrated is that if one wants information to be persistently available and robust against attack, it is a mistake to rely upon a single node which can be neutralised.

This has recently been demonstrated by the takedown of the direct download service Megaupload, whose disappearance led to the loss of massive amounts of its users' data, much of it extraneous even to the alleged copyright infringements which formed the pretext for its closure. In similar vein ISPs will often take down web sites containing disputed material merely because it is cheaper for them to do so than to go to court and have a judge decide. Such policies leave the door open to groundless bullying by all manner of companies, organisations and individuals ready and willing to make aggressive use of legal letters. Both direct download services and ISPs are examples of centralised structures which cannot be relied upon both because they are a single point of failure for attack, and because their commercial interests are not aligned with those of their users. 

Spreading files through distribution, decentralising the data, is the best way to defend against such attacks. In the following section two realms of file sharing are profiled. The first are standard p2p technologies whose technical design is determined by the efficiency of the networks in enabling speed of distribution and discovery of content through associated search mechanisms. The second focuses on I2P as an example of a so-called darknet, its design prioritises security and anonymity over other criteria offering a robust, if less resource efficient, path to persistent availability.

The means of sharing files mentioned below are just some examples of the many P2P technologies that were developed since 1999. BitTorrent and Soulseek have very different approaches, both however were designed for easy usability by a wide public and have significant user communities. I2P is of more recent development and has a small user base.

**BitTorrent** has become the most popular P2P file-sharing system. The controversy that surrounds it nowadays ironically seems to help the community grow, while police, lobbied by powerful copyright holders seize torrent-tracker server hardware and pursue their operators, sometimes to the point of jailing them as in the case of The Pirate Bay. We'll discuss BitTorrent in details later.

**Soulseek** - while it has never been the most popular file-sharing platform, neither did it ever have the ambition. Soulseek focuses on the exchange of music between enthusiasts, underground producers, fans and researchers. The system and the community around it is completely isolated from the Web: Soulseek files can not be linked to. They are kept exclusively on the hard-disks of Soulseek users. The content of the network fully depends on how many members are connected and what they share. Files are transferred only between two users at a time and nobody but those two users are involved. Because of this 'introverted' character - and the specificity of its content - Soulseek has stayed out of sight of legislation and non-pro-copy copyright advocates.

**I2P** is one of several systems developed to resist censorship (others include FreeNet and Tor) and has a much smaller user community, it is highlighted here because of its inclusion of Bit Torrent functionality within its basic installation. These systems can also be used to provide hidden services, amongst others, enabling you to publish web pages within their environments.


SoulSeek
--------

As a peer to peer (P2P) file sharing program, the content available is determined by the users of the Soulseek client, and what files they choose to share. The network has historically had a diverse mix of music, including underground and independent artists, unreleased music, such as demos and mix-tapes, bootlegs, etc. It is is entirely financed by donations, with no advertising or user fees.

> "Soulseek does not endorse nor condone the sharing of copyrighted materials. You should only share and download files which you are legally allowed to, or have otherwise received permission to, share." ([http://www.soulseekqt.net](http://www.soulseekqt.net))

Soulseek network depends on a pair of central servers. One server supports the original client and network, and the other supporting the newer network. While these central servers are key to coordinating searches and hosting chat rooms, they do not actually play a part in the transfer of files between users, which takes place directly between the users concerned.

Users can search for items; the results returned being a list of files whose names match the search term used. Searches may be explicit or may use wildcards/patterns or terms to be excluded. A feature specific to the Soulseek search engine is the inclusion of the folder names and file paths in the search list. This allows users to search by folder name.

The list of search results shows details, such as the full name and path of the file, its size, the user who is hosting the file, together with that users' average transfer rate, and, in the case of mp3 files, brief details about the encoded track itself, such as bit rate, length, etc. The resulting search list may then be sorted in a variety of ways and individual files (or folders) chosen for download.

Unlike BitTorrent, Soulseek does not support multi-source downloading or "swarming" like other post-Napster clients, and must fetch a requested file from a single source.

While the Soulseek software is free, a donation scheme exists to support the programming effort and cost of maintaining the servers. In return for donations, users are granted the privilege of being able to jump ahead of non-donating users in a queue when downloading files (but only if the files are not shared over a local area network). The Soulseek protocol search algorithms are not published, as those algorithms run on the server. However several Open Source implementations of server and client software exist for Linux, OS X and Windows.

Regarding privacy and copyright issues Soulseek stand quite far away from BitTorrent too. Soulseek has been taken to court only once, in 2008, but even that did not go anywhere. There are no indications of Soulseek users ever being brought to court or accused of illegal distribution of copyrighted materials or any other 'digital-millenium' crimes.

If you want to use the Soulseek network with some degree of real anonymity, you will need to use it over a VPN.

I2P
---

I2P began as a fork from the Freenet project, originally conceived as a method for censorship-resistant publishing and distribution. From their website:

> The I2P project was formed in 2003 to support the efforts of those trying to build a more free society by offering them an uncensorable, anonymous, and secure communication system. I2P is a development effort producing a low latency, fully distributed, autonomous, scalable, anonymous, resilient, and secure network. The goal is to operate successfully in hostile environments - even when an organization with substantial financial or political resources attacks it. All aspects of the network are open source and available without cost, as this should both assure the people using it that the software does what it claims, as well as enable others to contribute and improve upon it to defeat aggressive attempts to stifle free speech. ([http://www.i2p2.de/](http://www.i2p2.de/))

For a guide to installing the software and configuring your browser see section on Secure Filesharing - Installing I2P. Once complete, on launch you will be brought to a console page containing links to popular sites and services. In addition to the usual webpages (referred to as eePsites) there are a range of applications services available ranging from the blogging tool Syndie to a built in BitTorrent client which functions through a web interface.
