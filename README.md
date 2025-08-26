# THM--Takedown

This was a fantastic CTF from TryHackMe.
I have uploaded the python scripts I used to exploit the C2 and pivot to the agent.
Code is far from perfect, just enough to get the job done. You probably need to make edits to serve your needs. 
Analyze the implant to discover the execution guard rails. This should give you enough info to emulate a compromised client.
Data gained through analyzing the C2 comms with the implant exposes LFI on the C2, and more.
Exploits LFI, Enumerates C2 implant ID's, and spawns reverse shells from C2 server as well pivoting to another "compromised host" for the root flag.
