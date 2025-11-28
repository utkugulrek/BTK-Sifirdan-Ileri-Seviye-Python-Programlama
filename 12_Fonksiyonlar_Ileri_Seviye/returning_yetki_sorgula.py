def yetki_sorgula(page):
    def inner(role):
        match role:
            case "Admin":
                return f"{role} rolü {page} sayfasına erişebilir."
            case _:
                return f"{role} rolü {page} sayfasına erişemez."
    return inner

user1 = yetki_sorgula("Product Edit")
print(user1("Admin"))
print(user1("User"))
