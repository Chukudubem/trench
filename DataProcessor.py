#!/usr/bin/env python
# coding: utf-8

import json
import numpy as np
import gzip

#ciphersuites
cs = {u'c005': 0, u'c004': 1, u'c007': 2, u'0039': 3, u'0038': 4, u'c003': 5, u'c002': 6, u'0035': 7, u'0034': 8, u'0037': 9, u'0036': 10, 
      u'c009': 11, u'c008': 12, u'0033': 13, u'0032': 14, u'c07a': 15, u'c07b': 16, u'c07c': 17, u'c07d': 18, u'0065': 19, 
      u'c087': 21, u'c086': 22, u'c081': 23, u'c080': 24, u'c072': 25, u'c073': 26, u'c076': 27, u'c077': 28, u'0040': 29, u'0041': 30, 
      u'0042': 31, u'feff': 32, u'0044': 33, u'0045': 34, u'0046': 35, u'0030': 36, u'c00e': 37, u'c00d': 38, u'c00f': 39, u'c00a': 40, 
      u'c00c': 41, u'003e': 42, u'003d': 43, u'003f': 44, u'003a': 45, u'003c': 46, u'003b': 47, u'006a': 109, u'00ff': 49, u'00fd': 50, 
      u'00fb': 51, u'00fc': 52, u'c08a': 53, u'c08b': 54, u'5600': 55, u'c05d': 56, u'c05c': 57, u'00af': 58, u'00ae': 59, u'0017': 113, 
      u'00a7': 60, u'00a6': 61, u'00a5': 62, u'00a4': 63, u'00a3': 64, u'00a2': 65, u'00a1': 66, u'00a0': 67, u'cc13': 68, u'cc15': 69, 
      u'cc14': 70, u'c049': 71, u'c048': 20, u'0016': 114, u'000d': 74, u'000f': 75, u'000a': 76, u'000c': 77, u'0064': 81, u'0066': 79, 
      u'0067': 80, u'00b0': 78, u'00b1': 82, u'0062': 83, u'0063': 84, u'0060': 85, u'0061': 86, u'0068': 87, u'0069': 88, u'0004': 89, 
      u'0005': 90, u'0006': 91, u'0007': 92, u'0001': 93, u'0002': 94, u'0003': 95, u'0008': 96, u'0009': 97, u'0031': 98, u'0019': 125,
      u'0018': 126, u'c030': 101, u'c031': 102, u'c032': 103, u'006d': 104, u'00ba': 105, u'006b': 106, u'006c': 107, u'00bd': 108, 
      u'00be': 48, u'00c4': 110, u'00c0': 111, u'00c3': 112, u'cca9': 72, u'cca8': 73, u'0015': 115, u'0014': 116, u'0013': 117, u'0012': 118, 
      u'0011': 119, u'0010': 120, u'c01b': 121, u'c01c': 122, u'c01a': 123, u'c01f': 124, u'c01d': 99, u'c01e': 100, u'002c': 127, u'002f': 128, 
      u'c029': 129, u'c028': 130, u'c027': 131, u'c026': 132, u'c025': 133, u'c024': 134, u'c023': 135, u'c022': 136, u'c021': 137, u'c020': 138, 
      u'009f': 139, u'009e': 140, u'009d': 141, u'009c': 142, u'009b': 143, u'009a': 144, u'0088': 145, u'0089': 146, u'0084': 147, u'0085': 148, 
      u'0086': 149, u'0087': 150, u'0043': 151, u'c02f': 152, u'c02e': 153, u'c02d': 154, u'c02c': 155, u'c02b': 156, u'c02a': 157, u'c018': 158, 
      u'c019': 159, u'001b': 160, u'001a': 161, u'c012': 162, u'c013': 163, u'c011': 164, u'c016': 165, u'c017': 166, u'c014': 167, u'008d': 168, 
      u'008a': 169, u'008b': 170, u'008c': 171, u'0099': 172, u'0098': 173, u'0097': 174, u'0096': 175}

#extensions
ext = {u'server_name': 0, u'extended_master_secret': 1, u'renegotiation_info': 2, u'supported_groups': 3, u'ec_point_formats': 4, 
       u'session_ticket': 5, u'application_layer_protocol_negotiation': 6, u'status_request': 7, u'signature_algorithms': 8}


