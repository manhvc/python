# Họ tên: Vòng Chúng Mành
# Mã sinh viên: 22410017
# Đề 2:

class CongTy:
    def __init__(self, ma_cty: str, von_dh: float, thue: float):
        self._ma_cty = ma_cty
        self._von_dh = von_dh
        self._thue = thue

    def get_ma_cty(self):
        return self._ma_cty

    def get_thue(self):
        return self._thue

    def set_von_dh(self, von_dh: float):
        self._von_dh = von_dh

    def xet_doanh_thu(self):
        pass

    def xuat_data(self):
        return f'Ma Cty: {self._ma_cty}, \
        Von dieu hanh: {self._von_dh}, \
        Thue: {self._thue}'


class BatDongSan(CongTy):
    def __init__(self, ma_cty: str, von_dh: float, thue: float, so_ch: int, gia_ch: float):
        CongTy.__init__(self, ma_cty=ma_cty, von_dh=von_dh, thue=thue)
        self.__so_ch = so_ch
        self.__gia_ch = gia_ch

    def xuat_data(self):
        data = CongTy.xuat_data(self)
        print(f'{data}, \
                So can ho: {self.__so_ch}, \
                Gia moi can ho: {self.__gia_ch}')

    def xet_doanh_thu(self):
        doanh_thu = self._von_dh - (self.__so_ch * self.__gia_ch)
        if doanh_thu - (self.__gia_ch * self._thue) < 0:
            return 'Vượt'
        elif doanh_thu > 50:
            return 'Đạt'
        else:
            return 'Không Đạt'


class VanTai(CongTy):
    def __init__(self, ma_cty: str, von_dh: float, thue: float, tong_thu: float, chi_phi_mx: float):
        CongTy.__init__(self, ma_cty=ma_cty, von_dh=von_dh, thue=thue)
        self.__tong_thu = tong_thu
        self.__chi_phi = chi_phi_mx

    def xuat_data(self):
        data = CongTy.xuat_data(self)
        print(f'{data}, \
                Tong thu: {self.__tong_thu}, \
                Chi phi mua xe: {self.__chi_phi}')

    def xet_doanh_thu(self):
        if self._von_dh < self.__tong_thu:
            return 'Vượt'
        elif (self.__chi_phi * self._thue) > self.__tong_thu:
            return 'Đạt'
        else:
            return 'Không Đạt'


class GiaoDuc(CongTy):
    def __init__(self, ma_cty: str, von_dh: float, thue: float, tong_thu: float):
        CongTy.__init__(self, ma_cty=ma_cty, von_dh=von_dh, thue=thue)
        self.__tong_thu = tong_thu

    def xuat_data(self):
        data = CongTy.xuat_data(self)
        print(f'{data}, \
                Tong thu: {self.__tong_thu}')

    def xet_doanh_thu(self):
        if self._von_dh > self.__tong_thu:
            return 'Vượt'
        elif (self.__tong_thu * self._thue) > 10:
            return 'Đạt'
        else:
            return 'Không Đạt'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('=====================================================')
    print(f'Câu 1: Khởi tao dữ liệu')
    list_cty = [
        BatDongSan(ma_cty="B111", von_dh=108.5, thue=0.19, so_ch=65, gia_ch=1.3),
        BatDongSan(ma_cty="B112", von_dh=158.6, thue=0.15, so_ch=50, gia_ch=1.2),
        BatDongSan(ma_cty="B113", von_dh=130.8, thue=0.02, so_ch=67, gia_ch=1.1),
        VanTai(ma_cty="V201", von_dh=50.9, thue=0.06, tong_thu=61.1, chi_phi_mx=30.1),
        VanTai(ma_cty="V202", von_dh=80.5, thue=0.08, tong_thu=71.1, chi_phi_mx=0),
        GiaoDuc(ma_cty="G301", von_dh=39.3, thue=0.02, tong_thu=30.2),
        GiaoDuc(ma_cty="G302", von_dh=59.2, thue=0.03, tong_thu=65.6)
    ]
    print(f'Thông tin công ty đã khởi tạo')
    for cty in list_cty:
        cty.xuat_data()

    print('\n\n=====================================================')
    print(f'Câu 2: Xét doanh thu:')
    for cty in list_cty:
        print(f'Cong ty {cty.get_ma_cty()} doanh thu: {cty.xet_doanh_thu()}')

    print('\n\n=====================================================')
    print(f'Câu 3: Cập nhật vốn điều hành theo mã công ty')
    update_ma_cty = 'B114'
    update_von_dh = 110.5
    print(f'Cập nhật Mã công ty {update_ma_cty} với vốn điều hành {update_von_dh}')
    flag = 0
    for cty in list_cty:
        if update_ma_cty == cty.get_ma_cty():
            cty.set_von_dh(update_von_dh)
            cty.xuat_data()
            flag = 1
            break
    if flag == 0:
        print(f'Không tìm thấy mã công ty {update_ma_cty}. Không thể cập nhật')

    print('\n\n=====================================================')
    print(f'Câu 4: Tìm công ty có doanh thu la không dat')
    for cty in list_cty:
        if cty.xet_doanh_thu() == "Không Đạt":
            cty.xuat_data()

    print(f'\n\nCâu 5: Tìm các công ty có thuế nhỏ nhất')
    min_thue = 0.1
    for cty in list_cty:
        if min_thue > cty.get_thue():
            min_thue = cty.get_thue()
    for cty in list_cty:
        if cty.get_thue() == min_thue:
            cty.xuat_data()
