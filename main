from flet import *
def main(page:Page):
    page.title="calculator"
    t=Text(value="")
    page.horizontal_alignment="center"
    page.vertical_alignment="center"
    page.window.width=300
    page.window.height=500
    page.window.resizable=False
    def equal(text):
        ls=[]
        c=""
        for i in range(len(text)):
            if not(text[i].isdigit()):
                ls.append(text[i])
                c=text[i]
        # return ls
        print(ls)
        if len(ls)!=1:
            t.value=""
        else:

            ls_nums=text.split(ls[0])
            if len(ls_nums)==2:
                if c=="+":
                    t.value=t.value+"="+str(int(ls_nums[0])+int(ls_nums[1]))
                elif c=="-":
                    t.value=t.value+"="+str(int(ls_nums[0])-int(ls_nums[1]))
                elif c=="*":
                    t.value=t.value+"="+str(int(ls_nums[0])*int(ls_nums[1]))
                elif c=="/":
                    t.value=t.value+"="+str(int(ls_nums[0])/int(ls_nums[1]))
            else:
                t.value=""
        # page.update()


            
    def com_c(e):
        t.value=""
        page.update()
    def com_0(e):
        if not("=" in t.value):
            t.value=t.value+"0"
        else:
            t.value="0"
        page.update()

    def com_equal(e):
        equal(t.value)
        page.update()
    def com_minus(e):
        if not("=" in t.value):
            t.value=t.value+"-"
        else:
            t.value="-"
        page.update()
    def com_plus(e):
        if not("=" in t.value):
            t.value=t.value+"+"
        else:
            t.value="+"
        page.update()
    def com_3(e):
        if not("=" in t.value):
            t.value=t.value+"3"
        else:
            t.value="3"
        page.update()
    def com_2(e):
        if not("=" in t.value):
            t.value=t.value+"2"
        else:
            t.value="2"
        page.update()
    def com_1(e):
        if not("=" in t.value):
            t.value=t.value+"1"
        else:
            t.value="1"
        page.update()
    def com_4(e):
        if not("=" in t.value):
            t.value=t.value+"4"
        else:
            t.value="4"
        page.update()
    def com_5(e):
        if not("=" in t.value):
            t.value=t.value+"5"
        else:
            t.value="5"
        page.update()
    def com_6(e):
        if not("=" in t.value):
            t.value=t.value+"6"
        else:
            t.value="6"
        page.update()
    def com_divide(e):
        if not("=" in t.value):
            t.value=t.value+"/"
        else:
            t.value="/"
        page.update()
    def com_multi(e):
        if not("=" in t.value):
            t.value=t.value+"*"
        else:
            t.value="*"
        page.update()
    def com_9(e):
        if not("=" in t.value):
            t.value=t.value+"9"
        else:
            t.value="9"
        page.update()
    def com_8(e):
        if not("=" in t.value):
            t.value=t.value+"8"
        else:
            t.value="8"
        page.update()
    def com_7(e):
        if not("=" in t.value):
            t.value=t.value+"7"
        else:
            t.value="7"
        page.update()
    def com_can(e):
        if ("="in t.value):
            t.value=""
        else:
            if len(t.value)!=0:
                t.value=t.value[:-1]
        page.update()

    bt_c=ElevatedButton(text="C",on_click=com_c)
    bt_0=ElevatedButton(text="0",on_click=com_0)
    bt_equal=ElevatedButton(text="=",on_click=com_equal)
    bt_minus=ElevatedButton(text="-",on_click=com_minus)
    bt_plus=ElevatedButton(text="+",on_click=com_plus)
    bt_3=ElevatedButton(text="3",on_click=com_3)
    bt_2=ElevatedButton(text="2",on_click=com_2)
    bt_1=ElevatedButton(text="1",on_click=com_1)
    bt_4=ElevatedButton(text="4",on_click=com_4)
    bt_5=ElevatedButton(text="5",on_click=com_5)
    bt_6=ElevatedButton(text="6",on_click=com_6)
    bt_divide=ElevatedButton(text="/",on_click=com_divide)
    bt_multi=ElevatedButton(text="*",on_click=com_multi)
    bt_9=ElevatedButton(text="9",on_click=com_9)
    bt_8=ElevatedButton(text="8",on_click=com_8)
    bt_7=ElevatedButton(text="7",on_click=com_7)
    bt_can=ElevatedButton(text=" ",icon=icons.CANCEL_SHARP,icon_color="black",on_click=com_can,width=45)
    column_bt=Column([Row([bt_7,bt_8,bt_9,bt_multi]),Row([bt_4,bt_5,bt_6,bt_divide]),Row([bt_1,bt_2,bt_3,bt_plus]),Row([bt_c,bt_0,bt_equal,bt_minus])])
    maincolumn=Column([Container(content=Column([t,Container(content=bt_can,alignment=alignment.bottom_right)])),Container(content=column_bt,padding=5)],spacing=10)
    main_con=Container(maincolumn,alignment=alignment.center)
    page.add(main_con)
    

app(target=main)

