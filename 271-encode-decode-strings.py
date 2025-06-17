'''
original = ['i' 'love' 'cp' '#4']
encoded = "1i4love2cp2#4"
decoded = ['i' 'love' 'cp' '#4']
'''
class Transcode:

    def encode(self, strs : list[str]) -> str:
        encoded = []
        for word in strs:
            count = str(len(word))
            encoded.append(count + "#" + word)
        print("".join(encoded))
        return "".join(encoded)

    def decode(self, str: str) -> list[str]:
        sentence = []
        i = 0
        while (i < len(str)):
            j = i
            while (str[j] != "#"):
                j += 1
            lengthOfWord = int(str[i:j])
            j += 1
            word = str[j : j+lengthOfWord]
            sentence.append(word)
            i = j + lengthOfWord
        return sentence

if __name__ == "__main__":
    print(Transcode().decode(Transcode().encode(["IIIIIIIIIIIIIIIIIIIIIIIIIII","love","cp","#4"])))