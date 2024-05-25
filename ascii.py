import  sys

def center_text(text, width):
    return text.center(width)
def show_ascii():
    # Bảng tên các ký tự điều khiển ASCII
    control_chars = [
        "[NULL]", "[START OF HEADING]", "[START OF TEXT]", "[END OF TEXT]", "[END OF TRANSMISSION]",
        "[ENQUIRY]", "[ACKNOWLEDGE]", "[BELL]", "[BACKSPACE]", "[HORIZONTAL TAB]",
        "[LINEFEED]", "[VERTICAL TAB]", "[FORM FEED]", "[CARRIAGE RETURN]", "[SHIFT OUT]",
        "[SHIFT IN]", "[DATA LINK ESCAPE]", "[DEVICE CONTROL 1]", "[DEVICE CONTROL 2]",
        "[DEVICE CONTROL 3]", "[DEVICE CONTROL 4]", "[NEGATIVE ACKNOWLEDGE]",
        "[SYNCHRONOUS IDLE]", "[END OF TRANS. BLOCK]", "[CANCEL]", "[END OF MEDIUM]",
        "[SUBSTITUTE]", "[ESCAPE]", "[FILE SEPARATOR]", "[GROUP SEPARATOR]",
        "[RECORD SEPARATOR]", "[UNIT SEPARATOR]", "[SPACE]"
    ]

    # Hàm để trả về tên ký tự điều khiển hoặc ký tự ASCII thông thường
    def get_char_repr(dec):
        if dec < len(control_chars):
            return control_chars[dec]
        elif dec == 127:
            return "[DELETE]"
        else:
            return chr(dec)

    # Mở tệp để ghi
    with open('ascii_table2.txt', 'w') as file:
        # In các dòng trong bảng cho các ký tự từ 0 đến 31 và 127
        for i in range(128):
            dec_str = str(i).ljust(6)
            hex_str = f"0x{i:x}".ljust(8)
            char_str = get_char_repr(i)
            file.write(f"{dec_str}{hex_str}\t{char_str}\n")

    print("Bảng ASCII đã được ghi vào file ascii_table.txt")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    param = input()
    if param == '-sh' or param == '-show' or param.strip() == '':
        show_ascii()
        print("hi")

