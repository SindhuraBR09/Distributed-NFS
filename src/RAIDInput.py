class RAIDInput:
    def __init__(self, filename, filedata):
        self.filename = filename
        self.data = filedata
        self.bindata = self.convertToBinary(filedata)

    def convertToBinary(self, data):
        binary_data = []

        for x in data:
            binary_data.append(format(ord(x), 'b'))

        return binary_data

    def convertToStr(self, binary):
        data_str = ""
        for x in binary:
            data_str += chr(int(x, 2))

        print(data_str)

# test = RAIDInput('','This is a string')
# test.convertToStr(test.bindata)
