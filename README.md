# Application-Level-Threat-Intel-System

![Trench](trench.png)
Machine Learning for packet analytics of encrypted network traffic

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

       
       

