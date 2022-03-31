# %%
# -*- coding: utf-8 -*-
# Exercise 11:Asking Questions

def main():
    print("How old are you?",end='')
    age=input()
    print("you are %s"%age)
    print("you are %r"%age)
    print("you are %d"%int(age))
    print("you are %r"%int(age))

    age2=input("How old are you 2? ")
    print("you are %s"%age2)

    print("How old are you?","How tall are you?","how much do you weigh?",sep="|",end='',flush=True)
    print("How old are you?","How tall are you?","how much do you weigh?",sep="|",flush=True)

if __name__ == "__main__":
    main()


# %%



