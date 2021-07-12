import login_system as login
def main():
    login
    choice=input("If you want to order off the menu, enter 'menu'.\nIf you want recieve a recommendation, enter 'recommendation'.\nIf you want to place a special cake order, enter 'cake'.\n").lower()
    if choice == "menu":
        import menu as m
        m
    if choice =="recommendation":
        import recommendation as r
        r
    if choice=="cake":
        import cake_order as c
        c
main()
