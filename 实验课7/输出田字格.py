for i in range(11):
    if i in [0, 5, 10]:
        print("+ {0}+ {0}+".format('- ' * 4))
    else:
        print("|{: ^19}|".format('|'))