class Demo:

    def config(self):
        print("Hello my name")



q = 8
print(type(q))
Hello = Demo

print(type(Hello))


class Com:

    def config(self):
        print("Hello bro")


Com1 = Com()
Com2 = Com()

Com.config(Com1)
Com.config(Com2)