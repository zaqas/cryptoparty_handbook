Using GPG In Terminal
===============

Probably one of the safest way to encrypt an email is to encypt it outside of an application and then copy & paste the encrypted text into the browser window.

For example, write the text in a text editor like gedit, vim or kate and save it as .txt file (in this example "message.txt". Then type

    gpg -ase -r <recipients email/gpg id> -r <your gpg id> message.txt

A new file called "message.asc" will be created. It contains the encrypted message and can thus be either attached to an email or its content safely copy & pasted into the browser window.

To decrypt a message from the browser window, simply type `gpg` into the command line and hit Enter. Then copy & paste the message to be decrpyted into the commandline window and after being asked for your passphrase hit Ctrl+D (this enters a end-of-file character and prompts gpg to output the cleartext message).

If using the command line seems too cumbersome to you, you might consider using an application like  Seahorse, KGpg or whatever application ships with your operating system.

Another way to encrypt email inside of the browser is to use an add-on called Mailvelope. We will discuss how to install and use it later.