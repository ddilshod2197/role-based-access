class Rol:
    def __init__(self, rol_ismi):
        self.rol_ismi = rol_ismi

class Foydalanuvchi:
    def __init__(self, ism, familiya, rol):
        self.ism = ism
        self.familiya = familiya
        self.rol = rol

class RolBazasi:
    def __init__(self):
        self.rol_lar = []
        self.foydalanuvchilar = []

    def qo'sh_rol(self, rol):
        self.rol_lar.append(rol)

    def qo'sh_foydalanuvchi(self, foydalanuvchi):
        self.foydalanuvchilar.append(foydalanuvchi)

    def rolsini_chek(self, foydalanuvchi):
        return foydalanuvchi.rol.rol_ismi in [rol.rol_ismi for rol in self.rol_lar]

    def rolsini_ber(self, foydalanuvchi, rol):
        if self.rolsini_chek(foydalanuvchi):
            return f"Rol {rol.rol_ismi} {foydalanuvchi.ism} {foydalanuvchi.familiya} ga berildi"
        else:
            return f"Rol {rol.rol_ismi} {foydalanuvchi.ism} {foydalanuvchi.familiya} ga berilmadi"

baz = RolBazasi()

rol1 = Rol("Admin")
rol2 = Rol("Moderator")

baz.qo'sh_rol(rol1)
baz.qo'sh_rol(rol2)

foydalanuvchi1 = Foydalanuvchi("Ali", "Valiyev", rol1)
foydalanuvchi2 = Foydalanuvchi("Vali", "Valiyev", rol2)

baz.qo'sh_foydalanuvchi(foydalanuvchi1)
baz.qo'sh_foydalanuvchi(foydalanuvchi2)

print(baz.rolsini_ber(foydalanuvchi1, rol2))
print(baz.rolsini_ber(foydalanuvchi2, rol1))
```

Bu kodda biz ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro'yxatga ro
