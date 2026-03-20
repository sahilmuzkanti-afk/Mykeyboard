import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18)
keyboard.row_pins = (board.GP18, board.GP19, board.GP20, board.GP21, board.GP22)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.NO, KC.NO, KC.EQUAL, KC.MACRO([Press(KC.LPRN), Press(KC.RPRN), Tap(KC.LEFT)]), KC.MACRO([Press(KC.LCBR), Press(KC.RCBR), Tap(KC.LEFT)])],
    [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLASH, KC.NO, KC.NO, KC.PLUS, KC.MACRO([Tap(KC.LBRACKET), Tap(KC.RBRACKET), Tap(KC.LEFT)]), KC.MACRO([Tap(KC.QUOTE), Tap(KC.QUOTE), Tap(KC.LEFT)])],
    [KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.NO, KC.NO, KC.MINUS, KC.COLON],
    [KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.UP, KC.DOWN, KC.SLASH, KC.LABK, KC.RABK],
    [KC.LCTRL, KC.LALT, KC.LCMD, KC.SPACE, KC.RCMD, KC.RALT, KC.RCTRL, KC.GRAVE, KC.LEFT, KC.RIGHT, KC.ASTERISK, KC.BSLASH, KC.EXCLAIM]
]

if __name__ == '__main__':
    keyboard.go()
