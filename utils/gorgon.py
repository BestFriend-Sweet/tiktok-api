import hashlib
import random
import struct
import time


class Gorgon:
    digits   = {c: i for i, c in enumerate("0123456789abcdefghijklmnopqrstuvwxyz")}
    HEX_STRS = [[30 ,0 ,224 ,220 ,147 ,69 ,1 ,200 ],[30 ,0 ,224 ,236 ,147 ,69 ,1 ,200 ],[30 ,0 ,224 ,228 ,147 ,69 ,1 ,208 ],[30 ,60 ,224 ,244 ,147 ,69 ,0 ,216 ],[30 ,64 ,224 ,228 ,147 ,69 ,0 ,216 ],[30 ,0 ,224 ,227 ,147 ,69 ,1 ,213 ],[30 ,64 ,224 ,210 ,147 ,69 ,0 ,160 ],[30 ,64 ,224 ,203 ,147 ,69 ,0 ,150 ],[30 ,64 ,224 ,211 ,147 ,69 ,0 ,167 ],[30 ,64 ,224 ,228 ,147 ,69 ,0 ,156 ],[30 ,64 ,224 ,216 ,147 ,69 ,0 ,216 ],[30 ,64 ,224 ,226 ,147 ,69 ,0 ,205 ],[30 ,64 ,224 ,214 ,147 ,69 ,0 ,176 ],[30 ,64 ,224 ,217 ,147 ,69 ,0 ,180 ],[30 ,64 ,224 ,240 ,147 ,69 ,0 ,213 ],[30 ,64 ,224 ,210 ,147 ,69 ,0 ,216 ],[30 ,64 ,224 ,235 ,147 ,69 ,0 ,192 ],[30 ,64 ,224 ,234 ,147 ,69 ,0 ,193 ],[30 ,64 ,224 ,234 ,147 ,69 ,0 ,186 ],[30 ,64 ,224 ,171 ,147 ,69 ,0 ,136 ],[30 ,64 ,224 ,103 ,147 ,69 ,0 ,166 ],[30 ,64 ,224 ,167 ,147 ,69 ,0 ,15 ],[30 ,64 ,224 ,139 ,147 ,69 ,0 ,182 ],[30 ,64 ,224 ,194 ,147 ,69 ,0 ,84 ],[30 ,64 ,224 ,183 ,147 ,69 ,0 ,170 ],[30 ,64 ,224 ,205 ,147 ,69 ,0 ,125 ],[30 ,64 ,224 ,138 ,147 ,69 ,0 ,175 ],[30 ,64 ,224 ,229 ,147 ,69 ,0 ,12 ],[30 ,64 ,224 ,163 ,147 ,69 ,0 ,26 ],[30 ,64 ,224 ,105 ,147 ,69 ,0 ,35 ],[30 ,64 ,224 ,167 ,147 ,69 ,0 ,24 ],]
    LEN      = 20

    def calculate(self, params, cookie, body):

        self.hex_str  = random.choice(self.HEX_STRS)
        hash          = self.getGorgonHash(params, body, cookie)
        hexEncryption = self.encryption()
        gorgonHash    = self.initGorgonHash(hash, hexEncryption)

        result = ""
        handle = self.handle(gorgonHash["gorgon"])

        for item in handle:
            result += self.hex2str(item)

        hash_1 = self.hex2str(self.hex_str[7])
        hash_2 = self.hex2str(self.hex_str[3])
        hash_3 = self.hex2str(self.hex_str[1])
        hash_4 = self.hex2str(self.hex_str[6])

        return {
            "X-Gorgon": "0404{}{}{}{}{}".format(hash_1, hash_2, hash_3, hash_4, result),
            "X-Khronos": str(hash["time"]),
        }

    def charCodeAt(self, str, i):
        return self.get_bianma((str[i:1]))

    def encryption(self):
        pass
        # removed from preview
        

    def ensureMax(self, val, max=256):
        pass
        # removed from preview
        

    def epoch(self):
        return int(round(time.time()))

    def convert_base(self, hex, base):
        pass
        # removed from preview
        

    def fromHex(self, hex):
        pass
        # removed from preview
        

    def getGorgonHash(self, url, data=None, cookie=None, encoding="UTF-8"):
        pass
        # removed from preview
        

    def get_bianma(self, str):
        pass
        # removed from preview
        

    def handle(self, gorgonHash):
        pass
        # removed from preview
        

    def hex2str(self, num):
        tmp = self.toHex(num)
        if len(tmp) < 2:
            tmp = "0" + tmp
        return tmp

    def initGorgonHash(self, gorgonHash, hexEncryption):
        pass
        # removed from preview
        

    def ranges(self, start=0, stop=None, step=1):
        pass
        # removed from preview
        

    def rbit(self, num):
        pass
        # removed from preview
        

    def toHex(self, num):
        pass
        # removed from preview
        

    def uniord(self, str, from_encoding=False):
        pass
        # removed from preview
        

    def xGorgon_cookie(self, cookie, encoding="utf-8"):
        pass
        # removed from preview
        

    def xGorgon_data(self, data: (bytes or None or str), encoding="utf-8"):
        pass
        # removed from preview
        
