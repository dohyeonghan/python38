
class PythonEncoder:
    @staticmethod
    def unicode_korean(korean_str: str) -> None:
        """
        ord : 문자에 해당하는 유니코드 정수를 반환
        hex : 정수값을 받아 16진수 str로 변환
        유니코드 AC0 + 0 : '가'
        """
        print('Unicode code point of 가 : ' + hex(ord(korean_str)))

    @staticmethod
    def utf8_encode(korean_str: str) -> None:
        """
        xea/xb0/x80

        xea = 0xEA
        - 16진수 EA : 10진수 234
        - '가'의 유니코드 코드 포인트 AC00에서 상위 바이트

        xb0 = 0xB0
        - 10진수 176
        - '가'의 유니코드 코드 포인트 AC00에서 하위 바이트

        x80 = 0x80
        - 10진수 128
        다중 바이트 문자의 일부로 사용 -> '가'를 완전히 표현

        """
        utf8 = korean_str.encode('utf-8')
        print(f'UTF-8 value of {korean_str} : ' + str(utf8))
        print(f'{str(utf8)} is {utf8.decode("utf-8")}')

    @staticmethod
    def utf16_encode(korean_str: str) -> None:
        """
        utf16에서 BOM(0xFFFE) 사용하는 이유
        - UTF-8과 달리 바이트들의 조합만으로는 Byte Order를 유추할 수 없기 때문에

        BOM(Byte Order Mark)

        UTF-16에는 빅엔디안 모드와 리틀엔디안 모드가 있음
        -> BOM은 해당 형식을 구분하기 위해 존재

        ex) AC 00을 메모리에 저장할 떄
        빅엔디안은 AC 00
        리틀엔디안은 00 AC

        UTF-16 LE로 가나다 저장시
        fffe 00ac 98b0 e4b2
        """
        utf16 = korean_str.encode('utf-16')
        print(f'UTF-16 value of {korean_str} : ' + str(utf16))
        print(f'{str(utf16)} is {utf16.decode("utf-16")}')

def run():
    """
    Unicode code point of 가 : 0xac00
    UTF-8 value of 가 : b'\xea\xb0\x80'
    b'\xea\xb0\x80' is 가
    UTF-16 value of 가 : b'\xff\xfe\x00\xac'
    b'\xff\xfe\x00\xac' is 가
    """
    PythonEncoder.unicode_korean("가")
    PythonEncoder.utf8_encode("가")
    PythonEncoder.utf16_encode("가")

if __name__ == '__main__':
    run()