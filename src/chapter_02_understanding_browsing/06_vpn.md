VPN
===

The way your data makes it to the desired server and back to your laptop computer or a mobile device is not as straightforward as it might first seem. Say, you are connected to a wireless network at home and opening a wikipedia.org page. The path your request (data) takes will consist of multiple middle points or *"hops"* - in network-architect terminology. At each of these hops (which are likely to be more then 5) your data can be scooped, copied and potentially modified.

 * Your wireless network (your data can be sniffed from the air)
 * Your ISP (in most countries they are obliged to keep detailed logs of user activity)
 * Internet Exchange Point (IXP) somewhere on another continent (usually more secure then any other *hop*)
 * ISP of the hosting company that hosts the site (is probably keeping logs)
 * Internal network to which the server is connected
 * And multiple hops between...

Any person with physical access to the computers or the networks which are on the way from you to the remote server, intentionally or not, can collect and reveal the data that's passing from you to the remote server and back. This is especially true for so called 'last mile' situations - the few last leaps that an internet connection makes to reach a user. That includes domestic and public wireless or wired networks, telephone and mobile networks, networks in libraries, homes, schools, hotels. Your ISP can not be considered a safe, or 'data-neutral' instance either - in many countries state agencies do not even require a warrant to access your data, and there is always the risk of intrusion by paid attackers working for a deep-pocketed adversaries.

VPN - a Virtual Private Network - is a solution for this 'last-mile' leakage. VPN is a technology that allows the creation of a virtual network on top of an existing infrastructure. Such a VPN network operates using the same protocols and standards as the underlying physical network. Programs and OS use it transparently, as if it was a separate network connection, yet its topology or the way how network nodes (you, the VPN server and, potentially, other members or services available on VPN) are interconnected in relation to the physical space is entirely redefined.

Imagine that instead of having to trust your data to every single middle-man (your local network, ISP, the state) you have a choice to pass it via a server of a VPN provider whom you trust (after a recommendation or research) - from which your data will start its journey to the remote location. VPN allows you to recreate your local and geo-political context all together - from the moment your data leaves your computer and gets into the VPN network it is fully secured with TLS/SSL type encryption. And as such it will appear as pure random noise to any node who might be spying after you. It is as if your data was traveling inside a titanium-alloy pipe, unbreakable on all the way from your laptop to the VPN server. Of course one could argue that eventually, when your data is outside the safe harbour of VPN it becomes just as vulnerable as it was - but this is only partially true. Once your data exits the VPN server it is far away from you - way beyond the reach of some creeps sniffing on the local wireless network, your venal ISP or a local government obsessed with anti-terrorism laws. A serious VPN provider would have their servers installed at a high-security Internet exchange location, rendering any physical human access, tapping or logging a difficult task.

Another interesting and often underrated features of VPN is encoded in its name - besides being **V**irtual and **P**rivate it is also a **N**etwork. VPN allows one not only to connect via the VPN server to the rest of the world but also to communicate to other members of the same VPN network without ever having to leave the safety of encrypted space. Since a connection to VPN server, and thus the private network it facilitates, require a key or a *certificate*, only "invited" users are allowed. There is no chance that Internet stranger would gain access to what's on a VPN without enrolling as a user or stealing someones keys. 

> "A virtual private network (VPN) extends a private network across a public network, such as the Internet. It enables a computer to send and receive data across shared or public networks as if it were directly connected to the private network, while benefitting from the
 functionality, security and management policies of the private network."([http://en.wikipedia.org/wiki/Virtual_private_network](http://en.wikipedia.org/wiki/Virtual_private_network))

Many commercial VPN providers stress the anonymity that their service provides. 

Indeed, when you access the Internet via a VPN connection it does appear as if the connection is originating from the IP address of IPredator servers.

Choosing the right VPN is very important since you're entrusting them with your data and there are things that you should look for when you're choosing your vpn and we'll discuss it in details later.
