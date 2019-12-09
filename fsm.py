from transitions.extensions import GraphMachine

from utils import send_text_message
import random

base = ["Gin", "Vodka", "Tequila", "Whisky", "Rum", "Brandy"]
flavor = ["高酒精", "中酒精", "低酒精", "莓果", "柳橙", "柑橘",
          "甜", "酸", "酸甜", "氣泡", "鹽口", "薄荷", "藥草"
          ]
db = [["Alexander亞歷山大\n充滿巧克力及奶香的白蘭地調酒\n45ml 干邑白蘭地\n30ml 黑莫札特\n20ml 鮮奶油加鮮奶", [5], [0, 1, 5]],
      ["Martini馬丁尼\n雞尾酒之王\n60ml 琴酒\n20ml 香艾酒\n1dash 柑橘苦精", [0], [0, 12]],
      ["Long Island Iced Tea長島冰茶\n今晚趕進度\n15ml 琴酒\n15ml 龍舌蘭\n15ml 伏特加\n15ml 白蘭姆酒\n15ml 君度橙酒\n30ml Gomme sycup\n25ml 新鮮檸檬汁\n適量 可樂", [
          0, 1, 2, 4], [0, 5, 8, 9]],
      ["Manhattan曼哈頓\n優雅的調酒之后\n50ml 裸麥威士忌\n20ml 香艾酒\n1dash 安格仕苦精", [3], [0, 6, 12]],
      ["Mojito莫希托\nMy mojito in La Bodeguita - 海明威\n40ml 萊姆酒\n30ml 新鮮萊姆汁\n6束 薄荷葉\n2tsp 白砂糖\n適量 蘇打水",
          [4], [1, 2, 8, 9, 11]],
      ["Tequila Sunrise龍舌蘭日出\nIt's anpther tequila sunrise - 老鷹合唱團\n45ml 龍舌蘭\n90ml 柳橙汁\n15ml 紅石榴糖漿", [2], [2, 3, 4, 8]],
      ["Gin Rickey琴瑞奇\n十分純粹的一杯不甜調酒\n45ml 琴酒\n15ml 檸檬汁\n適量 蘇打水", [0], [1, 2, 7, 9, 12]],
      ["Margarita瑪格麗特\nMier\n35ml 龍舌蘭\n20ml 君度橙酒\n15ml 萊姆汁", [2], [0, 1, 5, 8, 10]]
      ]


def search_base(idx):
    restr = ""
    for s in db:
        if idx in s[1]:
            restr = restr + s[0]
            if db.index(s) != (len(db)-1):
                restr = restr + "\n"
    return restr


