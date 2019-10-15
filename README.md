

![Trench](trench.png)
<pre>Author: Dubem Nwoji</pre>
# Machine Learning for Encrypted Network Packet Analysis

### Introduction
<pre> Over the years, well-meaning stakeholders have strived to build trust into the internetwork of computers that we call the "web". In the last two years, however, a changing climate of mistrust has begun to grow and it is no surprise it correlates with the exponential growth of data. 

As more and more encryption is leveraged to protect communication and resources in the ever busy ebb and flow that is the web, there is a rising threat hidden in the shadows of TLS traffic - <bold>encrypted malware</bold>.

More effective mitigation techniques, such as packet sniffing (break and inspect) require a packet be "way-layed", decrypted, and the content, assessed for malicious content, before re-encrypting and sending it off on its way (if found to be benign). This solution, will necessary, poses a threat to the very trust that we strive to uphold. In addition to these privacy concerns is the latency and extra overhead introduced to the network - which in huge enterprise settings could lead to significant time and resource loss running into thousands (sometimes millions of dollars).

<bold>The Proposal</bold> - What if privacy and safety are not mutually exclusive and we can provide network administrators, security engineers, and end users, security while upholding trust and privacy?
</pre>
### Tools
### Dependencies

### Dependencies
#### Joy
- Description
- Link
*Steps*
1. Install Joy dependencies:

       [sudo] apt-get update
      
       [sudo] apt-get install gcc git libcurl3 libcurl4-openssl-dev libpcap0.8 libpcap-dev libssl-dev make python python-pip ruby ruby-ffi libz-dev
      
2. Download Joy:
    
       git clone https://github.com/cisco/joy.git
       cd joy

3.  Configure:

        ./configure --enable-gzip
       
4.  Build:
      
        make clean; make

5.  Installation:
  
        sudo ./install_joy/install-sh
        
To run offline:
  
    bin/joy [option] filename
    e.g. bin/joy bidir=1 http=1 dns=1 tls=1 dist=1  data.pcap > data.json

       
       

