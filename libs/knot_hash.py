#!/usr/bin/python3

from _functools import reduce

class Knot_hash:

    def getSubList(self, position, length, hash_arr):
        hash_size = len(hash_arr)
        circular_arr = hash_arr + hash_arr
        pos_from = position%hash_size
        pos_to = pos_from+length
        sub_list = circular_arr[pos_from:pos_to]
        return sub_list

    def reverse(self, list):
        return list[::-1]

    def substituteArray(self, position, hash_arr, sub_list):
        hash_size = len(hash_arr)
        i = 0
        while i < len(sub_list):
            substitute_pos = (position + i)%hash_size 
            hash_arr[substitute_pos] = sub_list[i]
            i += 1
        return hash_arr

    def xorDenseHash(self, sparse_hash):
        dense_hash = []
        for pos in range(16):
            from_pos = pos * 16
            to_pos = from_pos + 16
            sublist = sparse_hash[from_pos:to_pos]
            dense_part = reduce(lambda x, y: x ^ y, sublist)
            dense_hash.append(dense_part)

        # print(dense_hash)
        return dense_hash

    def generateHash(self, dense_hash):
        hex_arr = []
        for ascii in dense_hash:
            hex_raw = hex(ascii)
            hex_ = hex_raw.split("x")[1]
            if len(hex_) < 2:
                hex_ = "0" + hex_
            hex_arr.append(hex_)
        return "".join([s for s in hex_arr])


    def generate(self, input):
        list_size = 256
        hash_arr = list(range(list_size))

        add_sequence = [17, 31, 73, 47, 23]
        lengths = [ord(ch) for ch in list(input)]  
        lengths = lengths + add_sequence

        position = 0
        skip = 0
        for _ in range(64):
            for length in lengths:
                sub_list = self.reverse(self.getSubList(position, length, hash_arr))
                hash_arr = self.substituteArray(position, hash_arr, sub_list)
                position += (length + skip)%len(hash_arr)
                skip += 1
        
        sparse_hash = hash_arr
        dense_hash = self.xorDenseHash(sparse_hash)
        final_hash = self.generateHash(dense_hash)
        return final_hash