class DataProcessor:
    
    '''
    Input:
    
    Output:
    
    '''
    def __init__(self, file):
        self.contents = []

        with gzip.open(file, 'rt') as f:
            next(f)
            try:
                for line in f:
                    try:
                        self.contents.append(json.loads(line))
                    except:
                        continue
            except:
                return
    
    def getTLSInfo(self):
        if self.contents == []: 
            return None
        
        data = []
        for content in self.contents:
            if len(content["packets"]) == 0:
                continue
            tls_info = np.zeros(len(cs.keys()) + len(ext.keys()) + 1)

            if 'tls' in content and 'cs' in content['tls']:
                for c in content['tls']['cs']:
                    if c in cs:
                        tls_info[cs[c]] = 1
            else:
                data.append([])
                continue

            if 'tls' in content and 'c_extensions' in content['tls']:
                for e in content['tls']['c_extensions']:
                    if list(e)[0] in ext:
                        tls_info[len(cs.keys()) + ext[list(e)[0]]] = 1

            if 'tls' in content and 'c_key_length' in content['tls']:
                tls_info[len(cs.keys()) + len(ext.keys())] = content['tls']['c_key_length']
            data.append(tls_info)
        return data
    
    def getByteDistribution(self):
        if self.contents == []: 
                return None
        
        data = []
        for content in self.contents:
            if len(content['packets']) == 0:
                continue
            if 'byte_dist' in content and np.sum(content['byte_dist']) > 0:
                tmp = list(map(lambda x: np.divide(x,float(np.sum(content['byte_dist']))) , content['byte_dist']))
                data.append(tmp)
            else:
                data.append(np.zeros(256))
        return data
    
    def getIndividualFlowPcktLengths(self):
        if self.contents == []: 
                return None
            
        nrows = 10
        bin_size = 150.0
        
        #Try nrow = 60, binsize = 25.0
        #Add if contents == []: return None
        '''
        Input: List of dictionary
        Example: [{'b': 151, 'dir': '>', 'ipt': 23},
                 {'b': 1460, 'dir': '<', 'ipt': 21},
                 {'b': 1286, 'dir': '<', 'ipt': 0}, 
                 {'b': 150, 'dir': '>', 'ipt': 14}]
        '''

        data = []

        for content in self.contents:
            tx_matrix = np.zeros((nrows, nrows))
            if len(content['packets']) == 0:
                continue
            elif len(content['packets']) == 1:
                current_pkt_size = min(int(content['packets'][0]['b']/bin_size), nrows-1)
                tx_matrix[current_pkt_size, current_pkt_size] = 1
                data.append(list(tx_matrix.flatten()))
                continue

            #get raw transition count
            for i in range(1, len(content['packets'])):
                previous_pkt_size = min(int(content['packets'][i-1]['b']/bin_size), nrows-1)
                if 'b' not in content['packets'][i]:
                    break
                current_pkt_size = min(int(content['packets'][i]['b']/bin_size), nrows-1)
                tx_matrix[previous_pkt_size, current_pkt_size] +=1

            #get empirical transition probabilities
            for i in range(nrows):
                if float(np.sum(tx_matrix[i:i+1])) != 0:
                    tx_matrix[i:i+1] = tx_matrix[i:i+1]/float(np.sum(tx_matrix[i:i+1]))

            data.append(tx_matrix.flatten())

        return data
    
    def getIndividualFlowIPTs(self):
    
        if self.contents == []:
            return None

        #Try nrows = 30, bin_size = 50.0
        nrows = 10 
        bin_size =50.0

        data = []
        for content in self.contents:
            tx_matrix = np.zeros((nrows,nrows))
            if len(content['packets']) == 0:
                continue
            elif len(content['packets']) == 1:
                current_IPT = min(int(content['packets'][0]['ipt']/float(bin_size)), nrows-1)
                tx_matrix[current_IPT, current_IPT] = 1
                data.append(list(tx_matrix.flatten()))
                continue

            # get raw transition counts
            for i in range(1, len(content['packets'])):
                previous_IPT = min(int(content['packets'][i-1]['ipt']/float(bin_size)), nrows-1)
                current_IPT = min(int(content['packets'][i]['ipt']/float(bin_size)), nrows-1)
                tx_matrix[previous_IPT, current_IPT]

            # get empirical transition probabilities
            for i in range(nrows):
                if float(np.sum(tx_matrix[i:i+1])) != 0:
                    tx_matrix[i:i+1] = tx_matrix[i:i+1]/float(np.sum(tx_matrix[i:i+1]))

            data.append(tx_matrix.flatten())

        return data
    
    
    def getIndividualFlowMetadata(self):
        if self.contents == []:
            return None
        
        data = []
        
        for content in self.contents:
            if len(content['packets']) == 0:
                continue
            tmp = []

            key = content['sa'] + "-" + content['da'] + "-" + str(content['sp']) + "-" + str(content['dp']) + "-" + str(content['pr'])


            if content['dp'] != None:
                tmp.append(float(content['dp'])) # destination port
            else:
                tmp.append(0) #ICMP/etc.
            if content['sp'] != None:
                tmp.append(float(content['sp'])) # source port
            else:
                tmp.append(0) #ICMP/etc.      
            if 'num_pkts_in' in content:
                tmp.append(content['num_pkts_in']) # inbound packets
            else:
                tmp.append(0)
            if 'num_pkts_out' in content:
                tmp.append(content['num_pkts_out']) # outbound packets
            else:
                tmp.append(0)
            if 'bytes_in' in content:
                tmp.append(content['bytes_in']) # inbound bytes
            else:
                tmp.append(0)
            if 'bytes_out' in content:
                tmp.append(content['bytes_out']) # outbound bytes
            else:
                tmp.append(0)
            if content['packets'] == []: # elapsed time of flow
                tmp.append(0)
            else:
                time = 0
                for packet in content['packets']:
                    time += packet['ipt']
                tmp.append(time)
            tmp.append(key)
            data.append(tmp)
            
        if data == []:
            return None
        
        return data 

