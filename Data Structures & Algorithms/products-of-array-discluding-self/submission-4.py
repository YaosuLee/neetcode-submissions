
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        # Khởi tạo mảng output gồm toàn số 1
        output = [1] * length

        # Bước 1: Tính tích lũy từ bên trái (Prefix) trực tiếp vào mảng output
        # output[i] sẽ chứa tích của tất cả các số đứng trước i
        for i in range(1, length):
            output[i] = output[i - 1] * nums[i - 1]

        # Bước 2: Duyệt ngược từ phải qua trái để nhân thêm tích lũy bên phải (Suffix)
        # Sử dụng một biến đơn thay vì một mảng phụ
        right_prod = 1
        for i in range(length - 1, -1, -1):
            # Tích loại trừ chính nó = (Tích bên trái đang có) * (Tích bên phải)
            output[i] = output[i] * right_prod

            # Cập nhật tích lũy bên phải để dùng cho phần tử tiếp theo bên trái
            right_prod *= nums[i]

        return output