def search_flavor(idx):
    restr = ""
    for s in db:
        if idx in s[2]:
            restr = restr + s[0]
            if db.index(s) != (len(db)-1):
                restr = restr + "\n"
    return restr


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_base(self, event):
        text = event.message.text
        return text.lower() == "base"

    def is_going_to_flavor(self, event):
        text = event.message.text
        return text.lower() == "flavor"

    def is_going_to_random(self, event):
        text = event.message.text
        return text.lower() == "random"

    def on_enter_base(self, event):
        print("In base")
        reply_token = event.reply_token
        send_text_message(
            reply_token,
            "基酒：Gin(g)、Vodka(v)、Tequila(t)、Whisky(w)、Rum(r)、Brandy(b)"
        )

    def on_exit_base(self, event):
        print("Leave base")

    def on_enter_flavor(self, event):
        print("In flavor")
        reply_token = event.reply_token
        send_text_message(
            reply_token,
            "口味：高酒精(a)、中酒精(b)、低酒精(c)、莓果(d)、柳橙(e)、柑橘(f)、甜(g)、酸(h)、酸甜(i)、氣泡(j)、鹽口(k)、薄荷(l)、藥草(m)"
        )

    def on_exit_flavor(self, event):
        print("Leave flavor")

    def on_enter_random(self, event):
        print("In random")
        reply_token = event.reply_token
        select = random.sample(range(len(db)), 3)
        rstr = ""
        for i in range(len(select)):
            rstr = rstr + db[select[i]][0]
            if i != (len(select)-1):
                rstr = rstr + "\n"
        send_text_message(
            reply_token,
            rstr
        )
        self.go_back()

    def on_exit_random(self):
        print("Leave random")

    def is_going_to_base0(self, event):
        text = event.message.text
        return text.lower() == "g"

    def is_going_to_base1(self, event):
        text = event.message.text
        return text.lower() == "v"

    def is_going_to_base2(self, event):
        text = event.message.text
        return text.lower() == "t"

    def is_going_to_base3(self, event):
        text = event.message.text
        return text.lower() == "w"

    def is_going_to_base4(self, event):
        text = event.message.text
        return text.lower() == "r"

    def is_going_to_base5(self, event):
        text = event.message.text
        return text.lower() == "b"

    def on_enter_base0(self, event):
        print("In base0")
        reply_token = event.reply_token
        rstr = search_base(0)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_base0(self):
        print("Leave base0")

    def on_enter_base1(self, event):
        print("In base0")
        reply_token = event.reply_token
        rstr = search_base(1)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_base1(self):
        print("Leave base1")

    def on_enter_base2(self, event):
        print("In base0")
        reply_token = event.reply_token
        rstr = search_base(2)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_base2(self):
        print("Leave base2")

    def on_enter_base3(self, event):
        print("In base0")
        reply_token = event.reply_token
        rstr = search_base(3)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_base3(self):
        print("Leave base3")

    def on_enter_base4(self, event):
        print("In base0")
        reply_token = event.reply_token
        rstr = search_base(4)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_base4(self):
        print("Leave base4")

    def on_enter_base5(self, event):
        print("In base0")
        reply_token = event.reply_token
        rstr = search_base(5)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_base5(self):
        print("Leave base5")

    def is_going_to_flavor00(self, event):
        text = event.message.text
        return text.lower() == "a"

    def is_going_to_flavor01(self, event):
        text = event.message.text
        return text.lower() == "b"

    def is_going_to_flavor02(self, event):
        text = event.message.text
        return text.lower() == "c"

    def is_going_to_flavor03(self, event):
        text = event.message.text
        return text.lower() == "d"

    def is_going_to_flavor04(self, event):
        text = event.message.text
        return text.lower() == "e"

    def is_going_to_flavor05(self, event):
        text = event.message.text
        return text.lower() == "f"

    def is_going_to_flavor06(self, event):
        text = event.message.text
        return text.lower() == "g"

    def is_going_to_flavor07(self, event):
        text = event.message.text
        return text.lower() == "h"

    def is_going_to_flavor08(self, event):
        text = event.message.text
        return text.lower() == "i"

    def is_going_to_flavor09(self, event):
        text = event.message.text
        return text.lower() == "j"

    def is_going_to_flavor10(self, event):
        text = event.message.text
        return text.lower() == "k"

    def is_going_to_flavor11(self, event):
        text = event.message.text
        return text.lower() == "l"

    def is_going_to_flavor12(self, event):
        text = event.message.text
        return text.lower() == "m"

    def on_enter_flavor00(self, event):
        print("In flavor00")
        reply_token = event.reply_token
        rstr = search_flavor(0)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_flavor00(self):
        print("Leave flavor00")

    def on_enter_flavor01(self, event):
        print("In flavor01")
        reply_token = event.reply_token
        rstr = search_flavor(1)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_flavor01(self):
        print("Leave flavor01")

    def on_enter_flavor02(self, event):
        print("In flavor02")
        reply_token = event.reply_token
        rstr = search_flavor(2)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_flavor02(self):
        print("Leave flavor02")

    def on_enter_flavor03(self, event):
        print("In flavor03")
        reply_token = event.reply_token
        rstr = search_flavor(3)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_flavor03(self):
        print("Leave flavor03")

    def on_enter_flavor04(self, event):
        print("In flavor04")
        reply_token = event.reply_token
        rstr = search_flavor(4)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_flavor04(self):
        print("Leave flavor04")

    def on_enter_flavor05(self, event):
        print("In flavor05")
        reply_token = event.reply_token
        rstr = search_flavor(5)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_flavor05(self):
        print("Leave flavor05")

    def on_enter_flavor06(self, event):
        print("In flavor06")
        reply_token = event.reply_token
        rstr = search_flavor(6)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_flavor06(self):
        print("Leave flavor06")

    def on_enter_flavor07(self, event):
        print("In flavor07")
        reply_token = event.reply_token
        rstr = search_flavor(7)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_flavor07(self):
        print("Leave flavor07")

    def on_enter_flavor08(self, event):
        print("In flavor08")
        reply_token = event.reply_token
        rstr = search_flavor(8)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_flavor08(self):
        print("Leave flavor08")

    def on_enter_flavor09(self, event):
        print("In flavor09")
        reply_token = event.reply_token
        rstr = search_flavor(9)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_flavor09(self):
        print("Leave flavor09")

    def on_enter_flavor10(self, event):
        print("In flavor10")
        reply_token = event.reply_token
        rstr = search_flavor(10)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_flavor10(self):
        print("Leave flavor10")

    def on_enter_flavor11(self, event):
        print("In flavor11")
        reply_token = event.reply_token
        rstr = search_flavor(11)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_flavor11(self):
        print("Leave flavor11")

    def on_enter_flavor12(self, event):
        print("In flavor12")
        reply_token = event.reply_token
        rstr = search_flavor(12)
        send_text_message(reply_token, rstr)
        self.go_back()

    def on_exit_flavor12(self):
        print("Leave flavor12")
    # def is_going_to_state1(self, event):
    #     text = event.message.text
    #     return text.lower() == "go to state1"

    # def is_going_to_state2(self, event):
    #     text = event.message.text
    #     return text.lower() == "go to state2"

    # def on_enter_state1(self, event):
    #     print("I'm entering state1")

    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "Trigger state1")
    #     self.go_back()

    # def on_exit_state1(self):
    #     print("Leaving state1")

    # def on_enter_state2(self, event):
    #     print("I'm entering state2")

    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "Trigger state2")
    #     self.go_back()

    # def on_exit_state2(self):
    #     print("Leaving state2")
