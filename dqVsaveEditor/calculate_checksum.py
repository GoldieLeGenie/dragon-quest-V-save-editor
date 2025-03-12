data_size = 11128       
checksum_offset = 8 

def checksum(file_path):
    with open(file_path, "r+b") as f:
        data = bytearray(f.read(data_size))
        
        data[checksum_offset:checksum_offset + 4]
        data[checksum_offset:checksum_offset + 4] = bytes([0, 0, 0, 0])
        checksum = 0
        for i in range(data_size):
            checksum += data[i]  
        checksum &= 0xFFFFFFFF 
        data[checksum_offset:checksum_offset + 4] = checksum.to_bytes(4, byteorder="little")

        f.seek(0)
        f.write(data)
        print("Checksum replaced!")

