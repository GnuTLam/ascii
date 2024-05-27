import sys

COLOR_GREEN = "\x1b[38;5;42m"
COLOR_ORANGE = "\x1b[38;5;173m"
COLOR_BLUE = "\x1b[38;5;105m"
COLOR_CREAM = "\x1b[38;5;223m"
COLOR_RESET = "\033[0m"

ascii_data = (('0', '0x0', '[NULL]'),
              ('1', '0x1', '[START OF HEADING]'),
              ('2', '0x2', '[START OF TEXT]'),
              ('3', '0x3', '[END OF TEXT]'),
              ('4', '0x4', '[END OF TRANSMISSION]'),
              ('5', '0x5', '[ENQUIRY]'),
              ('6', '0x6', '[ACKNOWLEDGE]'),
              ('7', '0x7', '[BELL]'),
              ('8', '0x8', '[BACKSPACE]'),
              ('9', '0x9', '[HORIZONTAL TAB]'),
              ('10', '0xa', '[LINEFEED]'),
              ('11', '0xb', '[VERTICAL TAB]'),
              ('12', '0xc', '[FORM FEED]'),
              ('13', '0xd', '[CARRIAGE RETURN]'),
              ('14', '0xe', '[SHIFT OUT]'),
              ('15', '0xf', '[SHIFT OUT]'),
              ('16', '0x10', '[DATA LINK ESCAPE]'),
              ('17', '0x11', '[DEVICE CONTROL 1]'),
              ('18', '0x12', '[DEVICE CONTROL 2]'),
              ('19', '0x13', '[DEVICE CONTROL 3]'),
              ('20', '0x14', '[DEVICE CONTROL 4]'),
              ('21', '0x15', '[NEGATIVE ACKNOWLEDGE]'),
              ('22', '0x16', '[SYNCHRONOUS IDLE]'),
              ('23', '0x17', '[END OF TRANS. BLOCK]'),
              ('24', '0x18', '[CANCEL]'),
              ('25', '0x19', '[END OF MEDIUM]'),
              ('26', '0x1a', '[SUBSTITUTE]'),
              ('27', '0x1b', '[ESCAPE]'),
              ('28', '0x1c', '[FILE SEPARATOR]'),
              ('29', '0x1d', '[GROUP SEPARATOR]'),
              ('30', '0x1e', '[RECORD SEPARATOR]'),
              ('31', '0x1f', '[UNIT SEPARATOR]'),
              ('32', '0x20', '[SPACE]'),
              ('33', '0x21', ' !'),
              ('34', '0x22', ' "'),
              ('35', '0x23', ' #'),
              ('36', '0x24', ' $'),
              ('37', '0x25', ' %'),
              ('38', '0x26', ' &'),
              ('39', '0x27', ' \''),
              ('40', '0x28', ' ('),
              ('41', '0x29', ' )'),
              ('42', '0x2a', ' *'),
              ('43', '0x2b', ' +'),
              ('44', '0x2c', ' ,'),
              ('45', '0x2d', ' -'),
              ('46', '0x2e', ' .'),
              ('47', '0x2f', ' /'),
              ('48', '0x30', ' 0'),
              ('49', '0x31', ' 1'),
              ('50', '0x32', ' 2'),
              ('51', '0x33', ' 3'),
              ('52', '0x34', ' 4'),
              ('53', '0x35', ' 5'),
              ('54', '0x36', ' 6'),
              ('55', '0x37', ' 7'),
              ('56', '0x38', ' 8'),
              ('57', '0x39', ' 9'),
              ('58', '0x3a', ' :'),
              ('59', '0x3b', ' ;'),
              ('60', '0x3c', ' <'),
              ('61', '0x3d', ' ='),
              ('62', '0x3e', ' >'),
              ('63', '0x3f', ' ?'),
              ('64', '0x40', ' @'),
              ('65', '0x41', ' A'),
              ('66', '0x42', ' B'),
              ('67', '0x43', ' C'),
              ('68', '0x44', ' D'),
              ('69', '0x45', ' E'),
              ('70', '0x46', ' F'),
              ('71', '0x47', ' G'),
              ('72', '0x48', ' H'),
              ('73', '0x49', ' I'),
              ('74', '0x4a', ' J'),
              ('75', '0x4b', ' K'),
              ('76', '0x4c', ' L'),
              ('77', '0x4d', ' M'),
              ('78', '0x4e', ' N'),
              ('79', '0x4f', ' O'),
              ('80', '0x50', ' P'),
              ('81', '0x51', ' Q'),
              ('82', '0x52', ' R'),
              ('83', '0x53', ' S'),
              ('84', '0x54', ' T'),
              ('85', '0x55', ' U'),
              ('86', '0x56', ' V'),
              ('87', '0x57', ' W'),
              ('88', '0x58', ' X'),
              ('89', '0x59', ' Y'),
              ('90', '0x5a', ' Z'),
              ('91', '0x5b', ' ['),
              ('92', '0x5c', ' \\'),
              ('93', '0x5d', ' ]'),
              ('94', '0x5e', ' ^'),
              ('95', '0x5f', ' _'),
              ('96', '0x60', ' `'),
              ('97', '0x61', ' a'),
              ('98', '0x62', ' b'),
              ('99', '0x63', ' c'),
              ('100', '0x64', ' d'),
              ('101', '0x65', ' e'),
              ('102', '0x66', ' f'),
              ('103', '0x67', ' g'),
              ('104', '0x68', ' h'),
              ('105', '0x69', ' i'),
              ('106', '0x6a', ' j'),
              ('107', '0x6b', ' k'),
              ('108', '0x6c', ' l'),
              ('109', "0x6d", ' m'),
              ('110', '0x6e', ' n'),
              ('111', '0x6f', ' o'),
              ('112', '0x70', ' p'),
              ('113', '0x71', ' q'),
              ('114', '0x72', ' r'),
              ('115', '0x73', ' s'),
              ('116', '0x74', ' t'),
              ('117', '0x75', ' u'),
              ('118', '0x76', ' v'),
              ('119', '0x77', ' w'),
              ('120', '0x78', ' x'),
              ('121', '0x79', ' y'),
              ('122', '0x7a', ' z'),
              ('123', '0x7b', ' {'),
              ('124', '0x7c', ' |'),
              ('125', '0x7d', ' }'),
              ('126', '0x7e', ' ~'),
              ('127', '0x7f', ' [DELETE]'),
              ('', '', ''))


def line_format(line):
    w0 = COLOR_BLUE + line[0]
    w1 = COLOR_GREEN + line[1]
    w2 = COLOR_CREAM + line[2]
    return " " + w0.ljust(19) + w1.ljust(24) + w2


def show_ascii():
    print(COLOR_ORANGE + "-DEC-   -HEX-         -CHARACTER-".ljust(64) + "-DEC-   -HEX-         -CHAR-" + COLOR_RESET)
    for i in range(64):
        print(line_format(ascii_data[i]).ljust(96), end='')
        print(line_format(ascii_data[i + 64]))


def search_ascii(character=''):
    if character == '':
        print(COLOR_ORANGE + "-DEC-   -HEX-         -CHAR-")
        print(line_format(ascii_data[0]))
        return
    decimal = ord(character)
    print(COLOR_ORANGE + "-DEC-   -HEX-         -CHAR-")
    print(line_format(ascii_data[decimal]))


if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            if sys.argv[1] == '--s' or sys.argv[1] == '-search':
                if len(sys.argv) == 2:
                    search_ascii()
                else:
                    search_ascii(sys.argv[2])
        else:
            show_ascii()
    except Exception as e:
        print(f"An error occurred: {e}")
