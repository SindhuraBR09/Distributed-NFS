from RAIDInput import RAIDInput


def chunks(file_name, size=100000):
    with open('large-file.txt') as f:
        while content := f.read(size):
            yield content


if __name__ == '__main__':
    split_files = chunks('test_file')
    for chunk in split_files:
        print(len(chunk))
        


# if __name__ == "__main__":
#     with open('testfile.txt') as f:
#         content = f.read()
#         raidInput = RAIDInput('testfile', content)
#         raidInput.convertToStr(raidInput.bindata)
